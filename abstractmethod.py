from abc import ABCMeta , abstractmethod
class Animal(metaclass = ABCMeta):
    def __init__(self,color,race,name,gender):
        self.color = color
        self.race = race
        self.name = name
        self.gender = gender
        
    @abstractmethod   
    def sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    
class dog(Animal):
    @property
    def sound(self):
        return "how how"
        
    @property
    def eat(self):
        return "yam yam yam"
        
        
        
class horse(Animal):
    @property
    def sound(self):
        return "hi hi"
        
    @property
    def eat(self):
        return "yam yam yam"
    
    
    canicorso = dog('red','dd' ,'sali','jj')
    print(canicorso.)
    print(canicorso.sound)
