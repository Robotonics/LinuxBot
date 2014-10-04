#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmp085.py
#  
#  Copyright 2013 Stefan Mavrodiev <support@olimex.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.eld    updated: Updated

import sys
import select
import os
import smbus
import math
import time

from optparse import OptionParser
from optparse import OptionGroup


#define class for printing colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
class Registers:
    Configuration_Register_A = 0x00
    Configuration_Register_B = 0x01
    Configuration_Mode = 0x02
    Data_Output_X_MSB_Register = 0x03
    Data_Output_X_LSB_Register = 0x04
    Data_Output_Z_MSB_Register = 0x05
    Data_Output_Z_LSB_Register = 0x06
    Data_Output_Y_MSB_Register = 0x07
    Data_Output_Y_LSB_Register = 0x08
    Status_Register = 0x09
    Identification_Register_A = 0x0A
    Identification_Register_B = 0x0B
    Identification_Register_C = 0x0C

class HMC5883: 
        
    @staticmethod
    def measurement_modes(x):
        return {
            'normal': 0x00,
            'positive': 0x01,
            'negative': 0x02
        }[x]
    
    @staticmethod
    def operating_modes(x):
        return {
            'continuous' : 0x00,
            'single' : 0x01,
            'idle' : 0x02
        }[x]
        
    @staticmethod
    def output_rate(x):
        return {
            '0.75'  : 0x00,
            '1.5'   : 0x01,
            '3'     : 0x02,
            '7.5'   : 0x03,
            '15'    : 0x04,
            '30'    : 0x05,
            '75'    : 0x06
        }[x]
        
    __scale = {
        0   :   0.73,
        1   :   0.92,
        2   :   1.22,
        3   :   1.52,
        4   :   2.27,
        5   :   2.56,
        6   :   3.03,
        7   :   4.35
    }
        
    def __init__(self, options):
        #Parse options
        self.verbose = options.verbose
        self.i2c = options.i2c
        self.address = options.address
        self.do = HMC5883.output_rate(options.do)
        self.ma = options.ma
        self.hs = options.hs
        self.gn = options.gn
        self.ms = HMC5883.measurement_modes(options.ms)
        self.md = HMC5883.operating_modes(options.md)
        self.declination = (options.dec[0] + float(options.dec[1])/60)*math.pi/180
    
    def twosComplement(self, val, len):
        if (val & (1 << len - 1)):
            val = val - (1 << len)
        return val
    
    def selfTest(self):
        print(colors.BOLD + "MOD-HMC5883L Self-Test: " + colors.ENDC),
        try:
            # Open I2C-BUS
            if self.verbose:
                print
                print("Opening i2c-bus: "),
            bus = smbus.SMBus(self.i2c)
            if self.verbose:
                print(colors.OKGREEN + "OK" + colors.ENDC)
            
            # Read chip ID    
            if self.verbose:
                print("Reading chip-ID:"),
            ID = bus.read_i2c_block_data(self.address, Registers.Identification_Register_A, 3)
            if self.verbose:
                print(colors.OKGREEN + "OK" + colors.ENDC)
                
            # Check chip ID
            if self.verbose:
                print("Check chip-ID A[0x48]:"),
            if ID[0] == 0x48:
                if self.verbose:
                    print(colors.OKGREEN + "OK" + colors.ENDC)
            else:
                raise Exception("Chip-ID doesn't match!")
                
            if self.verbose:
                print("Check chip-ID B[0x34]:"),
            if ID[1] == 0x34:
                if self.verbose:
                    print(colors.OKGREEN + "OK" + colors.ENDC)
            else:
                raise Exception("Chip-ID doesn't match!")
            
            if self.verbose:
                print("Check chip-ID C[0x33]:"),
            if ID[2] == 0x33:
                if self.verbose:
                    print(colors.OKGREEN + "OK" + colors.ENDC)
            else:
                raise Exception("Chip-ID doesn't match!")
                
            #Sending configuration
            gain = 0x05
            while True:
                #1
                if self.verbose:
                    print("Sending configuration:"),
                bus.write_i2c_block_data(self.address, Registers.Configuration_Register_A, [0x71])
                #2
                bus.write_i2c_block_data(self.address, Registers.Configuration_Register_B, [gain << 5])
                #3
                bus.write_i2c_block_data(self.address, Registers.Configuration_Mode, [0x00])
                if self.verbose:
                    print(colors.OKGREEN + "OK" + colors.ENDC)
                #4
                if self.verbose:
                    print("Waiting for data...")
                #Ignore first recieved data
                while True:
                    if bus.read_i2c_block_data(self.address, Registers.Status_Register, 1)[0] & 0x01:
                        break
                bus.read_i2c_block_data(self.address, Registers.Data_Output_X_MSB_Register, 6)
                while True:
                    if bus.read_i2c_block_data(self.address, Registers.Status_Register, 1)[0] & 0x01:
                        break
                #5
                a = bus.read_i2c_block_data(self.address, Registers.Data_Output_X_MSB_Register, 6)
                x = a[0] << 8 | a[1]
                z = a[2] << 8 | a[3]
                y = a[4] << 8 | a[5]
                if self.verbose:
                    print("Checking limits:"),
                if  x > 243 and x < 575 and z > 243 and z < 575 and y > 243 and y < 575:
                    #Test pass
                    print(colors.OKGREEN + "OK" + colors.ENDC)
                    break
                else:
                    if gain < 7:
                        #Inclease gain
                        gain += 1
                        if self.verbose:
                            print(colors.WARNING + "Values outside limits! Increasing gain..." + colors.ENDC)
                    else:
                        bus.write_i2c_block_data(self.address, Registers.Configuration_Register_A, [0x70])
                        #Test fail
                        print(colors.FAIL + "FAIL" + colors.ENDC)
                        sys.exit(2)
           
            
        except Exception, e:
            print(colors.FAIL + "FAIL" + colors.ENDC)
            print(str(e))
            print
        sys.exit(0)
        return

    def getMeasurements(self):
        #print(colors.BOLD + "MOD-HMC5883L Measurements:" + colors.ENDC),
        #open bus
        if self.verbose:
            print
            print("Opening i2c bus: "),
        bus = smbus.SMBus(self.i2c)
        if self.verbose:
            print(colors.OKGREEN + "OK" + colors.ENDC)
        
        #send configuration
        if self.verbose:
            print("Setting configuration: "),
        bus.write_i2c_block_data(self.address, Registers.Configuration_Register_A, [self.ma << 5 | self.do << 2| self.ms])
        bus.write_i2c_block_data(self.address, Registers.Configuration_Register_B, [self.gn << 5])
        bus.write_i2c_block_data(self.address, Registers.Configuration_Mode, [self.hs << 7 | self.md])
        if self.verbose:
            print(colors.OKGREEN + "OK" + colors.ENDC)
        
        if self.verbose:
            print("Reading data")
        
        #if single
        if self.md == 0x01:
            for i in range(0, 2):
                #Wait for data to become ready
                while True:
                    if bus.read_i2c_block_data(self.address, Registers.Status_Register, 1)[0] & 0x01:
                        break
                #Do dummy read
                data = bus.read_i2c_block_data(self.address, Registers.Data_Output_X_MSB_Register, 6)
            
            x = self.twosComplement(data[0] << 8 | data[1], 16)
            z = self.twosComplement(data[2] << 8 | data[3], 16)
            y = self.twosComplement(data[4] << 8 | data[5], 16)
   
            
            x *= self.__scale[self.gn]
            z *= self.__scale[self.gn]
            y *= self.__scale[self.gn]
            
            heading = math.atan2(y, x)
            heading+= self.declination
            
            if heading < 0:
                heading += 2 * math.pi
            elif heading > 2 * math.pi:
                heading -= 2 * math.pi
                
            heading = heading * 180 / math.pi
            #print str(heading)
	    heading=round(heading,0)
	    print heading
            
            sys.exit(0)
            
        elif self.md == 0x00:
            
                
            while True:
                
                #Wait for data to become ready
                while True:
                    if bus.read_i2c_block_data(self.address, Registers.Status_Register, 1)[0] & 0x01:
                        break
                #Do dummy read
                data = bus.read_i2c_block_data(self.address, Registers.Data_Output_X_MSB_Register, 6)
                
                x = self.twosComplement(data[0] << 8 | data[1], 16)
                z = self.twosComplement(data[2] << 8 | data[3], 16)
                y = self.twosComplement(data[4] << 8 | data[5], 16)

                
                x *= self.__scale[self.gn]
                z *= self.__scale[self.gn]
                y *= self.__scale[self.gn]
                
                heading = math.atan2(y, x)
                heading+= self.declination
                
                if heading < 0:
                    heading += 2 * math.pi
                elif heading > 2 * math.pi:
                    heading -= 2 * math.pi
                    
                heading = heading * 180 / math.pi
                print "Heading: " + str(heading)
                
                time.sleep(0.5)              
        
        
        return
