from LogiTyme import LogiTyme
logityme = LogiTyme(env="local",maxTime=5)
logityme.StartReport()

@logityme.smart_threshold_check(maxTimeLimit=3)
def slow_function(n):
  result = 0
  for i in range(n):
    for j in range(n):
      result += i*j
      print(result)

  return result

@logityme.smart_threshold_check(maxTimeLimit=2)
def slow_function2(n):
  result = 0
  for i in range(n):
    for j in range(n):
      result += i*j
      print(result)

  return result

slow_function(20)
slow_function2(20)

logityme.LogiFuncStart(name="for-loop", maxLimit=3)
re = 0
for i in range(500):
  for j in range(500):
    re += i * j
    print(re)
logityme.LogiFuncEnd()

logityme.GenerateReport(saveFile=False)
