from PasswordManager import *
import string
from random import randint, shuffle, sample, choices




#####
# • Create a PasswordManager with the name ‘Student’ and the master password ‘FINAL’

password_manager = PasswordManager(name = 'Student', master_pw='FINAL')



#####
# • Add the site ‘www.gmail.com’ with the username ‘a_student’ and a randomly generated
# password using the default settings

password_manager.add_password(site = 'www.gmail.com', username= 'a_student')



#####
# • Add the site ‘www.wm.edu’ with the username ‘WMstudent’ and a randomly generated pass-
# word that has a maximum of 2 special characters and a minimum of 2 upper case characters,
# all other parameters are defaults

password_manager.add_password(site = 'www.wm.edu', username= 'WMstudent', criteria={'max_spec':2, 'min_upper':2})



#####
# • Change the password for ‘www.gmail.com’ to ‘update1235’

password_manager.change_password(site = 'www.gmail.com', new_pass = 'update1235', master_pass='FINAL')



#####
# • Get the site information for ‘www.wm.edu’

password_manager.get_site_info('www.wm.edu')



#####
# • Print out a string representation of the PasswordManager object you made

print(password_manager.__str__())