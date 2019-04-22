#!/usr/bin/python
import math

class character(object):
    nextLvlXP = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000]
    passivePerception = 10
    xp = 0
    hp = 0
    initiative = 0
    proficiencyBonus = 2
    lvl = 1
    carryCapacity = 0
    name=""


    #placeholder until classes are completed    
    race=""
    Class=""
    background=""
    
    def addHP(self, diceRoll):
        self.hp += diceRoll + abilityMod(self.con)

    def addXP(self, experience2Add):
        self.xp += experience2Add
        if self.xp>self.nextLvlXP(self.lvl):
            self.lvl+=1
            if self.lvl%4==0:
                self.proficiencyBonus+=1


        
    def __init__(self, name, race, Class, background, abilityScoreList, **kwargs): #abilitiyScores are a list
        '''
        Constructor
        
        '''
        
        self.name=name
        self.race=race
        self.Class=Class
        self.background=background
        
        self.strength = ability(abilityScoreList[0], self.proficiencyBonus, False)
        self.dexterity = ability(abilityScoreList[1], self.proficiencyBonus, False)
        self.constitution = ability(abilityScoreList[2], self.proficiencyBonus, False)
        self.intelligence = ability(abilityScoreList[3], self.proficiencyBonus, False)
        self.wisdom = ability(abilityScoreList[4], self.proficiencyBonus, False)
        self.charisma = ability(abilityScoreList[5], self.proficiencyBonus, False)

        #self.hp = race.hitDice + self.con.mod
        self.initiative = self.dexterity.mod
        self.carryCapacity = self.strength.score*15
        
        #Strength
        self.athletics = skill(self.strength.mod, self.proficiencyBonus, False, False)
        
        #Dexterity
        self.acrobatics = skill(self.dexterity.mod, self.proficiencyBonus, False, False)
        self.sleightOfHand  = skill(self.dexterity.mod, self.proficiencyBonus, False, False)
        self.stealth = skill(self.dexterity.mod, self.proficiencyBonus, False, False)

        #Intelligence
        self.arcana = skill(self.intelligence.mod, self.proficiencyBonus, False, False)
        self.history = skill(self.intelligence.mod, self.proficiencyBonus, False, False)
        self.investigation = skill(self.intelligence.mod, self.proficiencyBonus, False, False)
        self.nature = skill(self.intelligence.mod, self.proficiencyBonus, False, False)
        self.religion = skill(self.intelligence.mod, self.proficiencyBonus, False, False)

        #Wisdom
        self.animalHandling = skill(self.wisdom.mod, self.proficiencyBonus, False, False)
        self.insight = skill(self.wisdom.mod, self.proficiencyBonus, False, False)
        self.medicine = skill(self.wisdom.mod, self.proficiencyBonus, False, False)
        self.perception = skill(self.wisdom.mod, self.proficiencyBonus, False, False)
        self.survival = skill(self.wisdom.mod, self.proficiencyBonus, False, False)

        #Charisma:
        self.deception = skill(self.charisma.mod, self.proficiencyBonus, False, False)
        self.intimidation = skill(self.charisma.mod, self.proficiencyBonus, False, False)
        self.performance = skill(self.charisma.mod, self.proficiencyBonus, False, False)
        self.persuasion = skill(self.charisma.mod, self.proficiencyBonus, False, False)

        


        
    '''
    classdocs
    '''

class ability(character):
    '''
    classdocs

    '''
    score =8
    mod =0
    proficient= False
    savingThrow =0
  

    def __init__(self, score, bonus, proficient):
        '''
        Constructor
        '''
        self.score=score
        self.mod= math.floor((score-10)/2)
        self.SavingThrow=self.mod
        self.proficient=proficient
        if(proficient):
            self.savingThrow+=bonus
        



class skill(ability):
    '''
    classdocs
    
    is there a 'parent instance'? e.g. to have the value of athletics.mod
    default to the strength.mod value, rather than the default ability.mod value?
    '''
    expert= False


    def __init__(self, mod, bonus, proficient, expert):
        '''
        Constructor
        '''
        self.mod=mod
        self.proficient = proficient
        self.expert = expert
        if(proficient):
            self.mod+=bonus
            if(expert):
                self.mod+=bonus

    
    

        
        
        
    

