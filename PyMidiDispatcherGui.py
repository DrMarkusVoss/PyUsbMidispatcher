import tkinter as tk
import tkinter.font as tkFont


class PyMidiDispatcherGui:
    def __init__(self, root, midi_ins, midi_outs):
        self.root = root
        self.midi_ins = midi_ins
        self.midi_outs = midi_outs
        #setting title
        root.title("UMD - USB MIDI Dispatcher")
        self.frame= tk.Frame(root)
        self.frame.pack(side=tk.BOTTOM)


        but_Play=tk.Button(self.frame)
        but_Play["bg"] = "#c0c0c0"
        but_Play["fg"] = "#000000"
        but_Play["justify"] = "center"
        but_Play["text"] = "Play"
        but_Play.place(x=200,y=260,width=70,height=25)
        but_Play["command"] = self.but_Play_cmd
        but_Play.pack(side=tk.BOTTOM)

        value_inside_midi_clkmaster = tk.StringVar()

        # Set the default value of the variable
        value_inside_midi_clkmaster.set("Select MIDI Clock Master")
        lab_midi_clkmaster_strvar = tk.StringVar()
        lab_midi_clkmaster_strvar.set("MIDI Clock Master: ")
        lab_midi_clkmaster = tk.Label(self.frame, textvariable=lab_midi_clkmaster_strvar)
        lab_midi_clkmaster.pack(side=tk.LEFT)

        self.om_midi_clkmaster = tk.OptionMenu(self.frame, value_inside_midi_clkmaster, *self.midi_ins)
        self.om_midi_clkmaster["borderwidth"] = "1px"
        self.om_midi_clkmaster["fg"] = "#333333"
        self.om_midi_clkmaster["justify"] = "left"
        self.om_midi_clkmaster.place(x=190, y=110, width=200, height=25)
        self.om_midi_clkmaster.pack(side=tk.LEFT)


        # Set the default value of the variable
        value_inside_midi_in = tk.StringVar()
        value_inside_midi_in.set("Select a MIDI input port")
        lab_midi_in_strvar = tk.StringVar()
        lab_midi_in_strvar.set("Midi Input: ")
        lab_midi_in = tk.Label(self.frame, textvariable=lab_midi_in_strvar)
        lab_midi_in.pack(side=tk.LEFT)

        self.om_midi_clkmaster = tk.OptionMenu(self.frame, value_inside_midi_in, *self.midi_ins)
        self.om_midi_clkmaster["borderwidth"] = "1px"
        self.om_midi_clkmaster["fg"] = "#333333"
        self.om_midi_clkmaster["justify"] = "left"
        self.om_midi_clkmaster.place(x=190, y=110, width=200, height=25)
        self.om_midi_clkmaster.pack(side=tk.LEFT)



    def setMidiInputs(self, midi_input_list):
        self.midi_ins = midi_input_list
        self.om_midi_clkmaster.pack()






    def but_Play_cmd(self):
        print("command")
