from src.courseOfferService import courses
import constant.constants as constants

#---This function allot the courses to the Employee and print details of employee who have registered for the respective course---
def allot(cmd):
    courseOfferingId=cmd[1]

    #---Finding the object corresponding to the given course offering Id---
    for course in courses:
        if courseOfferingId==course.getCourseId():
            targetCourse=course
            break

    allotResult=[]
    
    for regId,emp in sorted(targetCourse.getRegEmp().items()):
        email=emp.getEmail()
        courseName=targetCourse.getCourseName()
        instructor=targetCourse.getInstructor()
        date=targetCourse.getDate()

        if(targetCourse.getIsCancelled()):
            status=constants.COURSE_CANCELED
        else:
            status=constants.CONFIRMED
        
        targetCourse.setIsAccepted(True)
        allotResult.append(list([regId,email,courseOfferingId,courseName,instructor,date,status]))
    return allotResult
