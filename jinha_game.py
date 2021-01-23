class Jinha:
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

    def Attack(self, name_1, d_a, name_2):
        if d_a <= 0:
            d_a = 0
            print("공격할수없음")
        else:
            print("{0}, {1}의 데미지로 {2}을 공격".format(name_1, d_a, name_2))

    def damaged(self, name, damage):
        if damage <= 0:
            damage = 0
        elif damage > 0:
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                print("몬스터의 체력이 {0}이 되었다.".format(self.hp))
                print("몬스터는 사망했다.")
            else :
                print("몬스터는 체력이 {0}남았다.".format(self.hp))


jinha = Jinha("진하", 20, 7, 7, True)
mon1 = Jinha("몬스터1", 7, 2, 2, False)
jinha.Attack(jinha.name, jinha.damage-mon1.defence, mon1.name)
mon1.damaged("몬스터1", jinha.damage-mon1.defence)
print("이번엔 몬스터1이 진하를 공격한다.")
mon1.Attack(mon1.name, mon1.defence-jinha.damage, jinha.name)
jinha.damaged(jinha.name, mon1.defence-jinha.damage)
print("다시 진하의 공격")
jinha.Attack(jinha.name, jinha.damage-mon1.defence, mon1.name)
mon1.damaged(mon1.name, jinha.damage-mon1.defence)'''







