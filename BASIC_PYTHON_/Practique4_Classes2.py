# getters/setters Annotations
class P:
    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1001)
print(p1.x)

p1.x = -12
print(p1.x)

# Sans annotations less fancy same functionality
class P:

    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)

#Two ways to set
p1=P(34)
print(p1.x)
p1.x = 45
print(p1.x)
p1.set_x(50)
print(p1.x)


class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)