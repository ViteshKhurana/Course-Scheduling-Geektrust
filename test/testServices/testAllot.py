import unittest
import sys
sys.path.append('..\courseScheduling')
from src.courseOfferService import addCourseOffering
from src.registerService import register
from src.allotService import allot
from constant.constants import ALLOT_CANCEL_RESPONSE,ALLOT_CONFIRMATION_RESPONSE

class testRegister(unittest.TestCase):
  
    def test_register1(self):      
        
        cmd=list("ADD-COURSE-OFFERING DP STRIVER 19082022 1 5".split())
        addCourseOffering(cmd)
        
        cmd=list("REGISTER VIRAT@GMAIL.COM OFFERING-DP-STRIVER".split())
        register(cmd)

        cmd=list("ALLOT OFFERING-DP-STRIVER".split())
        self.assertEqual(allot(cmd),ALLOT_CONFIRMATION_RESPONSE)




    
