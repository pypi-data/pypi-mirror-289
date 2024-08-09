from obstechutils.connection import SerialConnection
from obstechutils.dataclasses import strictdataclass, Field
from obstechutils.mqtt import MQTTClient
from obstechutils.precise_timing import average as average_function
from obstechutils import logging
from obstechutils.stats import MeasurementType, MeasurementBinner

from abc import ABC, abstractmethod

@strictdataclass
class MeteoSensor(SerialConnection, ABC):
            
    mqtt: MQTTClient    
    interval: TimeDeltaType = '1m'
    sampling: TimeDeltaType = Field(default='5s', ge='5s')
    sync: str = 'uct'
    binner: MeasurementBinner = MeasurementBinner()

    def loop_forever(self) -> None:
        
        logger = logging.getLogger()
        self.connect()

        while True:

            m = self.average_measurement()
            if not m:
                msg = 'no average measurement for weather sensor {self.id}'
                logger.error(msg)
                continue

            avg_name = 'last_minute' if interval.sec == 60 else 'average'
            topic = f'/ElSauce/Weather/{self.id}_{avg_name}'
            self.mqtt.publish_json(topic=topic, payload=m)

    def average_measurement(self) -> MeasurementType:

        logger = logging.getLogger()

        averager = average_function(
            interval=self.interval, sampling=self.sampling, sync=self.sync,
            averaging_fun=self.binner, return_times=True,
        )
        def measurement_function():
            m = self.measurement()
            if m:
                topic = '/ElSauce/Weather/Status/{self.id}'
                self.mqtt.publish(topic=topic, payload='OK')
            return m

        (date_start, date_end), dates, m = averager(measurement_function)()

        m['date_start'] = date_start.isot
        m['date_end'] = date_end.isot
        m['n_measurements'] = len(dates)
        m['average_type'] = self.binner.average_type

        logger.info(
            f"sensor {self.id}: measurement average for "
            f"{m['date_start']} - {m['date_end']}: {n_measurements} points"
        )

        m = self.after_averaging(m)
        m = {f'{self.id}_{key}': val for key, val in m.items()}

        return m

    @abstractmethod
    def measurement(self) -> MeasurementType: ...

    def after_averaging(self, m: MeasurementType) -> MeasurementType:
        return m
