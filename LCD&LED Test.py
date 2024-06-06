# Import all necessary libraries

from pico_i2c_lcd import I2cLcd #Import the i2clcd module from the pico_i2c_lcd library to control the i2c LCD display
from machine import I2C #Import I2C module from machine library to control yhe  I2C communication protocol
from machine import Pin # Import pin module from machine library to control the pins on the raspberry bi
import utime # Import utime to control the working time or timers in the program

# Create an object for the LCD
i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)

# Create the Lcd address
lcd = I2CLcd(i2c,0x027, 2, 16)

# Instruction to display information on the LCD
led.putstr("Hello Algo Peer!")
led.putstr("Code Solve Loop")

led = Pin(5, Pin.OUT) # Condigure/set the pin 5 as output

# Turn on Led
led.value(1)

# Wait for a few seconds
utime.sleep(5)

# Turn the Led off
led.value(0)