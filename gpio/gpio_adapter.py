import time
import RPi.GPIO as GPIO


def create_output_from_config(config):
    return SN74HC595NOutput(
        clock_speed=config['clock_speed'],
        serial_data_input=config['serial_data_input'],
        memory_clock=config['memory_clock'],
        serial_clock=config['serial_clock']
    )


class SN74HC595NOutput:
    def __init__(self, clock_speed=0.001, serial_data_input=11, memory_clock=12, serial_clock=13):
        self.SDI = serial_data_input
        self.RCLK = memory_clock
        self.SRCLK = serial_clock
        self.clock_speed = clock_speed

        GPIO.setup(self.SDI, GPIO.OUT)
        GPIO.setup(self.RCLK, GPIO.OUT)
        GPIO.setup(self.SRCLK, GPIO.OUT)
        GPIO.output(self.SDI, GPIO.LOW)
        GPIO.output(self.RCLK, GPIO.LOW)
        GPIO.output(self.SRCLK, GPIO.LOW)

    def send_byte(self, data):
        for bit in range(0, 8):
            GPIO.output(self.SDI, 0x80 & (data << bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            self.__tick()
            GPIO.output(self.SRCLK, GPIO.LOW)

    def store_data(self):
        GPIO.output(self.RCLK, GPIO.HIGH)
        self.__tick()
        GPIO.output(self.RCLK, GPIO.LOW)

    def __tick(self):
        time.sleep(self.clock_speed)
