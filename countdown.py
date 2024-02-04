import time as t

# defining countdown function
def countdown(time):
    while time:
        # The divmod function in Python returns a tuple containing the quotient and remainder of the division of two numbers.
        mins,secs = divmod(time,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end="\r")
        t.sleep(1)
        time-=1
    print("fire in the hole!")
# time in seconds
time = input("enter the time in seconds")
time = int(time)
countdown(time)