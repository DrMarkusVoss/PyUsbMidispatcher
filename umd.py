import time
import rtmidi
from rtmidi.midiutil import list_input_ports, list_output_ports, open_midiinput, open_midioutput
import tkinter as tk

from PyMidiDispatcherGui import *


dconfig = {
    "NoteFwd": True,
    "ClockFwd": True,
    "ClockGen": False,
    "ClockSrc": "RD-9",
    "ClockTargets": ["Cobalt8"],
    "MIDISrc1": "Cobalt8",
    "NoteFwd1": True,
    "CCFwd1": True,
    "NoteTargets1": [[[62,69], "Wavestate_in1"]],
    "MIDISrc2": "ProKeys",
    "NoteFwd2": True,
    "CCFwd2": False,
    "NoteTargets2": [[[62, 69], "virtual_opsix_in"], [[70, 78], "virtual_wavestatenative_in"]]
}

virtual = False

def dispatcherMainLoop():

    if virtual:
        midiout = rtmidi.MidiOut()
        midiout.open_virtual_port("MultiMidiSequencer")


    # also receive and send clock data
    #midiin.ignore_types(timing=False)

    midi_in_ports = rtmidi.MidiIn()
    midi_ins = midi_in_ports.get_ports()

    midi_out_ports = rtmidi.MidiOut()
    midi_outs = midi_out_ports.get_ports()

    root = tk.Tk()
    app = PyMidiDispatcherGui(root, midi_ins, midi_outs)

    root.mainloop()




if __name__ == '__main__':
    dispatcherMainLoop()

