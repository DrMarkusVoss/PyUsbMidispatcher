import time
import rtmidi
from rtmidi.midiutil import list_input_ports, list_output_ports, open_midiinput, open_midioutput

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

    list_input_ports()

    selected_input_port = selectInputPort()

    list_output_ports()

    selected_output_port = selectOutputPort()


    midiout, port_name_out = open_midioutput(selected_output_port)


    midiin, port_name_in = open_midiinput(selected_input_port)

    # also receive and send clock data
    midiin.ignore_types(timing=False)


    print("\nUSB-MIDI Dispatcher is active now!\n\n")
    print("\nPress Control-C to exit.")
    clkcounter = 0
    clktimest1 = 0
    clktimest2 = 0
    calcbpm = 0
    try:
        timer = time()
        while True:
            msg = midiin.get_message()

            if msg:
                message, deltatime = msg
                # print(message)
                timer += deltatime
                if int(message[0]) == 248:
                    clkcounter += 1
                    if clktimest1 == 0:
                        clktimest1 = timer
                    else:
                        delta = timer - clktimest1
                        clktimest1 = 0
                        calcbpm = int(round(60/(delta*24)))

                    if clkcounter == 100:
                        clkcounter = 0
                        print("[%r bpm] - [%s] -> [%s]:  CLOCK TICK" % (calcbpm, port_name_in, port_name_out))
                else:
                    print("[%r bpm] -  [%s] -> [%s]:  %r" % (calcbpm, port_name_in,port_name_out, message))
                    pass
                #midicmd, note, velocity = message

                midiout.send_message(message)
                #midiout2.send_message(message)

            # time.sleep(0.01)
    except KeyboardInterrupt:
        print('')
    finally:
        print("Exit.")
        midiin.close_port()
        midiout.close_port()
        del midiin
        del midiout


def selectInputPort():
    portnrstr = input("Select the input port by typing the corresponding number: ")
    selected_input_port = int(portnrstr)

    return selected_input_port


def selectOutputPort():
    portnrstr = input("Select the output port by typing the corresponding number: ")
    selected_output_port = int(portnrstr)

    return selected_output_port


if __name__ == '__main__':
    dispatcherMainLoop()

