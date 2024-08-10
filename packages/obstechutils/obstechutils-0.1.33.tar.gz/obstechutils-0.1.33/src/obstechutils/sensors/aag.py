from __future__ import annotations

from obstechutils.sensors.meteosensor import MeteoSensor
from obstechutils.sensors.pyrgeometer import PyrgeometerCalibrator
from obstechutils.dataclasses import strictdataclass
from obstechutils.stats import MeasurementBinner, MeasurementType
import numpy as np
import time
from astropy.time import Time

@strictdataclass
class AAG(MeteoSensor):
            
    timeout: float = 0.5
    baudrate: int = 9600
    id: str = 'aag'
    binner: MeasurementBinner = MeasurementBinner()
    cloud_calib: PyrgeometerCalibrator | None = None

    def read_device(self, cmd, wait=0.1):
        
        # Try to read a second time if there is an error 
        ntries = 2
        for i in range(ntries):
            try:
                self.send(cmd)
                rcv = self.receive()
                rcv = rcv[3:].split('\x11')[0].split()
                rcv = [x.split('!')[0] for x in rcv]
                rcv = [int(x) for x in rcv]
                return rcv
            except Exception as e:
                print(f'device error: {e}')
                if i < ntries-1:
                    self.reconnect(wait_before=0.5, wait_after=0.5)
                else:
                    raise

    def measurement(self):

        # read data
        try:
            # If we assume at most two reading errors, this should 
            # take at most 3.1 s + reconnection time.  
            temperature = 0.01 * self.read_device('T!')[0]
            temperature_ir = 0.01 * self.read_device('S!')[0]
            rain_freq = self.read_device('E!', wait=0.3)[0]
            try:
                d5, d6, d7 = self.read_device('C!')
            except:
                d5, d6, d7 = 0, 0, 0
            wind = self.read_device('V!')
        except Exception as e:
            print(f"could not read AAG sensor: {e}")
            return {}

        # check if wind is obtained
        wind_speed = wind[0] if len(wind) else 0.

        # a bit mysterious here
        d6 = 56/(1023 / min(max(d6, 1), 1022) - 1)
        d7 = 56/(1023 / min(max(d6, 1), 1022) - 1)
        d7 = 1/(np.log10(d7)/3450 + 1 / (273.15 + 25)) - 273.15

        m = dict(
            unix_time = Time.now().unix,
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

        cal = self.cloud_calib
        temperature_diff = 0
        if cal:
            temperature_diff = cal.temperature_correction(temperature) 
        temperature_sky = temperature_ir - temperature_diff

        m['temperature_diff'] = temperature_diff
        m['temperature_sky'] = temperature_sky

        return m


