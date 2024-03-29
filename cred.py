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
        saveCred method saves credential objects into userCred
        '''
        Cred.listCred.append(self)

#########################################################################
# display user credentials
    @classmethod    
    def displayCred(cls):
        '''
        method that returns the credential list
        '''
        return cls.listCred

##############################################################
#finding the user username
    @classmethod
    def findCredCform(cls, cForm):
         '''
        Method that takes in a platform name and returns a credential that matches that platform.

        Args:
             platform to search for
        Returns :
            Credential that matches the platform.
        '''
         for Cred in cls.listCred:
            if Cred.cForm == cForm:
                return Cred

# ##############################################################
#checking the user username
    @classmethod
    def checkCform(cls, cForm):
        for cred in cls.listCred:
            if cred.cForm == cForm:
                return True
        return False

    def deleteCred(self):
        '''
        deletecred method deletes a saved contact from the credential list
        '''

        Cred.listCred.remove(self)
