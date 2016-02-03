#!/usr/bin/python
# A simple program to send a number to the Arduinio that controls something
# Written on 1/18/16 by Trevor Gross (t.gross35@gmail.com)

import smbus
import time
import sys
bus = smbus.SMBus(1)

# This is the address we set up in the Arduino program
address = 0x03

# Function to write number to the given address


def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1  # Not sure if this is necessary


def send(trigger):
    val = trigger
    if trigger == 'powerbutton':
        val = 'FF02FD'
    elif trigger == 'red0':
        val = 'FF02FD'
    elif trigger == 'grn0':
        val = 'FF9A65'
    elif trigger == 'blu0':
        val = 'FFA25D'
    elif trigger == 'wht0':
        val = 'FF22DD'
    elif trigger == 'red1':
        val = 'FF2AD5'
    elif trigger == 'green1':
        val = 'FFAA55'
    elif trigger == 'redu':
        val = 'FF28D7'
    elif trigger == 'grnu':
        val = 'FFA857'
    elif trigger == 'bluu':
        val = 'FF6897'
    elif trigger == 'redd':
        val = 'FF08F7'
    elif trigger == 'grnd':
        val = 'FF8877'
    elif trigger == 'blud':
        val = 'FF48B7'

    sendval = int(val, 16)

    if sendval > 230:
        sendvalstr = str(sendval)

        writeNumber(220)

        for i in range(0, len(sendvalstr), 2):
            x = int(sendvalstr[i:i + 2])
            print x
            writeNumber(x)

        writeNumber(221)
    else:
        writeNumber(sendval)


def main():
    send(sys.argv[1])
    print "Sending value"

if __name__ == "__main__":
    main()
