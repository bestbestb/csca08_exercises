class LightSwitch:
    def __init__(self, state):
        """ set its default state by inputting a string "on" or "off"
        """
        if state == 'on':
            self.state = True
        elif state == 'off':
            self.state = False
            
    def turn_on(self, state):
        
        self.state = True
            
    def turn_off(self):
        
        self.state = False
        
    def flip(self):
        self.state = not self.state
            
            
    def print_status(self):
        if self.state == True:
            return 'I am on'
        elif self.state == False:
            return 'I am off'
            
            
class SwitchBoard:
    def __init__(self, num_switches):
        
        
        self.num_swithches = num_switches
        
        # make an empty list for the switches
        switches = []
        i = 0
        while i < num_switches:
            switches.append(LightSwitch(False))
            i += 1
            
        self.switches = switches    
        
    def __str__(self):
        return "The following switches are on: " + (' '.join(self.switches))
    
    def which_switch(self):
        
        '''return a list of integers representing the switches that are on, in
order
        '''
        
        for i in range(len(switches)):
            
            result = []
            
            if switches[i].is_on == True:
                
                result.append(str(i)) #
            return result        
        
    def flip(self, n):
        nth = switches[n]
        self.nth.flip()
        
    def filp_every(self, n):
        '''d flip the state of every nth lightswitch, starting at 0.
        '''
        
        i = 0
        mult_i = n * i
        while mult_i < len(self.switches):
            self.filp(n * k) 
            k += 1
                
    def reset(self, n):
        '''  turn all switches off.
        '''
        
        for switches in self.switches:
            switches.turn_off()


if(__name__ == "__main__"):
    board = SwitchBoard(5)
    i = 1
    while i < 5:
        board.flip_every(i)
        i += 1
x = SwitchBoard(4)
print(x)
x.flip(2)
print(x)         

###if(__name__ == "__main__"):
    ##a = LightSwitch("on")
   # a.flip()
   # print(a.print_status())
    