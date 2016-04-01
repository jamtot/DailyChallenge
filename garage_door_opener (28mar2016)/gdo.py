input0 = """button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete"""

input1 = """button_clicked
cycle_complete
button_clicked
block_detected
button_clicked
cycle_complete
button_clicked
block_cleared
button_clicked
cycle_complete"""

class GarageDoor(object):

    CLOSED, OPENING, OPEN, CLOSING, STOPPED_OPENING, STOPPED_CLOSING, EMERGENCY_OPENING, OPEN_BLOCKED = range(8)

    doordict = { CLOSED:"CLOSED",   OPENING:"OPENING",   OPEN:"OPEN", 
                 CLOSING:"CLOSING", STOPPED_OPENING:"STOPPED OPENING",
                 STOPPED_CLOSING:"STOPPED CLOSING", 
                 EMERGENCY_OPENING:"EMERGENCY OPENING",
                 OPEN_BLOCKED:"OPEN BLOCKED" }

    def __init__(self):
        self.current = self.CLOSED

    def button_clicked(self):
        if self.current == self.CLOSED:
            self.current = self.OPENING
        elif self.current == self.OPEN:
            self.current = self.CLOSING
        elif self.current == self.OPENING:
            self.current = self.STOPPED_OPENING
        elif self.current == self.CLOSING:
            self.current = self.STOPPED_CLOSING
        elif self.current == self.STOPPED_OPENING:
            self.current = self.CLOSING
        elif self.current == self.STOPPED_CLOSING:
            self.current = self.OPENING

    def block_detected(self):
        if self.current == self.CLOSING:
            self.current = self.EMERGENCY_OPENING

    def block_cleared(self):
        if self.current == self.EMERGENCY_OPENING:
            self.current = self.OPENING
        elif self.current == self.OPEN_BLOCKED:
            self.current = self.OPEN
            
    def cycle_complete(self):
        if self.current == self.OPENING:
            self.current = self.OPEN
        elif self.current == self.CLOSING:
            self.current = self.CLOSED
        elif self.current == self.EMERGENCY_OPENING:
            self.current = self.OPEN_BLOCKED

    def run_input( self, inp):
        inp = inp.splitlines()
        print "INITIAL:", self.doordict[self.current]
        for line in inp:
            eval("self."+line+"()")
            print line, self.doordict[self.current]
        return self.doordict[self.current]

if __name__ == "__main__":
    g = GarageDoor()
    assert g.run_input(input0) == "CLOSED"
    print
    assert g.run_input(input1) == "CLOSED"
