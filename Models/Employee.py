class Employee:
    def __init__(self,email):
        self.__email=email
        self.__empName=email.split('@')[0]
    
    #---Getters and Setters---
    def getEmpName(self):
        return self.__empName
    
    def getEmail(self):
        return self.__email