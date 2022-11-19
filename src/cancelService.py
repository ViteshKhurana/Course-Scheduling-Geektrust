from src.courseOfferService import courses
import constant.constants as constants

#---This function takes the cancellation request and check whether cancellation request can be processed or not---
def cancel(cmd):
    courseRegId=cmd[1]
    courseName=courseRegId.split('-')[-1]

    for course in courses:
        if(course.getCourseName()==courseName):
            targetCourse=course
            break
    
    cancelStatus=courseRegId+' '

    if targetCourse.getIsAccepted():
        cancelStatus+=constants.CANCEL_REJECTED
    else:
        targetCourse.removeEmpReg(courseRegId)
        cancelStatus+=constants.CANCEL_ACCEPTED
    return cancelStatus
        
    
