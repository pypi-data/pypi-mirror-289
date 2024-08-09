from obstechutils.db import DataBase
from obstechutils.types import TimeType, TimeDeltaType
from obstechutils import logging
from obstechutils.dataclasses import strictdataclass, Field

from astropy.time import Time
from functools import wraps

# only configured reading the database for coeffs, no calibration
# actually done here

@strictdataclass
class PyrgeometerCalibrator:
    """Calibration of a sky IR temperature sensor."""

    id: str    
    db: DataBase = DataBase.from_credentials(
        name='ElSauceWeather', 
        user='generic_obstech'
    )   
    db_table_name: str = 'cloudsensors_params'
    update_period: TimeDeltaType = '1d'
    coefficients = list[float] = Field(
        default_factory=lambda: [100., 0., 0., 0., 0., 0., 0.],
        min_length=7, max_length=7,
    )
    last_update_time:  TimeType = '1980-01-01'
    
    def __getattribute__(self, x):
        if x in ['last_update_time', 'coefficients']:
            self.update()
        return super().__getattribute__(x)

    def temperature_correction(self, temperature: float) -> float:

        K = self.coefficients         
        K1, K2, K3, K4, K5, K6, K7 = [
            K[0]/100, K[1]/10, K[2]/100, K[3]/1000, K[4]/100, K[5]/10, K[6]/100
        ]

        A = abs(K2 - temperature)
        S = np.sign(temperature - K2)

        T67 = sgn(K6) * S * A if A < 1 else K6 * S * np.log10(A) + K7
        Td = K1 * S * A + K3 * exp(K4 * temperature)**K5 + T67

        return Td

    def update(self):

        if (now := Time.now()) - self.last_update_time > self.update_period:

            try:

                query = """
                    SELECT k1,k2,k3,k4,k5,k6,k7 
                    FROM {self.db_table_name}
                    WHERE identifier = '{self.id}'
                    ORDER BY id
                    DESC LIMIT 1
                """

                with self.db.connect() as conn:
                    cursor = conn.cursor()
                    cursor.execute(query)
                    values = cursor.fetchall()

                self.coefficients[:] = values
                object.__setattr__(self, 'last_update_time', now)

            except Exception as e:

                logger.error(f'could not update coefficients')

            else:

                logger.info(f'coefficients uipdated for {self.id}: {values}')
