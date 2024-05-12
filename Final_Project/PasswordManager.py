import random
import string
from random import randint, shuffle, sample, choices
import pandas as pd



class PasswordManager:



    def __init__(self, name, master_pw):
        self.__passwords = pd.DataFrame(columns = ['Site', 'Username', 'Password']).set_index('Site') # password dataframe
        self.__name = name #store name of the user
        self.__master_pw = master_pw #store master password



    def __password_specs(self, length = 14, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
        
        # Gets the leftovers and calculates the number of special characters based on 2 conditions
        leftovers = length - min_num - min_upper
        if max_spec == 0 or leftovers <= max_spec:
            num_sc = randint(min_spec, leftovers)
        elif leftovers > max_spec:
            num_sc = randint(min_spec, max_spec)

        # Gets the number of numbers, number of uppercase letters, number of lowercase letters and 
        # returns them along with the number of special characters in a list
        num_num = randint(min_num, length - num_sc - min_upper)
        num_upper = randint(min_upper, length - num_sc - num_num)
        num_lower = length - (num_sc + num_num + num_upper)
        return [num_sc, num_num, num_upper, num_lower]



    def __password_gen(self, criteria = None,length = 14, spec_char = '@!&', repeat = True, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):

        #Checks if criteria contains information, if so, uses that the update the parameters  
            if criteria != None:
                for key in criteria.keys():
                    
                    if key == 'length':
                        length = criteria['length']

                    if key == 'spec_char':
                        spec_char = criteria['spec_char']

                    if key == 'repeat':
                        repeat = criteria['repeat']

                    if key == 'min_spec':
                        min_spec = criteria['min_spec']

                    if key == 'max_spec':
                        max_spec = criteria['max_spec']

                    if key == 'min_num':
                        min_num = criteria['min_num']

                    if key == 'min_upper':
                        min_upper = criteria['min_upper']

        # Some error checking
            if(max_spec < min_spec):
                max_spec = min_spec
            
        # If no repetition and the length of special characters is less than the minimum
        # amount of special characters needed, then it returns None and exits the function
            if repeat == False:
                if ((len(spec_char)) < (min_spec)):
                    return None
                

        # Generates random characters based on the previous specifications and returns those 
        # characters joined in a string
            required = sum([min_spec, min_num, min_upper])
            if required <= length and (repeat or len(spec_char)>=min_spec):
                specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
                if(repeat):
                    password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase, k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
                else:
                    while specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase) or specs[3] > len(string.ascii_lowercase):
                        specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
                    password = random.sample(string.ascii_lowercase, k=specs[3]) + random.sample(string.ascii_uppercase, k=specs[2]) + random.sample(string.digits, k=specs[1]) + random.sample(spec_char, k=specs[0])
                shuffle(password)
                return ''.join(password)
            else:
                return None



    def add_password(self, site, username, criteria = None):

        #generate a new password according to criteria
        new_password = self.__password_gen(criteria)

        #if site is not already in the df is True
        #adds the site, username and password to the df
        if site not in self.__passwords.index:
            if new_password != None:
                self.__passwords.loc[site] = [username, new_password]

        #otherwise, prints an error message for password generated with invalid specifications
            else:
                print('Invalid Specifications')



    def validate(self, mp):
        #Checks whether mp is the same as the master password
        #Returns a boolean
        return mp == self.__master_pw



    def change_password(self, site, master_pass, new_pass = None, criteria = None):
        #If master_password entered correctly
        #If site is present in the df
        #Updates the password to the site
        #This will be new_pass if provided, otherwise, will generate a
        #New password using criteria and store it in the collection of passwords

        #If master password is wrong, print an error message
        if self.validate(master_pass) == False:  # Checks if the master password input is correct
            print('Incorrect master password!')
            return False
        
        #If site does not exist, prints error message
        elif site not in self.__passwords.index:  # Checks if the site is in the dataframe
            # print(self.__passwords)
            # print('the indexes are: ', self.__passwords.index)
            print('Site does not exist!')
            return False
            
        elif new_pass == None:  # if there is no new_pass specified
            print(self.__passwords.at[site, 'Password'])
            print(self.__passwords)
            new_pass = self.__password_gen(criteria)  # creates a new one
            if new_pass == self.__passwords.at[site, 'Password']:  # If this newly generated password is the same as the old one
                print('Invalid criteria!')  # prints 'Invalid criteria!'
                return False  # then returns and exits
            
        # switches the old password with new_pass
        self.__passwords.at[site, 'Password'] = new_pass  



    def remove_site(self, site):
        #Delete a site and the associated data
        if site in self.__passwords.index:
            self.__passwords = self.__passwords.drop(site)



    def get_site_info(self, site):
        #Return a list of username and password for the site passed in as the argument
        if site in self.__passwords.index:
            return [self.__passwords.at[site, 'Username'], self.__passwords.at[site, 'Password']]



    def get_name(self):
        #Return the name of the owner of the password manager
        return self.__name



    def get_site_list(self):
        #Return a list of all the sites (just the sites, not the passwords)
        return list(self.__passwords.index)



    def __str__(self):
        #Return a string representation of ONLY the sites like so:
        #Sites stored for NAME_OF_OWNER
        #www.google.com
        #www.facebook.com
        #www.turtlesareawesome.org
        #One site per line with the header line
        site_collection = ''
        for i in self.get_site_list():
            site_collection += '\n' + i
        return 'Sites stored for '+ self.__name + site_collection
