# Import all the necessary libraries

from machine import Pin, I2C, ADC #Import Pin module to control the pins on the raspberry pi pico w,
                                  #I2C to control the communication protocol
                                  #Import ADC(Analog to digital converter to control the signal coming from the solar panel
 
 
import utime # Import time module to control the time in the program
import lcd_api # Import module to control the LCD
from pico_i2c_lcd import i2cLcd # Import module to control the LCD

#Set up the I2C for the LCD screen
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

#Create an address for the LCD
lcd = I2cLcd(i2c, 0x27, 2, 16)

#Set up the ADC pin on pin26
adc = ADC(Pin(26))


vref = 3.3 # The maximum voltage the ADC pin can read
adc_resolution = 65535 # The range of values/different levels the ADC pin can read or output

# List to store the timestamp and voltage data or reading
timestamps = []
voltage = []


#Function to calculate voltage
def calculate_voltage():
    raw_value = adc.read_u16() # Get raw value from the ADC (a number between 0 and 65,535)
    voltage = (raw_value / adc_resolution)* vref # Convert raw_value to voltage(a number between 0 and 3.3)
    return volage

def append_data_to_file(timestamp_str,voltage):
    try:
        with open("voltage_data.csv", "a") as data_file:  # Open the file in append mode
            data_file.write("(). {:.2f}\n".format(timestamp_str, voltage))
    except Exception as e:
        print("Error writing to file:" e)

def main():
  with open("voltage_data.csv", "w")as data_file:
        data_file.write("Timestamp, Voltage \n")
    
  while True:
        voltage = calculate_voltage() #Store the calculated voltage from solar panel
        
        lcd.clear() #Clear the LCD screen
        
        lcd.putstr("Voltage:{:2f}V".format(voltage)) # Show the voltage on the LCD screen
        
        
        #Get the current timestamp
        timestamp = utime.localtime()
        timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(timestamp[0],timestamp[1],timestamp[2],
                                                                           timestamp[3],timestamp[4],timestamp[5])
        
        print("Timestamp: {}, Voltage: {:.2f)V".format(timestamp_str, voltage))

        append_data_to_file(timestamp_str, voltage)
        
        #Wait for the 1 second before reading the voltage
        utime.sleep(1)
        
        led = Pin(5, Pin.OUT)
        
        #Turn on the LED
        led.value(1)
        
        utime.sleep(1)
        
        #Turn off the LED
        led.value(0)
        
        utime.sleep(1)
    
try:
    main()
except KeyboardInterrupt:
    print("Program Interrupted")

try:
    with open("Voltage_data.csv","r") as data_file:
        pass
except OSError:
    with open("Voltage_data.csv", "w") as data_file:
        data_file.write("Timestamp, Volatge\n")
    
    
