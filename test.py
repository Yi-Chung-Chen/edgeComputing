import time


class EdgeComputing():
    def __init__(self, R: float, W: float, np: float, C: float, wl: float):
        self.TranSpeed = R * 10**3
        self.Bandwidth = W * 10**6
        self.NoisePower = np
        self.ServiceSize = C * 10**3
        self.WaveLength = wl
        self.ts = C/R

    def SNR(self) -> float:
        ratio = self.TranSpeed/self.Bandwidth
        snr = 2**ratio - 1 
        return snr

    def Power(self, d) -> float:
        snr = self.SNR()
        power = self.NoisePower*snr*(d**2)/(self.WaveLength**2)
        return power

    def migration_energy_consumption(self, d) -> float:
        Pm = self.Power(d) # distance between targe and source
        Emc = self.ServiceSize*Pm/self.TranSpeed
        return Emc

    def communication_energy_consumption(self, d) -> float:
        Pc = self.Power(d) # distancce between user and source
        Ecc = Pc*self.ts  # 暫時只考慮tranmission delay，實際上要考慮 transmission/processing/queue delay
        return Ecc

ue_speed = 14 # m/s -> 100 km/hr
total_energy_consumption = 0

# --- bs1 ----500---- bs2 ----500---- bs3
server_position = [0, 250, 500,750,1000]

i = 0
serverNo = 0
ec = EdgeComputing(R=200, W=5, np=3, C=1000, wl=0.125)
do_migration = False
mode_on = False
while ue_speed*i<server_position[-1]:
    if not mode_on:
        if ue_speed*i>=250 and do_migration==False: # service migration from bs1 to bs2
            do_migration = True
            total_energy_consumption += ec.migration_energy_consumption(server_position[1]-server_position[0])
            serverNo = 1
        
        if ue_speed*i>=750 and do_migration == True: # service migration from bs2 to bs3
            do_migration = False
            total_energy_consumption += ec.migration_energy_consumption(server_position[-1]-server_position[1])
            serverNo = 2
    else:
        if ue_speed*i>=750 and do_migration == False:
            do_migration = True
            total_energy_consumption +=ec.migration_energy_consumption(1000)
            serverNo = 2

    total_energy_consumption += (ec.communication_energy_consumption(abs(ue_speed*i-server_position[serverNo]))/2)
    
    print(f'當前服務基站bs{serverNo+1}')
    print(f'ue位置:{ue_speed*i}，與bs{serverNo+1}的距離:{abs(ue_speed*i-server_position[serverNo])}')
    print(f'當前總能耗:{total_energy_consumption:.2f}')
    
    i+=1
    time.sleep(1)


