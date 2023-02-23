class Mach(object):  # This is the parent class
    def __init__(self, i, m):
        self.Muuo = 'University College'
        self.isaac = i
        self.muuo = m

    def speak(self):
        print()
        print('I love', self.isaac, self.muuo)



class Lov(Mach):   # This is the child class, inherits properties of the Mach class
    def __init__(self, i, m, at):
        super(Lov, self).__init__(i, m)
        self.at = at

Einstein = Lov('Tharaka', 'University', 'very much')
Einstein.speak()


