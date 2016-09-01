from datetime import datetime

now = datetime.now()
print (now)

print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)

print ("The date is %s/%s/%s" %(now.month ,now.day ,now.year))
print ("The time is %s:%s:%s" %(now.hour ,now.minute ,now.second))
