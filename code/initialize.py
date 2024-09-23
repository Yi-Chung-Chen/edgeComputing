import random


class EdgeServerExperiment():

    def __init__(self, Parameter: dict):
        
        self.ServiceSize = random.randint(1, 8) # MB 
        self.DataLength = Parameter["DataLength"]
        self.Coverage = Parameter["Coverage"] # m
        self.EdgeServerPositionBound = Parameter["EdgeServerPositionBound"] # m
        self.Velocity = Parameter["Velocity"] # m/s
        self.WirelessDelay = 0.0005 # s
        self.DownTime = 0.1 # s
        self.BandWidth = 50 # MB
        self.BitRateRecord = self.GenBitRateRecord()
        self.EdgeServerPosition = self.GenEdgeServer()
    

    def SetServiceSize(self, ServiceSize):
        """Function to Set Service Size"""

        self.ServiceSize = ServiceSize


    def GenBitRate(self):
        """Function To Generate Bitrate In The Random Range"""

        BitRate =  self.ServiceSize * 0.1 * random.uniform(0.002, 1) # MB

        return BitRate

    def GenBitRateRecord(self):
        """Function To Generate BitRate List And List.Length Is According To The Iser Set"""
        
        BitRateRecord = [self.GenBitRate() for i in range(self.DataLength)]

        return BitRateRecord

    def GenEdgeServer(self):
        """Function To Generate Edge Server Acoording To The Coverage"""

        EdgeServerPosition = [i for i in range(0, self.EdgeServerPositionBound + self.Coverage, self.Coverage)]
        
        return EdgeServerPosition
    
    def GetUESpeed(self):
        """Function To get User Equipment Speed"""

        return self.Velocity
    
    def GetBitRateRecord(self):
        """Function To Get BitRate"""

        return self.BitRateRecord
    
    def GetEdgeServerPosition(self):
        """Function To Get Edge Server Position"""

        return self.EdgeServerPosition

    def GetServiceSize(self):
        """Function To Get Service Size"""

        return self.ServiceSize

    def GetBandWidth(self):
        """Function To Get BandWidth"""

        return self.BandWidth
    
    def GetWireLessDelay(self):
        """Function To Get Wireless Delay"""

        return self.WirelessDelay

    def GetServiceMigrationDelay(self):
        """Function To Get Service Migration Delay Time"""

        ServiceMigrationDelayTime = self.ServiceSize/self.BandWidth + self.DownTime

        return ServiceMigrationDelayTime

    def BasicDelayTime(self, RunTime, Hop):
        """Function To Get Wireless Delay + BitRate[RunTime]/Bandwidth """

        BasicDelay = (Hop + 1) * self.BitRateRecord[RunTime]/self.BandWidth + self.WirelessDelay  # 至少會有一層語UE相連的Delay

        return BasicDelay

