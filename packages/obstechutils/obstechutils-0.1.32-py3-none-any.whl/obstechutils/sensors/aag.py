from obstechutils.devices.meteosensor import MeteoSensor
from obstechutils.devices.pyrgeometer import PyrgeometerCalibrator
from obstechutils.dataclasses import strictdataclass
from obstechutils.stats import MeasurementBinner, MeasurementType

import time

@strictdataclass
class AAG(MeteoSensor):
            
    timeout: float = 0.5
    baudrate: int = 9600
    vendor_id: int = 1659
    product_id: int = 8963
    id: str = 'aag'
    binner: MeasurementBinner = MeasurementBinner()
    cloud_calib: PyrgeometerCalibrator = PyrgeometerCalibrator(id='aag')

    def read_device(self, cmd, wait=0.1):
        
        # Try to read a second time if there is an error 
        ntries = 2
        for i in range(ntries):
            try:
                self.send(cmd)
                time.sleep(wait)
                rcv = self.readline()
                rcv = rcv[3:].split('\x11')[0].split()
                rcv = [x.split('!')[0] for x in rcv]
                rcv = [self.to_int(x) for x in rcv]
                return rcv
            except Exception as e:
                if i < ntries-1:
                    self.reconnect(wait_before=0.5, wait_after=0.5)

        raise e

    def measurement(self):

        # read data
        try:
            # If we assume at most two reading errors, this should 
            # take at most 3.1 s + reconnection time.  
            temperature = 0.01 * self.read_device('T!')[0]
            temperature_ir = 0.01 * self.read_device('S!')[0]
            rain_freq = self.read_device('E!', wait=0.3)[0]
            wind_speed = self.read_device('V!')
            d5, d6, d7 = self.read_device('C!')
        except Exception as e:
            print(f"could not read AAG sensor: {e}")
            return {}

        # check if wind is obtained
        wind = wind[0] if len(wind) else 0.

        # a bit mysterious here
        d6 = 56/(1023 / min(max(d6, 1), 1022) - 1)
        d7 = 56/(1023 / min(max(d6, 1), 1022) - 1)
        d7 = 1/(np.log10(d7)/3450 + 1 / (273.15 + 25)) - 273.15

        m = dict(
            unix_time = Time.time().unix,
            temperature = temperature,
            temperature_ir = temperature_ir,
            voltage = d5,
            rain_freq = d6,
            light = d7,
            wind_speed=wind_speed
        )

        return m

    def after_averaging(self, m: MeasurementType) -> MeasurementType:

        temperature = m['temperature']
        temperature_ir = m['temperature_ir']

        temperature_diff = self.cloud_calib.temperature_correction(temperature)
        temperature_sky = temperature_ir - temperature_diff

        m['temperature_diff'] = temperature_diff
        m['temperature_ir'] = temperature_ir

        return m

def monitor_aag1():
    cloud_calib = PyrgeometerCalibrator(id='aag1')
    sensor = AAG(id='aag1', cloud_calib=cloud_calib, vid=1024, pid=24577)
    sensor.loop_forever()

def monitor_aag2():
    cloud_calib = PyrgeometerCalibrator(id='aag2')
    sensor = AAG(id='aag2', cloud_calib=cloud_calib, vid=1659, pid=8953)
    sensor.loop_forever()

