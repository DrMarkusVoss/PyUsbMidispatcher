import tkinter as tk
import tkinter.font as tkFont
from threading import Thread
from time import sleep
from time import time
from MidiDispatchConfig import *
from rtmidi.midiutil import list_input_ports, list_output_ports, open_midiinput, open_midioutput

threadrunflag = True

class PyMidiDispatcherGui:
    def __init__(self, root, midi_ins, midi_outs):
        self.root = root
        self.midi_ins = midi_ins
        self.midi_outs = midi_outs
        #setting title
        root.title("UMD - USB MIDI Dispatcher")
        self.frame= tk.Frame(root)
        self.frame.pack(side=tk.BOTTOM)
        self.isplaying = True
        self.playThread = None
        self.midi_cfg = MidiDispatchConfig(midi_ins, midi_outs)

        but_Play=tk.Button(self.frame)

        #but_Play["justify"] = "right"
        but_Play["text"] = "Play"
        but_Play.place(x=200,y=260,width=70,height=25)
        but_Play["command"] = self.but_Play_cmd
        but_Play.pack(side=tk.BOTTOM)

        but_Stop=tk.Button(self.frame)

        #but_Play["justify"] = "right"
        but_Stop["text"] = "Stop"
        but_Stop.place(x=200,y=260,width=70,height=25)
        but_Stop["command"] = self.but_Stop_cmd
        but_Stop.pack(side=tk.BOTTOM)

        self.value_inside_midi_clkmaster = tk.StringVar()

        # Set the default value of the variable
        self.value_inside_midi_clkmaster.set("Select MIDI Clock Master")
        lab_midi_clkmaster_strvar = tk.StringVar()
        lab_midi_clkmaster_strvar.set("MIDI Clock Master: ")
        lab_midi_clkmaster = tk.Label(self.frame, textvariable=lab_midi_clkmaster_strvar)
        lab_midi_clkmaster.pack(side=tk.LEFT)

        self.om_midi_clkmaster = tk.OptionMenu(self.frame, self.value_inside_midi_clkmaster, *self.midi_ins, command=self.setClkMaster)
        #self.om_midi_clkmaster["justify"] = "left"
        self.om_midi_clkmaster.place(x=190, y=110, width=200, height=25)
        self.om_midi_clkmaster.pack(side=tk.LEFT)


        # Set the default value of the variable
        self.value_inside_midi_in = tk.StringVar()
        self.value_inside_midi_in.set("Select a MIDI input port")
        lab_midi_in_strvar = tk.StringVar()
        lab_midi_in_strvar.set("Midi Input/Source: ")
        lab_midi_in = tk.Label(self.frame, textvariable=lab_midi_in_strvar)
        lab_midi_in.pack(side=tk.LEFT)

        self.om_midi_in = tk.OptionMenu(self.frame, self.value_inside_midi_in, *self.midi_ins, command=self.setGblMidiIn)
        #self.om_midi_in["justify"] = "left"
        self.om_midi_in.place(x=190, y=110, width=200, height=25)
        self.om_midi_in.pack(side=tk.LEFT)

        # Set the default value of the variable
        self.value_inside_midi_out = tk.StringVar()
        self.value_inside_midi_out.set("Select a MIDI output port")
        lab_midi_out_strvar = tk.StringVar()
        lab_midi_out_strvar.set("Midi Output/Target: ")
        lab_midi_out = tk.Label(self.frame, textvariable=lab_midi_out_strvar)
        lab_midi_out.pack(side=tk.LEFT)

        self.om_midi_out = tk.OptionMenu(self.frame, self.value_inside_midi_out, *self.midi_outs, command=self.setGblMidiOut)
        # self.om_midi_out["justify"] = "left"
        self.om_midi_out.place(x=190, y=110, width=200, height=25)
        self.om_midi_out.pack(side=tk.LEFT)

    def setMidiInputs(self, midi_input_list):
        self.midi_ins = midi_input_list
        self.om_midi_clkmaster.pack()

    def setGblMidiIn(self, nr):
        self.midi_cfg.setGblMidiSource(self.value_inside_midi_in.get())

    def setGblMidiOut(self, nr):
        self.midi_cfg.setGblMidiTarget(self.value_inside_midi_out.get())

    def setClkMaster(self, nr):
        self.midi_cfg.setClkMaster(self.value_inside_midi_clkmaster.get())

    def but_Play_cmd(self):
        global threadrunflag
        print("UMD - MIDI Dispatching Loop started... ")
        threadrunflag = True
        self.playThread = Thread(target=self.playLoop, args=[self.midi_cfg], daemon=True)
        self.playThread.start()

    def but_Stop_cmd(self):
        global threadrunflag
        threadrunflag = False
        self.playThread = None

    def playLoop(self, runflag):
        global threadrunflag

        midiout, port_name_out = self.midi_cfg.getGblMidiTarget()

        midiin, port_name_in = self.midi_cfg.getGblMidiSource()

        clkmaster, port_name_clkmaster = self.midi_cfg.getClkMaster()

        # also receive and send clock data
        clkmaster.ignore_types(timing=False)

        clkcounter = 0
        clktimest1 = 0
        calcbpm = 0

        try:
            timer = time()
            clktimer = time()
            while threadrunflag:
                msg = midiin.get_message()
                clkmsg = clkmaster.get_message()

                if clkmsg:
                    clkmessage, clkdeltatime = clkmsg
                    clktimer += clkdeltatime
                    if int(clkmessage[0]) == 248:
                        midiout.send_message(clkmessage)
                        clkcounter += 1
                        if clktimest1 == 0:
                            clktimest1 = clktimer
                        else:
                            clkdelta = clktimer - clktimest1
                            clktimest1 = 0
                            calcbpm = int(round(60 / (clkdelta * 24)))

                        if clkcounter == 100:
                            clkcounter = 0
                            print("[%r bpm] - [%s] -> [%s]:  CLOCK TICK" % (calcbpm, port_name_clkmaster, port_name_out))
                if msg:
                    message, deltatime = msg
                    # print(message)
                    timer += deltatime
                    print("[%s] -> [%s]:  %r" % (port_name_in, port_name_out, message))
                    midiout.send_message(message)

        except KeyboardInterrupt:
            print('')
        finally:
            print("UMD - MIDI Dispatching Loop stopped... ")
            midiin.close_port()
            midiout.close_port()
            del midiin
            del midiout


