import unittest
from user import User


class TestClasses(unittest.TestCase):

    pass
    '''
    Test class that defines test cases for the user and credential classes behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
####### UserClass##########    
##############################################################
#good instantiation test
    def setUp(self):

        self.newUser= User("Annick","Francine","mfannick","anny12")
    
    def testInit(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.newUser.fname,"Annick")
        self.assertEqual(self.newUser.lname,"Francine")
        self.assertEqual(self.newUser.uname,"mfannick")
        self.assertEqual(self.newUser.pword,"anny12")

##############################################################
#saving test
    def testSaveUser(self):
        '''
        testSaveUser test case to test if the user object is saved into
        the user list
        '''
        self.newUser.saveUser()#saving the new user identity
        self.assertEqual(len(User.userList),1)
# ##############################################################
#display user identity 
    def testDisplayUser(self):
        '''
        method that returns a list of all user identities 
        '''
        self.assertEqual(User.displayUser(),User.userList)

# ##############################################################
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that cleans up after each test case has run.
            '''
            User.userList = []
#saving multiple times
    def testSaveMultiUser(self):
        '''
        testSaveMultiUser test checks if we can save multiple user
        objects to our userList
        ''' 
        self.newUser.saveUser()
        testUser= User("Annick1","Francine1","mfannick1","anny121")
        testUser.saveUser()
        self.assertEqual(len(User.userList),2) 

        

# ##############################################################
#searching user identity  
    def testFindUserByUserName(self):
        self.newUser.saveUser()
        testUser=User("Annick1","Francine1","mfannick1","anny121")
        testUser.saveUser()
        found_user= User.findByUserName("mfannick1")
        self.assertEqual(found_user.fname,testUser.fname)
       
if __name__ == '__main__':
    unittest.main() 