__all__ = []
__version__ = 0.1
__date__ = '2014-01-03'
__updated__ = '2014-01-03'


def main(argv=None):
    
    
    '''Command line options.'''    
    
    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    program_longdesc = 'HMC5883L is 3-Axis Digital Compass with 12-bit ADC that enables \
1deg to 2deg compass heading accuracy. HMC5883L is with I2C interface and can connect to any board with UEXT'
    program_license = "Copyright 2014 Stefan Mavrodiev (Olimex LTD)"

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
        parser.add_option("-i", "--i2c", type="int", dest="i2c", help="set i2c bus [default: %default]", metavar="I2C")
        parser.add_option("-a", "--address", type="int", dest="address", help="set device address [default %default]", metavar="ADDR")
        parser.add_option("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %default]")
        
        group = OptionGroup(parser, "HMC5883L options")
        group.add_option(
            "--ma",
            type="int",
            dest="ma",
            help="Select number of samples avaraged (1,2,4 or 8) per measurement output. [default: %default]")
        group.add_option(
            "--do",
            dest="do",
            type="choice",
            choices=['0.75', '1.5', '3', '7.5', '15', '30', '75'], 
            help="Data Output Rate Bits. These bits set the rate at which data is written to all three data output registers. [default: %default]. Valid values: 0.75, 1.5, 3, 7.5, 15, 30, 75.")
        group.add_option(
            "--ms",
            dest="ms",
            type="choice",
            choices=['normal', 'positive', 'negative'],
            help="Measurement Configuration Bits. These bits define the measurement flow of the device, specifically whether or not to incorporate an applied bias into the measurement. [default: %default]. Valid values: normal, positive, negative.")
        group.add_option(
            "--gn",
            type="int",
            dest="gn",
            help="Gain Configuration Bits. These bits configure the gain for the device. The gain configuration is common for all channels. [default: %default]. Valid values: 0 to 7.")
        group.add_option(
            "--hs",
            action="store_true",
            dest="hs",
            help="Set this pin to enable High Speed I2C, 3400kHz. [default: %default]")
        group.add_option(
            "--md",
            type="choice",
            choices=['single', 'continuous', 'idle'],
            dest="md",
            help="Mode Select Bits. These bits select the operation mode of this device. [default: %default]. Valid values: continuous, single, idle")
        
        parser.add_option_group(group)
        
        group = OptionGroup(parser, "HMC5883L actions")
        group.add_option("--selftest", action="store_true", dest="selftest", help="Run self test test operation")
        group.add_option("--declination", type="int", dest="dec", nargs=2, help="Declination. [default %default]. Format is \"degrees\" \"minutes\".", metavar="[DEG, MIN]")

        parser.add_option_group(group)
        
        # set defaults
        parser.set_defaults(i2c=1, address=0x1E, md="single", ma=1, do='15', ms="normal", gn=1, hs=False, dec=[0,0] )

        # process options
        (opts, args) = parser.parse_args(argv)
        
        # check parameters
        if opts.ma not in [1, 2, 4, 8]:
            raise Exception("ma: The selected value is not valid!")
            
        if opts.gn not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise Exception("gn: Invalid value!")
            
            
        
        # MAIN BODY #
        
        #Create class object
        obj = HMC5883(opts)
        
        if opts.selftest:
            obj.selfTest()
        else:
            obj.getMeasurements()
        

    except Exception, e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + str(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        print
        return 2


if __name__ == "__main__":
    sys.exit(main())
