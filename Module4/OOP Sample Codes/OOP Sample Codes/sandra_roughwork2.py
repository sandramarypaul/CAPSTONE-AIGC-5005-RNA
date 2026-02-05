

class Loan:
    def __intit__(self,annualIntrestRate=2.5,
                  numberOfYears = 1,loanamount = 1000, borrower = " "):
        self.__annualIntrestRate = annualIntrestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanamount
        self.__borrower= borrower


    def getAnnualIntrestRate(self):
        return self.__annualIntrestRate
    
    def getNumberOfYears(self):
        return self.__numberOfYears
    
    def getLoanAmount(self):
        return self.__loanAmount
    
    def getBorrower(self):
        return self.__borrower
    
    def SetAnnualInrestRate(self, annualInrestRate):
        self.__annualIntrestRate =  annualInrestRate

    def setNumberOfYears(self,numberOfYears):
        self.__numberOfYears = numberOfYears


    def setLoanAmount(self,loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self,borrower):
        self.__borrower = borrower


    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = \
          self.__loanAmount * monthlyInterestRate / (1 - (1 / 
          (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * \
            self.__numberOfYears * 12
        return totalPayment   