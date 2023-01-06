import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT) # Channel 1
GPIO.setup(16, GPIO.OUT) # Channel 2

GPIO.setup(18, GPIO.IN)

def signal_received(pin):

    # Check the RF signal and turn relay on or off
    if GPIO.input(pin) == 1:
        # RF signal received, turn relay on
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
    else:
        # No RF signal received, turn relay off
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)

# Event detection for the RF receiver pin
GPIO.add_event_detect(18, GPIO.BOTH, callback=signal_received)

# Wait for RF signals
while True:
    time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
