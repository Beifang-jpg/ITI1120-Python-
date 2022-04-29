class RationalNumber:
    numerator = 0
    denominator = 1
    def __init__(self,a,b):

        if (b == 0):
            raise ValueError(print("denominator can't be 0"))
            return
        else:
            if a > b:
                smaller = b
            else:
                smaller = a
            c = 0
            smaller = int(smaller)
            for i in range(1, smaller+1):
                if((a % i == 0) and (b % i == 0)):
                    c = i 
            if(c == 0):
                self.numerator = a
                self.denominator = b
            else:
                n = a/c
                d = b/c
                self.numerator = n
                self.denominator = d

            if(self.denominator < 0):
                self.denominator = self.denominator * (-1)
                self.numerator = self.numerator * (-1)
            else:
                pass

    def denominator(self):
        d = self.denominator
        return d
    def numerator(self):
        n = self.numerator
        return n

    def __str__(self) -> str:
        if(self.denominator == 1):
            return(str(int(self.numerator)))
        elif(self.numerator == 0):
            return("0")
        else:
            return(str(int(self.numerator)) + "/"+str(int(self.denominator)))

    def __eq__(self, other) -> bool:
        a = (self.numerator / self.denominator)
        b = (other.numerator / other.denominator)
        if ( a == b):
            return True
        else:
            return False

    def __gt__(self,other):
        a = (self.numerator / self.denominator)
        b = (other.numerator / other.denominator)

        if(a>b):
            return True
        else:
            return False

    def __lt__(self,other):


        a = (self.numerator / self.denominator)
        b = (other.numerator / other.denominator)

        if(a>b):
            return False
        else:
            return True

    def __add__(self,other):
        # newR = RationalNumber()
        
        a = self.denominator
        b = other.denominator
        if a > b:
            smaller = b
        else:
            smaller = a
        c = 0
        base = 0
        smaller = int(smaller)

        for i in range(1, smaller+1):
            if((a % i == 0) and (b % i == 0)):
                c = i 
        if(c == 0):
            base = a * b
        else:
            base = (a*b)/c
        up = (self.numerator * (base/self.denominator)) + (other.numerator * (base/other.denominator))
        newR = RationalNumber(up,base)

        return newR

    def __sub__(self,other):
        # newR = RationalNumber()
        
        a = self.denominator
        b = other.denominator
        if a > b:
            smaller = b
        else:
            smaller = a
        c = 0
        base = 0
        smaller = int(smaller)

        for i in range(1, smaller+1):
            if((a % i == 0) and (b % i == 0)):
                c = i 
        if(c == 0):
            base = a * b
        else:
            base = (a*b)/c
        up = (self.numerator * (base/self.denominator)) - (other.numerator * (base/other.denominator))
        newR = RationalNumber(up,base)

        return newR
    def __mul__(self,other):
        up = self.numerator * other.numerator
        base = self.denominator * other.denominator
        # print(up ,"and",base)
        # print(other.numerator ," and", other.denominator)

        newR = RationalNumber(up,base)
        return newR
    def __pow__(self,other):
        newR = RationalNumber(self.numerator,self.denominator)
        org = RationalNumber(self.numerator,self.denominator)

        if (other == 1):
            return newR

        for i in range (0,other-1):
            newR = newR * org
            # print("a")
        return newR 
    def __floordiv__(self, other):
        a = self.numerator / self.denominator
        b = other.numerator / other.denominator

        c = a//b
        c = int(c)
        return c
    def __truediv__(self, other):
        a = self.numerator / self.denominator
        b = other.numerator / other.denominator

        c = a/b
        return c



R1 = RationalNumber(20,30)
R2 = RationalNumber(1,6)
R11 = RationalNumber(1,4)

# R3 = R1 + R2
# R4 = R1 - R2
# R5 = R1 * R2
# R6 = R2**2
# R7 = R2**3
# R8 = R1 * 4
# R9 = R1 // R2
# R10 = R1// R11
# R12 = R1 /R2
# R13 = R1/ R11

# print(R3)
# print(R4)
# print(R5)
# print(R6)
# print(R7)
# print(R8)
# print(R9)
# print(R10)
# print(R12)
# print(R13)

class FractionMomo (RationalNumber):
    def __str__(self) -> str:
        if(self.denominator == 1):
            num = self.numerator
            num_str = str(self.numerator)
        elif(self.numerator == 0):
            num = 0
            num_str = "0"
        else:
            num = (self.numerator/ self.denominator)
            num_str = (str(int(self.numerator)) + "/"+str(int(self.denominator)))

        scientific = (f"{num:.1E}")
        scientific = str(scientific)
        AAA = "It is " + num_str + " and the scientific number is: " + scientific

        return AAA
    
    def __repr__(self) -> str:
        if(self.denominator == 1):
            num = self.numerator
            num_str = str(self.numerator)
        elif(self.numerator == 0):
            num = 0
            num_str = "0"
        else:
            num = (self.numerator/ self.denominator)
            num_str = (str(int(self.numerator)) + "/"+str(int(self.denominator)))

        scientific = (f"{num:.1E}")
        scientific = str(scientific)
        AAA = "It is " + num_str + " and the scientific number is: " + scientific

        return AAA