import pyvisa


class KeysightB2912a(object):
    """Python class for Keithley 2912 Sourcemeter, written by Francesca Incalza and Matteo Castellani :)"""

    def __init__(self, visa_name):
        rm = pyvisa.ResourceManager()
        self.pyvisa = rm.open_resource(visa_name)
        self.pyvisa.timeout = 5000  # Set response timeout (in milliseconds)
        # self.pyvisa.query_delay = 1 # Set extra delay time between write and read commands

    def read(self):
        return self.pyvisa.read()

    def write(self, string):
        self.pyvisa.write(string)

    def query(self, string):
        return self.pyvisa.query(string)

    def reset(self):
        self.write("*RST")

    def local_key(self):
        self.write("SYST:KEY 23")

    def setup_read_volt(self):
        self.write("*RST")
        self.write(":SOUR:FUNC:MODE CURR")
        self.write(":SOUR:CURR:LEVEL 0E-6")
        self.write('SENS:FUNC "VOLT"')

    def setup_4W_source_I_read_V(self, current="1000"):
        """current level in microamps"""
        self.write("*RST")
        self.write(":SOUR:FUNC:MODE CURR")  # Set operation mode to: source current
        print(":SOUR:CURR:LEVEL " + current + "E-6")
        self.write(":SOUR:CURR:LEVEL " + current + "E-6")
        self.write(
            ":SENS:REM 1"
        )  # Turn on "Remote Sensing" aka 4-wire measurement mode
        self.write('SENS:FUNC "VOLT", "CURR"')  # Have it output

    def setup_2W_source_I_read_V(self):
        self.write("*RST")
        self.write(":SOUR1:FUNC:MODE CURR")  # Set operation mode to: source current
        self.write(":SOUR1:CURR:LEVEL 0E-6")  # Set current level to 0 uA
        self.write(
            ":SENS:REM 0"
        )  # Turn off "Remote Sensing" aka 4-wire measurement mode
        self.write('SENS:FUNC "VOLT", "CURR"')  # Have it output

    def setup_2W_source_V_read_I(self):
        self.write("*RST")
        self.write(":SOUR:FUNC:MODE VOLT")  # Set operation mode to: source voltage
        self.write(":SOUR:VOLT:LEVEL 0E-3")  # Set voltage level to 0 mV
        self.write(
            ":SYST:RSEN 0"
        )  # Turn off "Remote Sensing" aka 4-wire measurement mode
        self.write('SENS:FUNC "VOLT", "CURR"')  # Have it output

    def user_settings(self):
        self.write("*RST")
        self.write(":SOUR1:FUNC:MODE CURR")  # Set operation mode to: source current
        self.write(":SOUR:CURR:RANG 100e-9")

    def set_output(self, output=False):
        if output is True:
            self.write(":OUTP ON")
        if output is False:
            self.write(":OUTP OFF")

    def set_measurement_time(self, plc_cycles=1.0):
        """plc_cycles Sets integration time Keithley.  Each cycle corresponds to
        1/60th of a second.  Default is 1.0, Max is 10.0. Min is 0.01.  See Keithley
        manual p18-70 for more details"""
        self.write(":NPLCycles %0.2f" % plc_cycles)

    def disable_remote(self):
        """Simulates the pressing of the "LOCAL" button on the Keithley
        which will take the keithley out of remote mode"""
        self.write(":SYST:KEY 23")

    def set_compliance_i(self, compliance_i=10e-6):
        self.write(":SENS:CURR:PROT %0.3e" % compliance_i)

    def set_compliance_v(self, compliance_v=10e-6):
        self.write(":SENS:VOLT:PROT %0.3e" % compliance_v)

    def set_current(self, current=0e-6):
        self.write(":SOUR:CURR:LEVEL %0.4e" % current)  # Set current level

    def set_voltage(self, voltage=0e-6):
        self.write(":SOUR:VOLT:LEVEL %0.4e" % voltage)  # Set current level

    def read_voltage_and_current(self):
        read_str = self.query(":READ?")
        # See page 18-51 of manual, returns: voltage, current, resistance, timestamp, status info
        # Returns something like '5.275894E-05,-1.508318E-06,+9.910000E+37,+2.562604E+03,+3.994000E+04'
        data = read_str.split(",")
        # print(data)
        voltage = float(data[0])
        # print(voltage)
        # current = float(data[1])
        current = float(data[1])
        return voltage, current

    def read_current(self, current=0e-6):
        voltage, current = self.read_voltage_and_current()
        return current

    def read_voltage(self):
        voltage, current = self.read_voltage_and_current()
        return voltage

    def read_resistance(self):
        voltage, current = self.read_voltage_and_current()
        return voltage

    def switch_front(self):
        self.write(":ROUT:TERM FRON")

    def switch_rear(self):
        self.write(":ROUT:TERM REAR")
