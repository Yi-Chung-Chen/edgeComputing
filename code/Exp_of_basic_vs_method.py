from initialize import *

Parameter = {
    "Coverage" : 500,
    "DataLength" : 145,
    "EdgeServerPositionBound" : 4000,
    "Velocity" : 27.7,
}

Experiment = EdgeServerExperiment(Parameter)
UESpeed = Experiment.GetUESpeed()
EdgeServer = Experiment.GetEdgeServerPosition()
UELocation = []


"""Case 1 : Always Migration"""

RunTime = 0
ServiceEdgeServer = 1
CurrentEdgeServer = 1
TotalDelayTime = 0 
Record1 = []

while UESpeed * RunTime<EdgeServer[-1]:

    if UESpeed * RunTime > EdgeServer[CurrentEdgeServer]:
        TotalDelayTime += Experiment.GetServiceMigrationDelay()
        CurrentEdgeServer += 1
        ServiceEdgeServer += 1

    Hop = CurrentEdgeServer - ServiceEdgeServer 

    TotalDelayTime += Experiment.BasicDelayTime(RunTime, Hop)

    Record1.append(TotalDelayTime)
    UELocation.append(UESpeed * RunTime)
    
    RunTime += 1

print(Experiment.GetServiceSize())

print(f'AlwaysMigration Total Delay Time: {TotalDelayTime} s')


"""Case 2 : Method"""

RunTime = 0
ServiceEdgeServer = 1
CurrentEdgeServer = 1
TotalDelayTime = 0 
Record2 = []

while UESpeed * RunTime < EdgeServer[-1]:

    if UESpeed * RunTime > EdgeServer[CurrentEdgeServer]:
        CurrentEdgeServer += 1

    Hop = CurrentEdgeServer - ServiceEdgeServer

    if Hop > 1:
        # trigger service migration
        TotalDelayTime += Experiment.GetServiceMigrationDelay()
        ServiceEdgeServer = CurrentEdgeServer
        Hop = 0

    TotalDelayTime += Experiment.BasicDelayTime(RunTime, Hop)
    Record2.append(TotalDelayTime)

    RunTime += 1

print(f'Method 的 Total Delay Time: {TotalDelayTime} s')

print(Experiment.GetServiceSize())