class LightSwitch:
    ''' a lightswitch which is either on or off'''

    def __init__(self, state):
        '''(LightSwitch, str) -> Nonetype
        sets the default state when taking 'on' or 'off'
        '''
        self.state = state

    def turn_on(self):
        '''(LightSwitch) -> Nonetype
        turn the light on
        '''
        self.state = True

    def turn_off(self):
        '''(LightSwitch) -> Nonetype
        turn the light off
        '''
        self.state = False

    def flip(self):
        '''(LightSwitch) -> Nonetype
        revese the status of the switch
        '''
        self.state = not self.state

    def __str__(self):
        '''(LightSwitch) -> Nonetype
        return the status of the switch
        '''
        # if the status is True, return "I am on"
        if self.state:
            return "I am on"
        # if the status is False, return " I am off"
        elif not self.state:
            return "I am off"


class SwitchBoard:
    ''' a board for all the switches'''

    def __init__(self, num_switches):
        '''(SwitchBoard) -> Nonetype
        sets the total number of switches, and all the switches are off
        '''
        self.switches = []
        for i in range(num_switches+1):
            i = LightSwitch(False)
            self.switches.append(i)

    def __str__(self):
        '''(SwitchBoard) -> Nonetype
        return the switches that are on
        '''
        result = self.which_switch()
        result_str = ' '.join(result)
        return 'The following switches are on: ' + result_str

    def which_switch(self):
        '''(SwitchBoard) -> Nonetype
        return a list of integers representing the switches that are on, in
        order
        '''
        # make an empty list
        result = []
        # for each switch
        for i in range(len(self.switches)):
            # if the switch is on
            if self.switches[i].state:
                # append to the list
                result.append(str(i))
        return result

    def flip(self, n):
        '''(SwitchBoard, int) -> Nonetype
        reverse the status of switch at the given index
        '''
        self.switches[n].flip()

    def flip_every(self, n):
        '''(switchboard, int) -> Nonetype
        reverse the status of multiples of the switch at the given index
        REQ: n must be a positive integer
        '''

        i = 0
        # loop the multiple whle it's smaller than the total number of switches
        while i * n < len(self.switches):
            # flip the multiple
            self.flip(i * n)
            i += 1

    def reset(self):
        '''(switchboard) -> Nonetype
        reset all switches to default
        '''
        # for every switch
        for switch in self.swtitches:
            # turn it off
            switch.turn_off()

if (__name__ == "__main__"):
    # 1203 switches in total
    board = SwitchBoard(1023)
    i = 1
    # need to loop the cases from 1 to 1023
    while i < 1024:
        board.flip_every(i)
        i += 1

    print(board)
    
