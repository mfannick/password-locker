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

##############################################################
#saving multiple credentials
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run.
        '''
        Cred.listCred = []

    def testSaveMultiCred(self):
        '''
        testSaveMultiUser test checks if we can save multiple user
        objects to our userList
        '''
        self.newCred.saveCred()
        testCred=Cred("hangout1","anny1","aabc@1")
        testCred.saveCred()
        self.assertEqual(len(Cred.listCred),2)

##############################################################
#displaying credentials
    def testDisplayCred(self):
        '''
        method that returns a list of all user credentials 
        '''
        self.assertEqual(Cred.displayCred(),Cred.listCred)

##############################################################
#userPassword generator
    def testPassWordGenerator(self):
        '''
        method that returns a randpm  password for credentials 
        '''
        self.newCred.passGenerator()
        self.assertEqual(Cred.displayCred(),Cred.listCred)



if __name__ == '__main__':
    unittest.main()     
       



