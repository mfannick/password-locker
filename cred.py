import random
class Cred:
    
    listCred=[]  # user identity for creating a account
#########################################################################
# instantiation
    def __init__(self,platform,userName,password):
        
        self.cForm=platform
        self.cName=userName
        self.cWord=password

#########################################################################
# saving user credentials
    
    def saveCred(self):
        '''
        saveCred method saves user objects into userCred
        '''
        Cred.listCred.append(self)

#########################################################################
# display user credentials
    @classmethod    
    def displayCred(cls):
        '''
        method that returns the user list
        '''
        return cls.listCred

##############################################################
#userPassword generator
    @classmethod
    def passGenerator(cls):
        '''
        method that returns the a random password
        '''
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = 8
        p =  "".join(random.sample(s,passlen ))
        return p
