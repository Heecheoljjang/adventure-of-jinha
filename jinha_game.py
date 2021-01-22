class  Monster :
    def __init__(self,name,hp,damage, defence):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = defence
        print("{0} 출현! [체력 : {1}   공격력 : {2}   방어력 : {3}]".format(\
            name,hp,damage,defence))

class  Jinha_ugly :
    def __init__(self,name,hp,damage, defence):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = defence
        print("{0}의 모험 시작! 진하의 상태 [체력 : {1}   공격력 : {2}   방어력 : {3}]".format(\
            name,hp,damage,defence))

'''class Attack :
    def __init__(self,name_j,name_m) :
        self.attack = name_j
        self.defence = name_m
        print("{0}, {1}를 공격! ".format(name_j,name_m))'''






jinha = Jinha_ugly("진하",50,7,7)
mon1 = Monster("몬스터1",30,3,5)

