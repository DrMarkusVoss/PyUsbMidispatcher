import time
import rtmidi
from rtmidi.midiutil import list_input_ports, list_output_ports, open_midiinput, open_midioutput


def dispatcherMainLoop():

    list_input_ports()

    selected_input_port = selectInputPort()

    list_output_ports()

    selected_output_port = selectOutputPort()

    midiout, port_name_out = open_midioutput(selected_output_port)

    midiin, port_name_in = open_midiinput(selected_input_port)

    print("\nUSB-MIDI Dispatcher is active now!\n\n")
    print("\nPress Control-C to exit.")
    try:
        timer = time.time()
        while True:
            msg = midiin.get_message()

            if msg:
                message, deltatime = msg
                timer += deltatime
                print("[%s] -> [%s]:  %r" % (port_name_in,port_name_out, message))
                midicmd, note, velocity = message

                midiout.send_message(message)

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

