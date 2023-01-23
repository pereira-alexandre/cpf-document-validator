class CPFValidator:
    
    def __init__(self, document):
        self.__documentNumber = document   #private attribute
        self.DOCUMENT_SIZE = 11
        self.SUM_LIMIT = 10
        self.THENTH_DIGIT = 9
        self.ELEVENTH_DIGIT = 10


    def isCPF(self):
        if len(self.__documentNumber) != self.DOCUMENT_SIZE:
            return False

        if not self.__isDigitValid():
            return False

        if not self.__isNextToLastDigitValid():
            return False
        
        if not self.__isLastDigitValid():
            return False

        return True


    def __isDigitValid(self):   #private function
        validDigits = 0
        for digit in range(0, self.DOCUMENT_SIZE):
            validDigits += int(self.__documentNumber[digit])
            digit += 1
        if int(self.__documentNumber[0]) == (validDigits / self.DOCUMENT_SIZE):
            return False
        return True


    def __calculateDigit(self, digitPosition):
        total = 0
        multiplier = 10
        index = digitPosition - multiplier
        for i in range(index, digitPosition-1):
            value = int(self.__documentNumber[i])
            total += (value*multiplier)
            i+=1
            multiplier-=1
        modulus = self.DOCUMENT_SIZE - (total%self.DOCUMENT_SIZE)
        return 0 if modulus >= self.SUM_LIMIT else modulus


    def __isNextToLastDigitValid(self):
        return int(self.__documentNumber[self.THENTH_DIGIT]) == self.__calculateDigit(10)


    def __isLastDigitValid(self):
        return int(self.__documentNumber[self.ELEVENTH_DIGIT]) == self.__calculateDigit(11)

