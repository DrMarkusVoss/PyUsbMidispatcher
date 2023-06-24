# PyUsbMidispatcher
A python implemented USB-MIDI dispatcher.

First you can select the Midi Input Device from a list of all devices available. Then you select the Midi Output Device
from a list of all available devices.  Then the dispatching starts. 

Typically, your input device is your master keyboard that is connected via USB-MIDI to your computer. 
Your output device is your computer/DAW/audio interface or maybe
another synthesizer that is also connected via USB-MIDI to your computer. Then the dispatcher will receive the MIDI
data from the input device and forward it to the selected output device (without any other setup or configuration
necessary).

# Usage
## First simple version
The first simple version lets you define a MIDI input as source (e.g. a MIDI Master Keyboard) and a MIDI output as target
to receive the MIDI commands and values (e.g. a Synthesizer Module) and then all MIDI Data coming in via MIDI over USB 
from the source will be routed to the target. You still have to make sure that the MIDI channels of source and target
are configured on the devices themselves in a way that they can interact.

Call example:
```
python3 pyumidispatcher_simple.py 
```

On your computer you will see each command that gets forwarded. Example:
```
[0 bpm] -  [MPK Mini Mk II] -> [JUPITER-X]:  [144, 65, 61]
[0 bpm] -  [MPK Mini Mk II] -> [JUPITER-X]:  [128, 65, 0]
[0 bpm] -  [MPK Mini Mk II] -> [JUPITER-X]:  [144, 65, 65]
[0 bpm] -  [MPK Mini Mk II] -> [JUPITER-X]:  [128, 65, 0]

```

When your source is a device with MIDI clock information (e.g. a Synthesizer or Sequencer), then also the MIDI clock
is transferred from source to target and the BPM value can also be seen on your computers output. Otherwise, in case
no MIDI clock information is tranferred, you will see "0 bpm".

## UMD - complex MIDI routing with a GUI
The target is to develop a configurable MIDI routing and dispatching software, that will allow some cool use cases:
- split the zones of a "dumb" MIDI USB Keyboard on dispatch the data from the different zones to different targets
- define one device a clock master and send the clock data to all other devices in your defined setup
- define one or several sources for MIDI NoteOn/NoteOff information with several flexible targets

This program is still in build up and will take some time, and first will get a maybe ugly Tkinter GUI.

It can be called like this:
```
python3 umd.py
```
Then a Tkinter GUI will appear that currently covering the functionality of the "simple" command line version.


## System Requirements
- tested on MacOS Monterey (12.4) with Python 3.8
- uses the python-rtmidi package (install with pip3)
- all MIDI devices must support MIDI via USB and must be connected via USB to the computer
