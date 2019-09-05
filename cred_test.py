import unittest
from cred import Cred
####### credential Class##########   
##############################################################
#good instantiation test
class TestClasse2(unittest.TestCase):

    def setUp(self):
        self.newCred=Cred("hangout","anny","aabc@")
        '''
        test_init test case to test if the object is initialized properly
        '''  
    def test2Init(self):
        self.assertEqual(self.newCred.cForm,"hangout")
        self.assertEqual(self.newCred.cName,"anny")  
        self.assertEqual(self.newCred.cWord,"aabc@")

##############################################################
#saving credentials
    def testSaveCred(self):
        '''
        testSaveUser test case to test if the user object is saved into
        the user list
        ''' 
        self.newCred.saveCred()
        self.assertEqual(len(Cred.listCred),1)
if __name__ == '__main__':
    unittest.main()     
       