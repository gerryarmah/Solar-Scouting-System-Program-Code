from machine import ADC, Pin
import utime

# Initialize the ADC on GP26 (ADC0)
adc = ADC(Pin(26))

# Conversion factor for ADC value to voltage (3.3V reference and 12-bit resolution)
conversion_factor = 3.3 / (65535)

# Function to read and convert ADC value to wind speed
def read_wind_speed():
    # Read the raw ADC value
    adc_value = adc.read_u16()
    # Convert the ADC value to voltage
    voltage = adc_value * conversion_factor
    # Print the ADC value and corresponding voltage for debugging
    print("ADC Value:", adc_value)
    print("Voltage:", voltage, "V")
    # Estimate the wind speed from the voltage (this requires calibration specific to your anemometer)
    # For simplicity, we assume a linear relationship for this example (modify as needed)
    wind_speed = voltage * 10  # Example: 10 m/s per Volt (modify based on calibration)
    return wind_speed

# Main loop to read and print the wind speed
while True:
    wind_speed = read_wind_speed()
    print("Estimated Wind Speed:", wind_speed, "m/s")
    utime.sleep(1)  # Wait for 1 second before the next reading
