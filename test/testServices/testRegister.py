import unittest
import sys
from Models.Course import course
sys.path.append('..\courseScheduling')
from src.courseOfferService import addCourseOffering
from src.registerService import register
from constant.constants import COURSE_FULL_ERR

class testRegister(unittest.TestCase):
  
    def test_register1(self):      
        
        cmd=list("ADD-COURSE-OFFERING DP STRIVER 19082022 1 5".split())
        addCourseOffering(cmd)
        
        cmd=list("REGISTER VIRAT@GMAIL.COM OFFERING-DP-STRIVER".split())
        self.assertEqual(register(cmd),"REG-COURSE-VIRAT-DP ACCEPTED")
    
    def test_register2(self):      
        
        cmd=list("ADD-COURSE-OFFERING GRAPH ADITYA 01072021 0 1".split())
        addCourseOffering(cmd)
        
        cmd=list("REGISTER VIRAT@GMAIL.COM OFFERING-GRAPH-ADITYA".split())
        register(cmd)
        
        cmd=list("REGISTER ROHIT@GMAIL.COM OFFERING-GRAPH-ADITYA".split())
        self.assertEqual(register(cmd),COURSE_FULL_ERR)

    
