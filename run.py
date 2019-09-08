#!/usr/bin/env python3.6
from user import User
from cred import Cred
import random
#####################User identinty############################

#Create function
def createUser(fname,lname,uname,pword):

    '''
    Function to create a new user
    '''

    newUser=User(fname,lname,uname,pword)
    return newUser
#save function
def saveUser(user):
    '''
    Function to save user identity
    '''
    user.saveUser()
    #username
def findByUserName(uname):
    '''
    Function for finding the user using the username
    '''
    User.findByUserName(uname)

def checkByUname(uname):
    '''
    Function for checking user password
    '''
    User.checkUname(uname)
def findUserByUname(uname):
    '''
    Function for finding user password
    '''
    return User.findUserUname(uname)
#passoword
def checkByPWord(pword):
    '''
    Function for checking user password
    '''
    User.checkUname(pword)
def findUserByPword(pword):
    '''
    Function for finding user password
    '''
    return User.findUserPword(pword)
#################################################credentials
#Create function
def createUserCred(cForm,cName,cWord):

    '''
    Function to create a new user
    '''

    newCred=Cred(cForm,cName,cWord)
    return newCred
#save function
def saveCred(cred):
    '''
    Function to save user identity
    '''
    cred.saveCred()
# Displaying all credentials
def displayCreds():
    '''
    Function that returns all the saved contacts
    '''
    return Cred.displayCred()
# #userPassword generator
# def passGeneratorlog():

#     return Cred.passGenerator()
def checkByCform(cForm):
    '''
    Function for checking user password
    '''
    Cred.checkCform(cForm)
def findUserByCform(cForm):
    '''
    Function for finding user password
    '''
    return Cred.findCredCform(cForm)




##################### main function user function############################
def main():
    print('welcome to password locker app')
    while True:
        print("Use these short codes : cc - create an account, lg - login in your account")# choosing one of the short codes
        shortCode=input()
        if shortCode=='cc':
            #inputing user details
            print('we will need your firstname,lastname,the username you will use and the pasword ')
            print('\n')
            print('Hello what\'s your firstname')
            fname=input()
            print(f'{fname} what\'s your lastname')
            lname=input()
            print(f'{fname} write your username')
            uname=input()
            if findUserByUname(uname):
                searchUname=findUserByUname(uname)
                print(f'{searchUname} already exist use another username')
                continue
            else:
                print('your password')
                pword=input()
            #checking user password
                if findUserByPword(pword):
                    searchPword=findUserByPword(pword)
                    print(f'{searchPword} already exist use another password')
                
                
                    print('\n')
                    print(f'{fname} {lname} welcome to password locker app')

                    saveUser(createUser(fname,lname,uname,pword))
                    print('********Account successfully created**********')
                    print(f'{fname} {lname} here is your generate username:{uname} and password:{pword}')
#################################################### login
        elif shortCode=='lg':
            
            print('please enter your username')
            username=input()
            if username!=uname:
                continue
            else:
                print('please enter your password')
                password=input()
                if password!=pword:
                    continue
                else:
################################################################# credentials
                    print('***************************Credentials****************************************')
                    while True:
                            print('Use these short codes : add - add a platform, dis - display credentials cp - create a platfrom , del - delete a platform, ex -exit the credentials, del - Delete one credential')
                            shortCode1=input()
                            if shortCode1=='add':
                                print('Enter the platform name......')
                                cForm=input()
                                print('Enter the platform username.........')
                                cName=input()
                                print('Enter the platform password...........')
                                cWord=input()
                                saveCred(createUserCred(cForm,cName,cWord))
                                print('********Successfully saved**********')
                            elif shortCode1=='dis':
                                if displayCreds():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for cred in displayCreds():
                                        print(f"{cred.cForm}")
                                        print(f"{cred.cName}")
                                        print(f"{cred.cWord}")
                                else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                            elif shortCode1=='cp':
                                print('Enter the platform name......')
                                cForm=input()
                                print('Enter the platform username.........')
                                cName=input()
                                print('Choose:gen - generate for me a password, mine - my password ')
                                gener=input()
                                if gener=='gen':
                                # cWord1=Cred.passGeneratorlog()
                                    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                                    passlen = 8
                                    p =  "".join(random.sample(s,passlen ))
                                    cWord=p
                                    print(f'your password:{cWord}')
                                else:
                                    print('Enter the platform password...........')
                                    cWord=input()
                                    saveCred(createUserCred(cForm,cName,cWord))
                                    print('********Successfully saved**********')
                            elif shortCode1 == 'del':
                                print('enter the username of the platform you want to delete')
                                platF = input()
                                if checkByCform(platF):
                                    search_platF = findUserByCform(platF)
                                    for cred in displayCreds():
                                         print(f"{search_platF.cName}, {search_platF.cWord}")
                                         y="yes"
                                         print('do u realy want to delete it yes - yes.no - no')
                                         inputs=input()
                                         if(inputs==y):
                                             search_platF.deleteCred()
                                         else:
                                             pass
                            elif shortCode1 == "ex":
                                print("logged out")
                                break
                            else:
                                print("Please use the right short codes")
################################################################ 


if __name__ == '__main__':

    main()

        
    
    
    