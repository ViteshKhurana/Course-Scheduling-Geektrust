from Models.Employee import Employee

class course:

    def __init__(self,courseName,instructor,date,minCapacity,maxCapacity,courseOfferingId):
        self.__courseName=courseName
        self.__instructor=instructor
        self.__date=date
        self.__minCapacity=minCapacity
        self.__maxCapacity=maxCapacity
        self.__courseOfferingId=courseOfferingId
        self.__registeredEmp={}
        self.__isCanceled=True
        self.__isAccepted=False
    
    #---Getters and Setters---

    def getCourseName(self):
        return self.__courseName
    
    def getInstructor(self):
        return self.__instructor

    def getDate(self):
        return self.__date

    def getMinEmp(self):
        return self.__minCapacity
    
    def getMaxEmp(self):
        return self.__maxCapacity
    
    def getCourseId(self):
        return self.__courseOfferingId
    
    def getRegEmp(self):
        return self.__registeredEmp
    
    def getIsCancelled(self):
        return self.__isCanceled

    def setIsCancelled(self,isCanceled):
        self.__isCanceled=isCanceled
    
    def getIsAccepted(self):
        return self.__isAccepted

    def setIsAccepted(self,isAccepted):
        self.__isAccepted=isAccepted
    
    #---Removing Employee Registration after Cancelling Request---
    def removeEmpReg(self,registrationId):
        self.__registeredEmp.pop(registrationId)
        if(len(self.getRegEmp())>=self.getMinEmp()):
            self.setIsCancelled(False)
        else:
            self.setIsCancelled(True)

    #---Adding Employee Registration
    def addEmpReg(self,emp):
        registrationId="REG-COURSE-"+emp.getEmpName()+"-"+self.getCourseName()
        self.__registeredEmp[registrationId]=emp
        if len(self.getRegEmp())>=self.getMinEmp():
            self.setIsCancelled(False)
        return registrationId


    

    