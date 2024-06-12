"""Module providing a function time counting."""

import time


class EdgeComputing():
    """"class representing EdgeComputing"""

    def __init__(self, transmission_speed: float, bandwidth: float,
                 noise_power: float, service_size: float, wave_length: float):
        self.transmission_speed = transmission_speed * 10**3
        self.bandwidth = bandwidth * 10**6
        self.noise_power = noise_power
        self.service_size = service_size * 10**3
        self.wave_length = wave_length
        self.communication_time = service_size/bandwidth

    def signal_noise_ratio(self) -> float:
        """funtion to calculate signal-noise ratio"""

        ratio = self.transmission_speed/self.bandwidth
        snr = 2**ratio-1
        return snr

    def power(self, distance: float) -> float:
        """function to calculate power"""

        snr = self.signal_noise_ratio()
        power = self.noise_power*snr*(distance**2)/(self.wave_length**2)
        return power

    def migration_energy_consumption(self, distance_between_target_and_source: float) -> float:
        """function to calculate migration_energy_consumption"""

        power_of_migration = self.power(distance_between_target_and_source)
        energy_of_migration_consumption = self.service_size*power_of_migration/self.transmission_speed
        return energy_of_migration_consumption

    def communication_energy_consumption(self, distacne_between_source_and_ue: float) -> float:
        """function to calculate communication_energy_consumption"""

        power_of_communication = self.power(distacne_between_source_and_ue)
        energy_of_communication_consumption = power_of_communication*self.communication_time
        # 暫時只考慮tranmission delay，實際上要考慮 transmission/processing/queue delay
        return energy_of_communication_consumption

UE_SPEED = 14 # m/s -> 100 km/hr
TOTAL_CONSUMPTION = 0

# --- bs1 ----500---- bs2 ----500---- bs3
SERVER_POSITION = [0, 250, 500, 750, 1000]

SECOND = 0
SERVER_NO = 0
EC = EdgeComputing(transmission_speed=200, bandwidth=5, 
                   noise_power=3, service_size=1000, wave_length=0.125)

DO_MIGRATION = False
MODE_ON = False

while UE_SPEED*SECOND<SERVER_POSITION[-1]:
    if not MODE_ON:
        if UE_SPEED*SECOND>=250 and DO_MIGRATION is False: # service migration from bs1 to bs2
            DO_MIGRATION = True
            TOTAL_CONSUMPTION += EC.migration_energy_consumption(SERVER_POSITION[1]-SERVER_POSITION[0])
            SERVER_NO = 1
        
        if UE_SPEED*SECOND>=750 and DO_MIGRATION is True: # service migration from bs2 to bs3
            DO_MIGRATION = False
            TOTAL_CONSUMPTION += EC.migration_energy_consumption(SERVER_POSITION[-1]-SERVER_POSITION[1])
            SERVER_NO = 2
    else:
        if UE_SPEED*SECOND>=750 and DO_MIGRATION is False:
            DO_MIGRATION = True
            TOTAL_CONSUMPTION +=EC.migration_energy_consumption(1000)
            SERVER_NO = 2

    TOTAL_CONSUMPTION += (EC.communication_energy_consumption(abs(UE_SPEED*SECOND-SERVER_POSITION[SERVER_NO]))/2)
    
    print(f'當前服務基站bs{SERVER_NO+1}')
    print(f'ue位置:{UE_SPEED*SECOND}，與bs{SERVER_NO+1}的距離:{abs(UE_SPEED*SECOND-SERVER_POSITION[SERVER_NO])}')
    print(f'當前總能耗:{TOTAL_CONSUMPTION:.2f}')
    SECOND+=1
    time.sleep(1.0)
