import unittest
import sys
sys.path.append('..\courseScheduling')
from src.courseOfferService import addCourseOffering

class testCourseOffer(unittest.TestCase):
  
    def test_courseOffering1(self):      
        
        cmd=list("ADD-COURSE-OFFERING DB HOLA 19082022 1 5".split())
        self.assertEqual(addCourseOffering(cmd),"OFFERING-DB-HOLA")

