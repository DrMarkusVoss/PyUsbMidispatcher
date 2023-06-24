from rtmidi.midiutil import list_input_ports, list_output_ports, open_midiinput, open_midioutput

class MidiDispatchConfig:
    def __init__(self, midi_ins, midi_outs):
        self.midi_ins = midi_ins
        self.midi_outs = midi_outs
        self.clk_master = 0
        self.gbl_midi_source = 0
        self.gbl_midi_target = 0

    def setClkMaster(self, clk_master):
        self.clk_master = self.midi_ins.index(clk_master)

    def setGblMidiSource(self, source):
        self.gbl_midi_source = self.midi_ins.index(source)

    def setGblMidiTarget(self, target):
        self.gbl_midi_target = self.midi_outs.index(target)

    def getGblMidiSource(self):
        return open_midiinput(self.gbl_midi_source)

    def getGblMidiTarget(self):
        return open_midioutput(self.gbl_midi_target)

    def getClkMaster(self):
        return open_midiinput(self.clk_master)





