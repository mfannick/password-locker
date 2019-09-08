import random


class Cred:

    listCred = []  # user identity for creating a account
#########################################################################
# instantiation
    def __init__(self, platform, userName, password):

        self.cForm = platform
        self.cName = userName
        self.cWord = password

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
# finding the user username
    @classmethod
    def findCredCform(cls, cForm):
        '''
       Method that takes in a number and returns a contact that matches that number.

       Args:
           number: Phone number to search for
       Returns :
           Contact of person that matches the number.
       '''
        for cred in cls.listCred:
            if cred.cForm == cForm:
                return cred.cForm

# ##############################################################
# checking the user username
    @classmethod
    def checkCform(cls, cForm):
        for cred in cls.listCred:
            if cred.cForm == cForm:
                return True
        return False

    def deleteCred(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Cred.listCred.remove(self)
