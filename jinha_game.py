class Jinha :
    def __init__(self,name,hp,damage, defence):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        print("{0} 출현! [체력 : {1}   공격력 : {2}   방어력 : {3}]".format(\
            name,hp,damage,defence))

    def Attack(self,name_1,d_a,name_2) :
        if d_a <= 0 :
            print("공격할수없음")
        else :
            print("{0}, {1}의 데미지로 {2}을 공격".format(name_1,d_a,name_2))

    def damaged(self,name,damage):
        self.hp -= damage
        if self.hp > 0 :
             print("몬스터는 체력이 {0}남았다.".format(self.hp))
        else :
            print("몬스터는 사망했다.")


jinha = Jinha("진하",20,7,7)
mon1 = Jinha("몬스터1",7,2,2)
J_M = jinha.damage-mon1.defence #진하의 공격력 - 몬스터의 방어력
M_J = mon1.damage- jinha.defence #몬스터의 공격력 - 진하의 방어력
if M_J <= 0 :
    M_J = 0
jinha.Attack(jinha.name, J_M, mon1.name)
mon1.damaged("몬스터1",J_M)
print("이번엔 몬스터1이 진하를 공격한다.")
mon1.Attack(mon1.name,M_J,jinha.name)
jinha.damaged(jinha.name,M_J)
print("다시 진하의 공격")
jinha.Attack(jinha.name,J_M,mon1.name)
mon1.damaged(mon1.name,J_M)







