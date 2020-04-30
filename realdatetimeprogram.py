from datetime import datetime

now = datetime.now()

print(now.date())

print("hrs", now.hour, "Seconds", now.sec)

print(now.time())


#Output------------------
#2020-04-30
#('hrs', 20, 'Seconds', 4)
#20:33:04.115000
