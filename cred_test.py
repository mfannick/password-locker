import unittest
from cred import Cred
####### credential Class##########   
##############################################################
#good instantiation test
class TestClasse2(unittest.TestCase):

    def setUp(self):
        self.newCred=Cred("hangout","anny","aabc@")  
    def test2Init(self):
        self.assertEqual(self.newCred.cForm,"hangout")
        self.assertEqual(self.newCred.cName,"anny")  
        self.assertEqual(self.newCred.cWord,"aabc@")

if __name__ == '__main__':
    unittest.main()     
       