import RPi.GPIO as GPIO
import time
from datetime import date
from datetime import datetime
import calendar


GPIO.setmode(GPIO.BOARD)


GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

servo1 = GPIO.PWM(7,50)
servo2 = GPIO.PWM(11,50)
servo3 = GPIO.PWM(13,50)
servo4 = GPIO.PWM(15,50)
servo5 = GPIO.PWM(16,50)
servo6 = GPIO.PWM(18,50)
servo7 = GPIO.PWM(22,50)

#get the day of the week and the time
my_date = date.today()
print(calendar.day_name[my_date.weekday()]) #this is the day of the week
today = calendar.day_name[my_date.weekday()]

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


#define run motor
def run_motor(day_of_week):
    
    print(day_of_week)
    
    if(day_of_week == "Monday"):
        servo = servo1
        
    if(day_of_week == "Tuesday"):
        servo = servo2
    
    if(day_of_week == "Wednesday"):
        servo = servo3
        
    if(day_of_week == "Thursday"):
        servo = servo4
    
    if(day_of_week == "Friday"):
        servo = servo5
        
    if(day_of_week == "Saturday"):
        servo = servo6
        
    if(day_of_week == "Sunday"):
        servo = servo7
        
    
    servo.start(0)
    print ("Waiting for 2 seconds")
    time.sleep(2)

    print ("Rotating 45ish degrees")

    servo.ChangeDutyCycle(4)
    time.sleep(2)

    # Turn back to 0 degrees
    print ("Turning back to 0 degrees for 2 seconds")
    servo.ChangeDutyCycle(2)
    time.sleep(2)
    servo.stop()
    #end
    GPIO.cleanup()
    print ("Goodbye")




##################################################

#run the motor

i = 1
while(i > 0):
    if(current_time == 9): #if time is 9AM, the turn the motor (we decided to do 9AM by default but you can change this to whatever time you need (military time))
        run_motor(today)
        

