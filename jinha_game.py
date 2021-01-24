class Character:
    def __init__(self, name, hp, damage, defence):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence

    def Attack(self, enemy):
        if self.damage - enemy.defence <= 0:
            self.damage = enemy.defence
            print("상대 방어력이 높아 공격불가")
            print("{0}의 체력은 그대로이다.".format(enemy.name))
        else:
            print("{0}, {1}의 데미지로 {2}을 공격!".format(self.name, self.damage - enemy.defence, enemy.name))
            enemy.hp -= (self.damage - enemy.defence)
            if enemy.hp > 0:
                print("{0}의 체력이 {1}이 되었다.".format(enemy.name, enemy.hp))
            else:
                enemy.hp = 0
                print("{0}의 체력이 0이 되었다.".format(enemy.name))
                print("{0} 사망".format(enemy.name))
                print("{0}의 현재 체력 :{1}".format(self.name, self.hp))


class User(Character):
    def __init__(self, name, hp, damage, defence):
        Character.__init__(self, name, hp, damage, defence)
        print("{0}의 모험시작!  [체력: {1}   공격력: {2}   방어력: {3}]".format( \
            name, hp, damage, defence))




class Monster(Character):
    def __init__(self, name, hp, damage, defence):
        Character.__init__(self, name, hp, damage, defence)
        print("야생의 {0} 출현! [체력: {1}   공격력:{2}   방어력: {3}]".format(name, hp, damage, defence))


jinha = User("진하", 20, 7, 7)
mon1 = Monster("몬스터1", 7, 2, 2)
jinha.Attack(mon1)
print("이번엔 몬스터1이 진하를 공격한다.")
mon1.Attack(jinha)
print("다시 진하의 공격")
jinha.Attack(mon1)

'''class Jinha:
    def __init__(self, name, hp, damage, defence, user):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.user = user
        if(user == True):
            print("{0}의 모험시작!  [체력: {1}   공격력: {2}   방어력: {3}]".format(\
            name, hp, damage, defence))
        else:
            print("야생의 {0} 출현! [체력: {1}   공격력:{2}   방어력: {3}]".format(name, hp, damage, defence))

    def Attack(self, enemy):
        if self.damage - enemy.defence <= 0:
            self.damage = enemy.defence
            print("상대 방어력이 높아 공격불가")
            print("{0}의 체력은 그대로이다.".format(enemy.name))
        else:
            print("{0}, {1}의 데미지로 {2}을 공격!".format(self.name, self.damage - enemy.defence, enemy.name))
            enemy.hp -= (self.damage - enemy.defence)
            if enemy.hp > 0:
                print("{0}의 체력이 {1}이 되었다.".format(enemy.name, enemy.hp))
            else:
                enemy.hp = 0
                print("{0}의 체력이 0이 되었다.".format(enemy.name))
                print("{0} 사망".format(enemy.name))
                print("{0}의 현재 체력 :{1}".format(self.name, self.hp))


jinha = Jinha("진하", 20, 7, 7, True)
mon1 = Jinha("몬스터1", 7, 2, 2, False)
jinha.Attack(mon1)
print("이번엔 몬스터1이 진하를 공격한다.")
mon1.Attack(jinha)
print("다시 진하의 공격")
jinha.Attack(mon)'''







