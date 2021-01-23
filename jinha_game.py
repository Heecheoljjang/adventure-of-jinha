class  Monster :
    def __init__(self,name,hp_m,damage, defence):
        self.name = name
        self.hp_m = hp_m
        self.damage = damage
        self.defence = defence
        print("{0} 출현! [체력 : {1}   공격력 : {2}   방어력 : {3}]".format(\
            name,hp_m,damage,defence))

    def Attack_M(self,name_1,d_a,name_2) :
        '''self.name_1 = name_1
        self.name_2 = name_2
        self.d_a = d_a'''
        if d_a <= 0 :
            print("공격할수없음")
        else :
            print("{0}, {1}의 데미지로{2}을 공격".format(name_1,d_a,name_2))

    def damaged_M(self,name,damage):
        self.hp_m -= damage
        if self.hp_m > 0 :
             print("몬스터는 체력이 {0}남았다.".format(self.hp_m))
        else :
            print("몬스터는 사망했다.")

class  Jinha_ugly :
    def __init__(self,name,hp_j,damage, defence):
        self.name = name
        self.hp_j = hp_j
        self.damage = damage
        self.defence = defence
        print("{0}의 모험 시작! 진하의 상태 [체력 : {1}   공격력 : {2}   방어력 : {3}]".format(\
            name,hp_j,damage,defence))

    def Attack_J(self,name_1, d_a, name_2) :
        '''self.name_1 = name_1
        self.name_2 = name_2
        self.d_a = d_a'''
        print("{0}, {1}의 데미지로 {2}을 공격".format(name_1,d_a,name_2))

    def damaged_J(self,name,damage):
        self.hp_j -= damage
        print("진하는 체력이 {0}남았다.".format(self.hp_j))
        if self.hp_j <= 0 :
            print("진하는 사망해버렸다.")


jinha = Jinha_ugly("진하",20,7,7)
mon1 = Monster("몬스터1",7,2,2)
J_M = jinha.damage-mon1.defence #진하의 공격력 - 몬스터의 방어력
M_J = mon1.damage- jinha.defence #몬스터의 공격력 - 진하의 방어력
if M_J <= 0 :
    M_J = 0
print("진하는 몬스터1을 마주쳤다")
jinha.Attack_J(jinha.name, J_M, mon1.name)
mon1.damaged_M("몬스터1",J_M)
print("이번엔 몬스터1이 진하를 공격한다.")
mon1.Attack_M(mon1.name,M_J,jinha.name)
jinha.damaged_J(jinha.name,M_J)
print("다시 진하의 공격")
jinha.Attack_J(jinha.name,J_M,mon1.name)
mon1.damaged_M(mon1.name,J_M)







