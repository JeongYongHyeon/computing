class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))

    def love(self, other):
        print("%s, %s 사랑에 빠지다." % (self.fullname, other.fullname))

    def fight(self, other):
        print("%s, %s 싸우네." % (self.fullname, other.fullname))

    def __add__(self, other):
        print("%s, %s 결혼했네." % (self.fullname, other.fullname))

    def __sub__(self, other):
        print("%s, %s 이혼했네." % (self.fullname, other.fullname))

    def __mul__(self, other):
        print("%s, %s 2세를 얻었네." % (self.fullname, other.fullname))

    def __truediv__(self, other):
        print("%s, %s 자식 결혼해서 출가했네." % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s,%s 여행 %d일 감." % (self.fullname, where, day))


pey = HousePark("가네")

juliet = HouseKim("사랑")

pey.travel("진도")

juliet.travel("진도", 5)

pey.love(juliet)

pey + juliet

pey * juliet

pey / juliet

pey.fight(juliet)

pey - juliet