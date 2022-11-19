import unittest
import sys
sys.path.append('..\courseScheduling')
from src.validateInput import validateInputs


class testValidateInput(unittest.TestCase):
  
    def test_validateInput1(self):      

        cmd=list("ADD-COURSE-OFFERING JAVA JAMES 19022023 1 2".split())
        self.assertEqual(validateInputs(cmd),True)
        
        cmd=list("ADD-COURSE-OFFERING PYTHON".split())
        self.assertEqual(validateInputs(cmd),False)
    
    def test_validateInput2(self):      

        cmd=list("ADD-COURSE-OFFERING JAVA BOB 18012023 0 1".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("REGISTER ANDY@GMAIL.COM OFFERING-JAVA-BOB".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("REGISTER JON".split())
        self.assertEqual(validateInputs(cmd),False)

    def test_validateInput3(self):      

        cmd=list("ADD-COURSE-OFFERING DATASCIENCE RAVI 21092022 4 10".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("REGISTER ANDY@GMAIL.COM OFFERING-DATASCIENCE-RAVI".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("ALLOT OFFERING-DATASCIENCE-RAVI".split())
        self.assertEqual(validateInputs(cmd),True)
    
    def test_validateInput4(self):      

        cmd=list("ADD-COURSE-OFFERING DSA BABBAR 18022022 2 4".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("REGISTER ANDY@GMAIL.COM OFFERING-DSA-BABBAR".split())
        self.assertEqual(validateInputs(cmd),True)

        cmd=list("CANCEL REG-COURSE-ANDY-DSA".split())
        self.assertEqual(validateInputs(cmd),True)


    




