from obstechutils.devices.meteosensor import MeteoSensor
from obstechutils.dataclasses import strictdataclass
from obstechutils.stats import MeasurementBinner, MeasurementType
from obstechutils import meteo
from obstechutils import logging
from obstechutils.connection import SerialException

import pynmea2
import time

@strictdataclass
class NM150(MeteoSensor):

    timeout: float = 0.1
    baudrate: int = 4800
    vendor_id: int = 1741
    product_id: int = 289
    id: str = 'nm150'
    binner: MeasurementBinner = MeasurementBinner(
        angle_variables=['nm150_wind_dir'],
        maximum_variables={'nm150_wind_dir': 'nm150_wind_gust'}
    )

    @classmethod
    def parse_wimda_packet(cls, packet):

        m = None

        if packet.startswith('$WIMDA'):
            try:
                m = pynmea2.parse(packet)
                m.b_pressure_bar = float(m.b_pressure_bar)
                m.air_temp = float(m.air_temp)
                m.wind_speed_meters = float(m.wind_speed_meters)
                m.direction_true = float(m.direction_true)
                m.rel_humidity = float(m.rel_humidity)
            except:
                ...

        return m

    def get_wimda_message(self):

        # Every second a GPGGA and a WIMDA message are published with
        # a separation of ~ 0.16s.  After discarding past data, wait 
        # ~ 1s to ensure a can WIMDA be read.
        #
        # The maximum time the function can take  is given by
        #       1 + 3 * self.timeout = 1.3 seconds
        # under the most improbable pessimistic scenario

        while self.in_waiting():
            packet = self.readline(errors='replace').strip()

        wimda_wait_time = 0.2 if packet.startswith('$GPGGA') else 1.
        time.sleep(wimda_wait_time)

        # Read the next two messages if present
        i = 0
        while (i := i + 1) <= 2 and self.in_waiting():
            packet = self.readline(errors='replace').strip()
            if (m := self.parse_wimda_packet(packet)) is not None:
                return m

        raise RuntimeError('No valid WIMDA packet')

    def measurement(self):

        logger = logging.getLogger()
        id = f'weather sensor {self.id}'

        # Try to get a correct packet within a sampling time, as
        # long as we want a 0.2 Hz (5 s) frequency. 
        #
        # * First attempt: at most ~ 1.3 seconds 
        # * Subsequent attemps: at most ~ 1.4 seconds (reconnect is fast)
        #
        # Within 1 sampling time of 5 s, either the following will have
        # occured:
        #  * a well-formed packet has been read
        #  * or three attempts and a reconnection to port have been tried

        t = time.time()
        needs_reconnect = False
        message = None
        n_tries = 0

        while message is None and time.time() - t < self.sampling - 1.5:

            n_tries += 1

            try:

                if needs_reconnect:
                    logger.info(f'{id}: try to reconnect to serial port')
                    self.reconnect()
                    needs_reconnect = False

                # try to read WIMDA NMEA packet. That takes ~ 1 s (max 1.3s) 
                message = self.get_wimda_message()

            except SerialException as e:

                logger.info(f'{id}: serial port error: {e}')
                needs_reconnect = True

            except Exception as e:

                # after every second consecutive failure to have a correct 
                # NMEA packet we will try a reconnect just in case
                if n_tries % 2 == 0:
                    msg = (f'{id}: {n_tries} consecutive failures '
                            'to get a properly filled WIMDA packet')
                    logger.warning(msg)
                    needs_reconnect = True

        else:

            logger.warning(f'{id}: no measurement obtained')
            return { }

        dewpoint = meteo.dew_point(message.air_temp, message.rel_humidity)
        m = dict(
            unix_time = Time.now().unix,
            pressure = message.b_pressure_bar * 1000,
            temperature = message.air_temp,
            wind_speed = message.wind_speed_meters,
            wind_dir = message.direction_true,
            humidity = message.rel_humidity,
            dew_point = dewpoint,
        )

        msg = (f"{m['date']} {m['temperature']:.1f} {m['pressure']:.1f}")
        logger.debug(msg)

        return m

def monitor_nm150():
    sensor = NM150(id='nm150', vid=1741, pid=289)
    sensor.loop_forever()

