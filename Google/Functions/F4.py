#finding leftover seconds

def seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - (hours*3600))//60
    real_seconds = (seconds - (hours*3600) - (minutes*60))
    return hours,minutes ,real_seconds

a = seconds(69000)
print("The real hours,minutes and seconds of given seconds is ",a)