"""A package with various classes and functions to manipulate fractions."""
from math import gcd, lcm, floor, ceil

class Fraction:
    pass        

class MixedNumber:
    pass

class Fraction:
    """A class for representing rational numbers as the division of two quantities."""
    def __init__(self, numerator: int | float, denominator: int | float):
        self.numerator = numerator
        """The numerator of this Fraction."""
        self.denominator = denominator
        """The denominator of this Fraction."""

    def __setattr__(self, name, value):
        if name != "numerator" and name != "denominator":
            raise AttributeError("'Fraction' object has no attribute '" + name + "'")
        try:
            if (name == "numerator" and type(value) == float and self.__dict__["denominator"]) or (name == "denominator" and (type(self.numerator) == float or type(value) == float)):
                if name == "denominator":
                    if value < 0:
                        self.__dict__["numerator"] *= -1
                        value *= -1
                    elif value == 0:
                        self.__dict__["numerator"] = 0
                        value = 1
                self.__dict__[name] = value
                len_n, len_d = 0, 0
                if str(self.numerator).find(".") != -1:
                    len_n = len(str(self.numerator).split(".")[1])
                if str(self.denominator).find(".") != -1:
                    len_d = len(str(self.denominator).split(".")[1])
                inverse_int = eval("1e+" + str(max(len_n, len_d)))
                self.__dict__["numerator"] *= inverse_int
                self.__dict__["denominator"] *= inverse_int
                self.__dict__["numerator"] = int(self.numerator)
                self.__dict__["denominator"] = int(self.denominator)
            elif type(value) == int:
                self.__dict__[name] = value
            else:
                raise TypeError("The " + name + " attribute should be an int or float")
            gcd_of_terms = gcd(self.numerator, self.denominator)
            self.__dict__["numerator"] //= gcd_of_terms
            self.__dict__["denominator"] //= gcd_of_terms
        except (AttributeError, KeyError):
            self.__dict__[name] = value

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __repr__(self):
        return "Fraction(" + str(self) + ")"
    
    def __int__(self):
        if self.numerator >= 0:
            return floor(self)
        else:
            return ceil(self)

    def __float__(self):
        return self.numerator / self.denominator
    
    def __index__(self):
        return int(self)
    
    def __trunc__(self):
        return int(self)
    
    def __add__(self, other: int | float | Fraction | MixedNumber):
        other = convert_to_fraction(other)
        lcm_of_d = lcm(self.denominator, other.denominator)
        return Fraction(self.numerator * lcm_of_d / self.denominator + other.numerator * lcm_of_d / other.denominator, lcm_of_d)

    __radd__ = __add__
    
    def __sub__(self, other: int | float | Fraction | MixedNumber):
        return self + -other
    
    def __rsub__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_fraction(other) - self
    
    def __mul__(self, other: int | float | Fraction | MixedNumber):
        other = convert_to_fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    __rmul__ = __mul__

    def __truediv__(self, other: int | float | Fraction | MixedNumber):
        return self * convert_to_fraction(other).reciprocal()
    
    def __rtruediv__(self, other: int | float | Fraction | MixedNumber):
        other = convert_to_fraction(other)
        self_rec = self.reciprocal()
        return Fraction(self_rec.numerator * other.numerator, self_rec.denominator * other.denominator)
    
    def __floordiv__(self, other: int | float | Fraction | MixedNumber):
        return Fraction(floor(self / other), 1)
    
    def __rfloordiv__(self, other: int | float | Fraction | MixedNumber):
        return Fraction(floor(other / self), 1)
    
    def __mod__(self, other: int | float | Fraction | MixedNumber):
        return self - other * (self / other)
    
    def __rmod__(self, other: int | float | Fraction | MixedNumber):
        return other - self * (other / self)
    
    def __divmod__(self, other: int | float | Fraction | MixedNumber):
        return (self // other, self % other)
    
    def __rdivmod__(self, other: int | float | Fraction | MixedNumber):
        return (other // self, other % self)

    def __pow__(self, other: int | float | Fraction | MixedNumber):
        other = float(other)
        if other == 0:
            return Fraction(1, 1)
        elif other < 0:
            return self.reciprocal() ** (-other)
        else:
            return Fraction(self.numerator ** other, self.denominator ** other)
        
    def __rpow__(self, other: int | float | Fraction | MixedNumber):
        float_self = float(self)
        other = convert_to_fraction(other)
        if self == 0:
            return Fraction(1, 1)
        elif self < 0:
            return other.reciprocal() ** (-self)
        else:
            return Fraction(other.numerator ** float_self, other.denominator ** float_self)
    
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)
    
    def __round__(self, ndigits):
        return round(float(self), ndigits)
    
    def __floor__(self):
        return self.numerator // self.denominator
    
    def __ceil__(self):
        return ceil(self.numerator / self.denominator)
    
    def __lt__(self, other: int | float | Fraction | MixedNumber):
        other = convert_to_fraction(other)
        lcm_of_d = lcm(self.denominator, other.denominator)
        return self.numerator * lcm_of_d / self.denominator < other.numerator * lcm_of_d / other.denominator
        
    def __gt__(self, other: int | float | Fraction | MixedNumber):
        other = convert_to_fraction(other)
        lcm_of_d = lcm(self.denominator, other.denominator)
        return self.numerator * lcm_of_d / self.denominator > other.numerator * lcm_of_d / other.denominator
    
    def __le__(self, other: int | float | Fraction | MixedNumber):
        return not self > other
    
    def __ge__(self, other: int | float | Fraction | MixedNumber):
        return not self < other
    
    def __eq__(self, other):
        other = convert_to_fraction(other)
        return self.numerator == other.numerator and self.denominator == self.denominator
    
    def __ne__(self, other):
        return not self == other

    def reciprocal(self):
        """Returns the inverse of this Fraction."""
        return Fraction(self.denominator, self.numerator)
    
    def get_type(self):
        """Returns a string indicating whether this Fraction is a proper fraction, an improper fraction or a unit fraction."""
        if self.numerator < self.denominator:
            return "proper"
        elif self.numerator > self.denominator:
            return "improper"
        else:
            return "unit"

class MixedNumber:
    """A class for representing rational numbers as a whole number plus a proper fraction."""
    def __init__(self, whole: int, fraction: Fraction):
        self.whole = whole
        """The whole part of this MixedNumber."""
        self.fraction = fraction
        """The fractional part of this MixedNumber."""
    
    def __setattr__(self, name, value):
        if name != "whole" and name != "fraction":
            raise AttributeError("'Fraction' object has no attribute '" + name + "'")
        if name == "whole" and type(value) != int:
            raise TypeError("The whole attribute should be an int")
        elif name == "fraction":
            if type(value) != Fraction:
                raise TypeError("The fraction attribute should be a Fraction")
            elif value >= 1 or value <= -1:
                self.__dict__["whole"] += int(value)
                value -= int(value)
        self.__dict__[name] = value
    
    def __str__(self):
        return str(self.whole) + " " + str(self.fraction)
    
    def __repr__(self):
        return "MixedNumber(" + str(self) + ")"
    
    def __int__(self):
        return self.whole

    def __float__(self):
        return self.whole + self.fraction.numerator / self.fraction.denominator
    
    def __index__(self):
        return int(self)
    
    def __trunc__(self):
        return int(self)
    
    def __add__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(convert_to_fraction(self) + convert_to_fraction(other))

    __radd__ = __add__
    
    def __sub__(self, other: int | float | Fraction | MixedNumber):
        return self + -other
    
    def __rsub__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(convert_to_fraction(self) - convert_to_fraction(other))
    
    def __mul__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(convert_to_fraction(self) * convert_to_fraction(other))
    
    __rmul__ = __mul__

    def __truediv__(self, other: int | float | Fraction | MixedNumber):
        return self * convert_to_fraction(other).reciprocal()
    
    def __rtruediv__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(convert_to_fraction(other) * convert_to_fraction(self).reciprocal())
    
    def __floordiv__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(Fraction(floor(self / other), 1))
    
    def __rfloordiv__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(Fraction(floor(other / self), 1))
    
    def __mod__(self, other: int | float | Fraction | MixedNumber):
        return self - other * (self / other)
    
    def __rmod__(self, other: int | float | Fraction | MixedNumber):
        return convert_to_mixed_number(other - self * (other / self))
    
    def __divmod__(self, other: int | float | Fraction | MixedNumber):
        return (self // other, self % other)
    
    def __rdivmod__(self, other: int | float | Fraction | MixedNumber):
        return (convert_to_mixed_number(other // self), convert_to_mixed_number(other % self))

    def __pow__(self, other: int | float | Fraction | MixedNumber):
        fraction_self = convert_to_fraction(self)
        other = float(other)
        if other == 0:
            return MixedNumber(1, Fraction(0, 1))
        elif other < 0:
            return convert_to_mixed_number(fraction_self.reciprocal() ** (-other))
        else:
            return convert_to_mixed_number(Fraction(fraction_self.numerator ** other, fraction_self.denominator ** other))
        
    def __rpow__(self, other: int | float | Fraction | MixedNumber):
        float_self = float(self)
        other = convert_to_fraction(other)
        if self == 0:
            return MixedNumber(1, Fraction(0, 1))
        elif self < 0:
            return convert_to_mixed_number(other.reciprocal() ** (-self))
        else:
            return convert_to_mixed_number(Fraction(other.numerator ** float_self, other.denominator ** float_self))
    
    def __neg__(self):
        return MixedNumber(-self.whole, -self.fraction)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return MixedNumber(abs(self.whole), abs(self.fraction))
    
    def __round__(self, ndigits):
        return round(float(self), ndigits)
    
    def __floor__(self):
        return floor(convert_to_fraction(self))
    
    def __ceil__(self):
        return ceil(convert_to_fraction(self))
    
    def __lt__(self, other: int | float | Fraction | MixedNumber):
        fraction_self = convert_to_fraction(self)
        other = convert_to_fraction(other)
        lcm_of_d = lcm(self.denominator, other.denominator)
        return fraction_self.numerator * lcm_of_d / fraction_self.denominator < other.numerator * lcm_of_d / other.denominator
        
    def __gt__(self, other: int | float | Fraction | MixedNumber):
        fraction_self = convert_to_fraction(self)
        other = convert_to_fraction(other)
        lcm_of_d = lcm(self.denominator, other.denominator)
        return fraction_self.numerator * lcm_of_d / fraction_self.denominator > other.numerator * lcm_of_d / other.denominator
        
    def __le__(self, other: int | float | Fraction | MixedNumber):
        return not self > other
    
    def __ge__(self, other: int | float | Fraction | MixedNumber):
        return not self < other
    
    def __eq__(self, other: int | float | Fraction | MixedNumber):
        fraction_self = convert_to_fraction(self)
        other = convert_to_fraction(other)
        return fraction_self.numerator == other.numerator and fraction_self.denominator == other.denominator
    
    def __ne__(self, other: int | float | Fraction | MixedNumber):
        return not self == other

    def reciprocal(self):
        """Returns the inverse of this MixedNumber."""
        return 1 / self

def convert_to_fraction(x: int | float | MixedNumber):
    """Create a Fraction from x, where x should be an int, float or MixedNumber."""
    if type(x) == int or type(x) == float:
        return Fraction(x, 1)
    elif type(x) == MixedNumber:
        return Fraction(x.whole * x.fraction.denominator + x.fraction.numerator, x.fraction.denominator)
    elif type(x) == Fraction:
        return x
    else:
        raise TypeError("The x parameter should be an int, float or MixedNumber.")
    
def convert_to_mixed_number(x: int | float | Fraction):
    """Create a MixedNumber from x, where x should be an int, float or Fraction."""
    if type(x) == int or type(x) == float:
        return MixedNumber(0, Fraction(x, 1))
    elif type(x) == Fraction:
        return MixedNumber(0, x)
    elif type(x) == MixedNumber:
        return x
    else:
        raise TypeError("The x parameter should be an int, float or Fraction.")
    
def is_like(x: Fraction, y: Fraction):
    """Returns a boolean indicating whether x and y are like fractions."""
    if type(x) != Fraction:
        raise TypeError("The x parameter should be a Fraction")
    elif type(y) != Fraction:
        raise TypeError("The y parameter should be a Fraction")
    return convert_to_fraction(x).denominator == convert_to_fraction(y).denominator

if __name__ == "__main__":
    frac1 = Fraction(17, 0.0626)
    frac2 = Fraction(1204.5, -1650)
    print("Debug")
    if str(frac1) == "85000/313":
        print("1st test succeeded")
    else:
        print("1st test failed ------ str(frac1) != \"85000/313\"")
    if int(frac1) == 271:
        print("2nd test succeeded")
    else:
        print("2nd test failed ------ int(frac1) != 271")
    if float(frac1) == 271.5654952076677:
        print("3rd test succeeded")
    else:
        print("3rd test failed ------ float(frac1) != 271.5654952076677")
    if str(frac2) == "-73/100":
        print("4th test succeeded")
    else:
        print("4th test failed ------ str(frac2) != \"-73/100\"")
    if int(frac2) == 0:
        print("5th test succeeded")
    else:
        print("5th test failed ------ int(frac2) != 0")
    if float(frac2) == -0.73:
        print("6th test succeeded")
    else:
        print("6th test failed ------ float(frac2) != -0.73")
    if str(frac1 + 0.65) == "1704069/6260":
        print("7th test succeeded")
    else:
        print("7th test failed ------ str(frac1 + 0.65) != \"1704069/6260\"")
    if str(frac2 + 0.5517) == "-1783/10000":
        print("8th test succeeded")
    else:
        print("8th test failed ------ str(frac2 + 0.5517) != \"-1783/10000\"")
    if str(frac1 + frac2) == "8477151/31300":
        print("9th test succeeded")
    else:
        print("9th test failed ------ str(frac1 + frac2) != \"8477151/31300\"")
    if str(frac1 - 0.65) == "1695931/6260":
        print("10th test succeeded")
    else:
        print("10th test failed ------ str(frac1 - 0.65) != \"1695931/6260\"")
    if str(frac2 - 0.5517) == "-12817/10000":
        print("11th test succeeded")
    else:
        print("11th test failed ------ str(frac2 - 0.5517) != \"-12817/10000\"")
    if str(0.65 - frac1) == "-1695931/6260":
        print("12th test succeeded")
    else:
        print("12th test failed ------ str(0.65 - frac1) != \"-1695931/6260\"")
    if str(0.5517 - frac2) == "12817/10000":
        print("13th test succeeded")
    else:
        print("13th test failed ------ str(0.5517 - frac2) != \"12817/10000\"")
    if str(frac1 - frac2) == "8522849/31300":
        print("14th test succeeded")
    else:
        print("14th test failed ------ str(frac1 - frac2) != \"8522849/31300\"")