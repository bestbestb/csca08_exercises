class LightSwitch:

    def __init__(self, state):
        if (state == "on"):
            self.state = True
        elif (state == "off"):
            self.state = False

    def turn_on(self):
        if (self.state is True):
            raise InvalidSwitchException
        else:
            self.state = True

    def turn_off(self):
        if (self.state is False):
            raise InvalidSwitchException
        else:
            self.state = False

    def flip(self):
        self.state = not self.state

    def __str__(self):
        if (self.state is True):
            return("I am on")

        elif (self.state is False):
            return("I am off")


class InvalidSwitchException(Exception):
    pass


class NoSuchSwitchException(Exception):
    pass


class SwitchBoard:
    def __init__(self, numswitches):
        self.listswitch = []
        self.liston = []
        index = 0
        for index in range(numswitches):
            self.listswitch.append(LightSwitch("off"))

    def __str__(self):
        printstatement = "The following switches are on:  "
        indice = 0
        self.which_switch()
        for indice in range(len(self.liston)):
            printstatement += str(self.liston[indice])
            printstatement += " "
        return (printstatement)

    def which_switch(self):
        indice = 0
        for indice in range(len(self.listswitch)):
            if (self.listswitch[indice].state is True):
                self.liston.append(indice)

    def flip(self, num):
        if (num < 0):
            raise InvalidSwitchException
        elif (num > len(self.listswitch)):
            raise NoSuchSwitchException
        else:
            self.listswitch[num].flip()

    def flip_every(self, num):
        indice = 0
        if (num < 0) or (num > len(self.listswitch)):
            raise InvalidSwitchException
        else:
            for indice in range(0, len(self.listswitch), num):
                self.listswitch[indice].flip()

    def reset():
        indice = 0
        for indice in range(len(self.listwitch)):
            try:
                self.listswitch[indice].turn_off()
            except:
                pass
if(__name__ == "__main__"):
    switchboard = SwitchBoard(1023)
    loop = 1
    for loop in range(1, 1023):
        switchboard.flip_every(loop)
    print(switchboard)