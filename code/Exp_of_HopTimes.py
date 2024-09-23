from initialize import *

Parameter = {
    "Coverage" :500,
    "DataLength" : 3611,
    "EdgeServerPositionBound" : 100000,
    "Velocity" : 27.7,
}

Times = 0


for ithExperiment in range(1, 9):

    Test = EdgeServerExperiment(Parameter)

    RunTime = 0

    ServiceEdge = 1
    ConnectedEdge = 1

    CurrentDelayTime = 0
    ServiceMigrationDelayTime = Test.GetServiceMigrationDelay()
    

    UESpeed =Test.GetUESpeed()
    BitRate = Test.GetBitRateRecord()
    BandWidth = Test.GetBandWidth()
    EdgeServer = Test.GetEdgeServerPosition()

    Enough = True

    Test.SetServiceSize(4)

    """ Get the ans of CurrentDelayTime > Service Migration Delay """
    while CurrentDelayTime < ServiceMigrationDelayTime:
        hop = ConnectedEdge - ServiceEdge

        CurrentDelayTime = (hop+1) * (BitRate[RunTime]/BandWidth) + Test.GetWireLessDelay()

        if UESpeed * RunTime > EdgeServer[ConnectedEdge] :
            ConnectedEdge += 1
        
        if ConnectedEdge == len(EdgeServer):
            Enough = False
            break
        
        RunTime += 1 
    
    Times += hop

    print(f"=========第{ithExperiment}次實驗=========")

    print(f'運行時間: {RunTime}')

    print(f'最大跳躍次數: {hop}')

    print(f'本次Service大小: {Test.GetServiceSize()} MB')

    print(f'當前延遲: {CurrentDelayTime} s' )

    print(f'遷移延遲: {ServiceMigrationDelayTime} s')

    print(f'伺服器範圍是否足夠: {Enough}')

print(f"平均最大跳躍次數: {Times/10}")