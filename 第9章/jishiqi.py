import time
a = time.monotonic()
b = time.ctime(a)
print(b)
startPerfCounter = time.perf_counter()
print(startPerfCounter)
time.sleep(0.24)
otherLoopPerfCounter = time.perf_counter()
otherLoopPerf = otherLoopPerfCounter - startPerfCounter
print(otherLoopPerf)
