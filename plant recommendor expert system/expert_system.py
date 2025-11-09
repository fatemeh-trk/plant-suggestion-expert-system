from experta import *
from experta import KnowledgeEngine


class plantRec(Fact):
    """user inputs"""
    pass

class plantExpert(KnowledgeEngine):
    @Rule(plantRec(light='low',humidity='low',care='easy',kid_friendly='yes',
                   water='low',space='small'))
    def snake_plant(self):
        self.declare(Fact(plant='Snake Plant', info='Low light, minimal care, safe for kids.'))


    @Rule(plantRec(light='medium', humidity='medium', care='moderate',
                              kid_friendly='yes', water='medium', space='medium'))
    def spider_plant(self):
        self.declare(Fact(plant='Spider Plant', info='Cleans air, medium light, kid-safe.'))

    @Rule(plantRec(light='high', humidity='high', care='difficult',
                              kid_friendly='no', water='high', space='large'))
    def fiddle_leaf_fig(self):
        self.declare(Fact(plant='Fiddle Leaf Fig', info='Thrives in bright spaces, needs care, not pet-safe.'))

    @Rule(plantRec(light='medium', humidity='high', care='easy',
                              kid_friendly='yes', water='medium', space='small'))
    def peace_lily(self):
        self.declare(Fact(plant='Peace Lily', info='Loves humidity, easy care, elegant look.'))

    @Rule(plantRec(light='low', humidity='medium', care='easy',
                              kid_friendly='no', water='low', space='small'))
    def pothos(self):
        self.declare(Fact(plant='Pothos', info='Grows anywhere, trailing vines, not safe for pets.'))

    @Rule(plantRec(light='high', humidity='medium', care='moderate',
                              kid_friendly='yes', water='medium', space='large'))
    def rubber_plant(self):
        self.declare(Fact(plant='Rubber Plant', info='Bright light, strong look, moderate care.'))

    @Rule(plantRec(light='medium', humidity='low', care='easy',
                              kid_friendly='yes', water='low', space='small'))
    def aloe_vera(self):
        self.declare(Fact(plant='Aloe Vera', info='Medicinal plant, minimal watering, easy maintenance.'))


