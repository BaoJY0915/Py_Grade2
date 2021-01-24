import time

lctime = time.localtime()
lotime = time.strftime('%A, %d.%B %Y %I:%M %p',lctime)

print(lotime)
