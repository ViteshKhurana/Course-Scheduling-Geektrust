import unittest
import sys
sys.path.append('..\courseScheduling')
from src.courseOfferService import addCourseOffering
from src.registerService import register
from src.allotService import allot
from src.cancelService import cancel
from constant.constants import CANCEL_REJECTED,CANCEL_ACCEPTED

class testRegister(unittest.TestCase):
  
    def test_register1(self):      
        
        cmd=list("ADD-COURSE-OFFERING TREE ADITYA 01072021 3 6".split())
        addCourseOffering(cmd)
        
        cmd=list("REGISTER ROHIT@GMAIL.COM OFFERING-TREE-ADITYA".split())
        register(cmd)

        cmd=list("ALLOT OFFERING-TREE-ADITYA".split())
        allot(cmd)

        cmd=list("CANCEL REG-COURSE-ROHIT-TREE".split())
        self.assertEqual(cancel(cmd),"REG-COURSE-ROHIT-TREE "+CANCEL_REJECTED)

    def test_register2(self):      
        
        cmd=list("ADD-COURSE-OFFERING ALGO ADITYA 01072021 3 6".split())
        addCourseOffering(cmd)
        
        cmd=list("REGISTER ROHIT@GMAIL.COM OFFERING-ALGO-ADITYA".split())
        register(cmd)

        cmd=list("CANCEL REG-COURSE-ROHIT-ALGO".split())
        self.assertEqual(cancel(cmd),"REG-COURSE-ROHIT-ALGO "+CANCEL_ACCEPTED)

    