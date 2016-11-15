
class LightSwitch:
    def __init__(self,condition):
        self.is_on = condition
     
             
    def turn_on(self):
        self.is_on = True
     
    def turn_off(self):
        self.is_on = False
         
    def flip(self):
        self.is_on = not self.is_on ##
             
    def __str__(self):
        if self.is_on == True:
            return "I am on"
        else:
            return "I am off"
 
class SwitchBoard:
    def __init__(self, number):
        self._lights = []
        for i in range(number):
            i = LightSwitch(False)
            self._lights.append(i)
 
    def which_switch(self):
        result = []
        for i in range(len(self._lights)): ##
            if self._lights[i].is_on == True:
                result.append(str(i)) #
        return result
 
    def __str__(self):
        result = self.which_switch() #
        result_str = ','.join(result)
        return 'The following switches are on: ' + result_str
    def flip(self, n):
        self._lights[n].flip() ##
 
    def flip_every(self, n):
        k = 0
        while n * k <= len(self._lights) - 1:
            self.flip(n * k) ##
            k = k + 1
    def reset(self):
        for light in self._lights:
            light.turn_off() ##
 
'''light_board = SwitchBoard(10)
print(light_board)
light_board.filp_every(2)
print(light_board)
light_board.filp(2)
print(light_board)
light_board.reset()
print(light_board)
light_board.filp_every(1)
print(light_board)
'''

if (__name__ == "__main__"):
    
    board = SwitchBoard(1203)
    i = 1
    
    while i < 5:
        
        board.flip_every(i)
        
        i += 1
    
    print(board)