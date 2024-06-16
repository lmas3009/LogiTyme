from src.logityme.logityme import LogiTyme

logityme = LogiTyme(env="local")

logityme.StartReport()

logityme.LogiFuncStart(name="forLoop")
for i in range(500):
    for j in range(500):
        print(i*j)
logityme.LogiFuncEnd()

def LogFunction():
    for i in range(500):
        for j in range(500):
            print(i * j)

LogFunction()

logityme.GenerateReport(saveFile=False)
