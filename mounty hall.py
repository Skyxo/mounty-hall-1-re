from random import *

class Door():
    
    def __init__(self, id):
        self.opened = False
        self.iscar = False
        self.id = id
    
    def isCar(self):
        return self.iscar
        
    def setCar(self):
        self.iscar = True
    
    def getId(self):
        return self.id

def createList(n):
    doorlist_ = []
    for i in range(n):
        doorlist_.append(Door(i))
    return doorlist_

def program(change):

    #On remet tout à 0
    doors_ = createList(3)
    possiblechoicep_ = doors_.copy()
    possiblechoicej_ = doors_.copy()
    
    #On met une voiture derrière une des portes
    doorcar = choice(doors_)
    doorcar.setCar()
    
    #Le joueur choisi une porte
    firstchoicej = choice(doors_)
    
    #On retire le choix de la porte du joueur et le choix de la porte pour les possibilités de choix du présentateur
    if firstchoicej is doorcar:
        possiblechoicep_.remove(firstchoicej)
    else:
        possiblechoicep_.remove(doorcar)
        possiblechoicep_.remove(firstchoicej)

    #Le présentateur ouvre une des autres portes qui ne contient pas la voiture
    doorchoicep = choice(possiblechoicep_)

    #Le joueur décide s'il veut changer de choix
    possiblechoicej_.remove(doorchoicep)
    changechoice = change
    if changechoice:
        possiblechoicej_.remove(firstchoicej)
        secondchoicej = possiblechoicej_[0]
    else:
        secondchoicej = firstchoicej

    #On vérifie si le joueur a gagné
    if secondchoicej.isCar():
        return True
    else:
        return False

countwin = 0
countloose = 0

change = True                     #True pour le joueur change de choix, False pour qu'il ne change pas de choix

for i in range(10000):
    if program(change):
        countwin+=1
    else:
        countloose+=1

print("win: {}\nloose: {}".format(countwin, countloose))