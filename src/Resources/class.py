
from Resources.feat import Feat
from Resources.subclass import Subclass
class Class(object):
    '''
    D&D Character's Class class.
    '''
    __hitDice=0 #d8 would just be 8, might need to think about incorporating a different (possible a dice class) method to handle the homebrew case of multiple dice
    __savingThrows=[0] #list of saving throw proficiencies
    __skillsAvail=0 #number of skills able to choose
    __skills=[0] #list of skills to choose from
    __proficiencies=[0] #array of weapon, armor, and tool proficiencies, for now using text parsing/matching to check, there might be an easier way
    __equipment=[[0,0]] #starting equipment choices. 2D to accomodate the multiple choices
    __feats=[[0,0]] #2d array of feats and the level aquired
    __specLv=0 #level class gains subclass
    __subclasses=[0] #list of subclasses

    def __init__(self, hitDie, savingThrows, skillsAvail,skills, proficiencies, equipment,feats,specLv,subclasses):
        '''
        Constructor
        '''
    #having trouble thinking of how to handle different class resources like Sneak Attack, Sorcery Point, Ki, etc elegantly and dynamically 