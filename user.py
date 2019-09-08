class User:
    """
    Class that generates new instances of user identify for creating an account in the app
    """
    listUser = []  # user identity for creating a account
#########################################################################
# instantiation
    def __init__(self, firstName, lastName, userName, passWord):

        self.fname = firstName
        self.lname = lastName
        self.uname = userName
        self.pword = passWord

#########################################################################
# saving user identity

    def saveUser(self):
        '''
        saveUser method saves user objects into userList
        '''
        User.listUser.append(self)
##############################################################
# display useridentities
    @classmethod
    def displayUser(cls):
        '''
        method that returns the user list
        '''
        return cls.listUser

# ##############################################################
# saving multiple times
    @classmethod
    def findByUserName(cls, uname):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
        number: userName to search for
        Returns :
        Identity of person that matches the userName.
        '''
        for user in cls.listUser:
            if user.uname == uname:
                return user

# ##############################################################
#finding the user username
    @classmethod
    def findUserUname(cls, uname):
         '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
         for user in cls.listUser:
            if user.uname == uname:
                return user.uname

# ##############################################################
#checking the user username
    @classmethod
    def checkUname(cls, uname):
        for user in cls.listUser:
            if user.uname == uname:
                return True
        return False
# ##############################################################
#finding the user password
    @classmethod
    def findUserPword(cls,pword):
         '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
         for user in cls.listUser:
            if user.pword == pword:
                return user.pword

# ##############################################################
#checking the user password
    @classmethod
    def checkPWord(cls, pword):
        for user in cls.listUser:
            if user.pword == pword:
                return True
        return False
# ################# login
# #finding the user username
#     @classmethod
#     def findUserUnamelog(cls, username):
#          '''
#         Method that takes in a number and returns a contact that matches that number.

#         Args:
#             number: Phone number to search for
#         Returns :
#             Contact of person that matches the number.
#         '''
#          for user in cls.listUser:
#             if User.listUser[username] == user.username:
#                 return User.listUser[username]

# # ##############################################################
# #checking the user username match for login
#     @classmethod
#     def checkUnamelog(cls, username):
#         for user in cls.listUser:
#             if User.listUser[username] == user.userName:
#                 return True
#         return False
#         #   for user in cls.listUser:
#         #     if user.username == User.listUser[username]:
#         #         return True
#         # return False
       

        
