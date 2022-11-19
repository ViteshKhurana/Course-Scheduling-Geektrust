from Models.Course import course

#---To keep track of all the course-offer objects---
courses=[]

#---This function Add the details of the course offered in the course class and generate a course offering ID---
def addCourseOffering(cmd):
    courseName=cmd[1]
    instructor=cmd[2]
    date=cmd[3]
    minCapacity=int(cmd[4])
    maxCapacity=int(cmd[5])

    courseOfferingId="OFFERING-"+courseName+"-"+instructor
    courseOfferingObj=course(courseName,instructor,date,minCapacity,maxCapacity,courseOfferingId)
    courses.append(courseOfferingObj)

    return(courseOfferingId)

    
    