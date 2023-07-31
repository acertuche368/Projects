import machine
import time
Charger_relay = machine.Pin(0, machine.Pin.OUT)
# Function to convert ADC value to voltage
def adc_to_voltage(adc_value, max_adc_value, voltage_range):
    return adc_value / max_adc_value * voltage_range
Charger_relay.value(0)
# Main loop to read battery voltage
while True:
    adc = machine.ADC(26)  # Replace 26 with the GPIO pin number you connected the battery to
    adc_value = adc.read_u16()

    # Assuming voltage divider resistor values (R1 and R2) are properly chosen to scale down the voltage
    battery_voltage = (adc_to_voltage(adc_value, 65535, 3.3))  # 3.3V is the ADC input range

    print(f"Battery Voltage: {battery_voltage:.2f} V")
    
    time.sleep(5)  # Adjust the interval between readings as needed
    if battery_voltage <= 2.6:
        Charger_relay.value(1)
        print("Charger is now on")
    elif battery_voltage >=3.3:
        Charger_relay.value(0)
        print("Charger is off")