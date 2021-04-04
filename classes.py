#class classname:
#   def __init__(self):
#       self.atrebiute = 0
#    def anotherfunctiun(self):
#       anotherfunction(s)  
#   
#self == to enteract whit the classit self



#class inheritenceclassname(Parentclass):
#
#    def __init__ (self,input1,input2):
#        Parentclass.__init__(self)
#        self.attribiute1 = input1
#        self.attribiute2 = input2
#        self.attrebiute3 = 0
#
#    def anothermethod(self):
#        action



class team:
    def __init__ (self,name = 'name',origin = 'origin'):
        self.teamname = name
        self.teamorigin = origin

    def defineteamname(self,name):
        self.teamname = name

    def defineteameorigin(self,origin):
        self.teamorigin = origin



class player(team):

    def __init__ (self):
        team.__init__(self)
        self.playername = 'none'
        self.playerpoints = 0

    def scoredpoints(self):
        self.platyerpoints += 1
    
    def setname(self,name):
        self.playername = name

player1 = player()

print(player1.playername)

print(player1.playerpoints)



print(player1.teamname)

print(player1.teamorigin)