def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

class Fraction:
    def __init__(self, top, bottom):
        if round(top) != top or round(bottom) != bottom:
            raise TypeError("Числитель и знаменатель должны быть целыми числами")

        abs_bottom = abs(bottom)
        common = gcd(top, abs_bottom)
        
        self.num = (-top if abs_bottom != bottom else top) // common
        self.dev = abs_bottom // common

    def __str__(self):
        return f"{self.num}/{self.dev}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.dev})"

    def __add__(self, other):
        if isinstance(other, Fraction):
            newnum = self.num * other.dev + other.num * self.dev
            newdev = self.dev * other.dev

            return Fraction(newnum, newdev)
        elif isinstance(other, int):
            return other + self
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            new_fraction = Fraction(other, 1)
            return self + new_fraction
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            newnum = self.num * other.dev + other.num * self.dev
            newdev = self.dev * other.dev

            common = gcd(newnum, newdev)

            self.num = newnum // common
            self.dev = newdev // common
            return self
        elif isinstance(other, int):
            self.num += other * self.dev
            return self
        else:
            return NotImplemented

    def __sub__(self, other):
        newnum = self.num * other.dev - other.num * self.dev
        newdev = self.dev * other.dev

        return Fraction(newnum, newdev)

    def __mul__(self, other):
        newnum = self.num * other.num
        newdev = self.dev * other.dev

        return Fraction(newnum, newdev)

    def __truediv__(self, other):
        newnum = self.num * other.dev
        newdev = other.num * self.dev

        return Fraction(newnum, newdev)

    def __eq__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num == second_num

    def __ne__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num != second_num

    def __lt__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num <= second_num

    def __gt__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.dev
        second_num = other.num * self.dev

        return first_num >= second_num


x = Fraction(1,2)
y = Fraction(1,4)
# print(x-y)
x += -2
print(x)
print(x.__repr__())
