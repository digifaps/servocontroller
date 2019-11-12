#!/usr/bin/env python3

import threading
import time
from functions.sqlquery import sql_query, sql_query2
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
#kit.continuous_servo[1].throttle = -0.1
#kit.continuous_servo[1].throttle = 0

kit = ServoKit(channels=16)

def thread_servo(result):
    print(result["serv_id"],result["deg_min"],result["deg_max"],result["sleep_min"],result["sleep_max"])
    kit.servo[int(result["serv_id"])].angle = int(result["deg_min"])
    time.sleep(int(result["sleep_min"]))
    kit.servo[int(result["serv_id"])].angle = int(result["deg_max"])
    time.sleep(int(result["sleep_max"]))
    kit.servo[int(result["serv_id"])].angle = int(result["deg_min"])

def button_callback(channel):
    print("Button was pushed!")
    results = sql_query(''' SELECT * FROM data_table''')    
    for result in results:
        x = threading.Thread(target=thread_servo, args=(result,))
        threads.append(x)
        x.start()
    for result, thread in enumerate(threads):
        #print("Main    : before joining thread %d.", index)
        thread.join()
    
    print("Done")


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(17,GPIO.RISING,callback=button_callback,bouncetime=500)

#

if __name__ == "__main__":

    threads = list()
    while True:   
        a = 1
    # for result in results:
    #    x = threading.Thread(target=thread_servo, args=(result,))
    #    threads.append(x)
    #    x.start()

   # for result, thread in enumerate(threads):
        #print("Main    : before joining thread %d.", index)
    #    thread.join()
        #print(result["serv_id"])
    
    
#message = input("Press enter to quit\n\n")

GPIO.cleanup()

