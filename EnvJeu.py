import Morpion
import copy
import numpy
from random import *

class EnvJeu(object):
    """description of class"""

    monMorpion = Morpion.Morpion()
    actionIASimulee = numpy.ndarray(shape=(9, 1),
                    dtype=numpy.float32)

    #Constructeur
    #def __init__(self):
    #    #On crée l'objet morpion pour gérer la partie
    #    self.monMorpion 

    #On override la fonction reset
    def reset(self):
        #Permet de recommencer la partie
        self.monMorpion.initPartie()
        return self.monMorpion.getListePionJ_UN()

    #Fonction pour agir sur l'env
    def step(self, action, isJ1, isAlgo):


        if(isAlgo == True):
            #On gère l'autre déplacement
            self.actionIASimulee = numpy.zeros(9)
            move = self.monMorpion.getAllMovePossible()
            #Dans le cas où aucuns déplacement n'est possible
            if(len(move) > 0):
                moveChoisi = move[randint(0,len(move)-1)]
                #On max l'index du move
                self.actionIASimulee[moveChoisi] = 1.0
                #On fait le move
                result = self.monMorpion.tourJ_DEUX(copy.copy(self.actionIASimulee))

                if(result == 1):
                    #L'IA perd la partie
                    return self.monMorpion.getListePionJ_UN(), -10, True
            self.monMorpion.verificationFinPartie()
            return self.monMorpion.getListePionJ_DEUX(), 10, self.monMorpion.finPartie
        #On fait jouer l'IA
        self.actionIASimulee = numpy.zeros(9)
        self.actionIASimulee[action] = 1.0
        if(isJ1 == True):
            result = self.monMorpion.tourJ_UN(copy.copy(self.actionIASimulee))
        else:
            result = self.monMorpion.tourJ_DEUX(copy.copy(self.actionIASimulee))
        #On gère le score
        if(result == -2):
            self.monMorpion.finPartie = False
            #On passe à la partie suivante
            if(isJ1 == True):
                return self.monMorpion.getListePionJ_UN(), -50, True
            else:
                return self.monMorpion.getListePionJ_DEUX(), -50, True
        #partie gagnée
        elif(result == 1):
            if(isJ1 == True):
                return self.monMorpion.getListePionJ_UN(), 100, True
            else:
                return self.monMorpion.getListePionJ_DEUX(), 100, True

        

        #On retourne l'emplacement des pièces actuelles
        self.monMorpion.verificationFinPartie()
        if(isJ1 == True):

            return self.monMorpion.getListePionJ_UN(), 10, self.monMorpion.finPartie
        else:
            return self.monMorpion.getListePionJ_DEUX(), 10, self.monMorpion.finPartie

    #Fonction pour afficher les résultats
    def render(self):
        print(self.monMorpion.strToDisplay(numpy.asarray(self.monMorpion.getListePionJ_UN())))

