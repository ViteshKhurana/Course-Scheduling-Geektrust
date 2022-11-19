#---Regex Expression Matching for Email validation---
import re
from constant.constants import NO_OF_PARAMETERS, REGEX 
from src.courseOfferService import addCourseOffering
from src.registerService import register
from src.allotService import allot
from src.cancelService import cancel

def validateInputs(cmd):
    lengthOfCmd=len(cmd)

    if cmd[0]=="ADD-COURSE-OFFERING":
        #---Checking whether the cmd has correct no of parameters or not and whether minimum no of employee is less than of maximum no of employee---
        if lengthOfCmd==NO_OF_PARAMETERS["courseOffer"] and int(cmd[4])<=int(cmd[5]):
            print(addCourseOffering(cmd))
            return True

    elif cmd[0]=="REGISTER" and lengthOfCmd==NO_OF_PARAMETERS["register"]:
        email=cmd[1]
        if re.fullmatch(REGEX,email):
            registerResult=register(cmd)
            print(registerResult)
            return True

    elif cmd[0]=="ALLOT" and lengthOfCmd==NO_OF_PARAMETERS["allot"]:
        allotResult=allot(cmd)
        for allot1 in allotResult:
            print(*allot1)
        return True

    elif cmd[0]=="CANCEL" and lengthOfCmd==NO_OF_PARAMETERS["cancel"]:
        print(cancel(cmd))
        return True

    return False
