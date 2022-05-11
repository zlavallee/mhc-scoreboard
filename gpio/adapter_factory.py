from gpio.core import ShiftRegister, StubShiftRegister


def create_output_from_config(config) -> ShiftRegister:
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        return StubShiftRegister()
    else:
        from gpio.gpio_adapter import SN74HC595NOutput

        return SN74HC595NOutput(
            clock_speed=config['clock_speed'],
            serial_data_input=config['serial_data_input'],
            memory_clock=config['memory_clock'],
            serial_clock=config['serial_clock']
        )
