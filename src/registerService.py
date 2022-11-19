from src.courseOfferService import courses
from Models.Employee import Employee
import constant.constants as constants

def register(cmd):
    email=cmd[1]
    courseOfferingId=cmd[2]
    empObj=Employee(email)
    
    for course in courses:
        if courseOfferingId==course.getCourseId():
            targetCourse=course
            break

    if len(targetCourse.getRegEmp())==targetCourse.getMaxEmp():
        return(constants.COURSE_FULL_ERR)
    else:
        courseRegId=targetCourse.addEmpReg(empObj)
        return(courseRegId+' '+constants.ACCEPTED)

        
    
    