# PyUsbMidispatcher
A python implemented USB-MIDI dispatcher.

First you can select the Midi Input Device from a list of all devices available. Then you select the Midi Output Device
from a list of all available devices.  Then the dispatching starts. 

Typically, your input device is your master keyboard that is connected via USB-MIDI to your computer. 
Your output device is your computer/DAW/audio interface or maybe
another synthesizer that is also connected via USB-MIDI to your computer. Then the dispatcher will receive the MIDI
data from the input device and forward it to the selected output device (without any other setup or configuration
necessary).

## System Requirements
- tested on MacOS Monterey (12.4) with Python 3.8
- uses the python-rtmidi package (install with pip3)
- all MIDI devices must support MIDI via USB and must be connected via USB to the computer
