# Temp file to blink LED
# Author: Rafael Lima
# License: Private
# Date: 29/12/2017
#######################################################################################

# Import libraries
import RPi.GPIO as GPIO
import time                           
#######################################################################################

blink_time  = 0.0005    # Define blink LED (seconds)
led_pin     = 12        # Define LED pin as GPIO 12
#######################################################################################

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_pin, GPIO.OUT)    # Define pin 12 as output

# Function to turn on the LED
def LedOn(_pin):
    GPIO.output(_pin, 1)
    return

# Function to turn off the LED
def LedOff(_pin):
    GPIO.output(_pin, 0)
    return

try:
    print("\n\nStarting program...")
    # Loop
    while(1):
        #print("\nTurning ON...")
        LedOn(led_pin)          # Turn on the LED
        time.sleep(blink_time)  # Waits the time
        #print("\nTurning OFF")
        LedOff(led_pin)         # Turn off the LED
        time.sleep(blink_time)  # Waits the time again

except KeyboardInterrupt:
    print("\nKeyboard interrupt!")
    GPIO.cleanup()  # Clear all GPIO setup
    exit()
        
except Exception as e:
    print("\nProgram error!\n\tExceprion=> \"%s\"" % (e))
    GPIO.cleanup()  # Clear all GPIO setup
    exit()

finally:
    GPIO.cleanup()  # Clear all GPIO setup
    exit()
