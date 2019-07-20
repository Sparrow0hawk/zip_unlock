#md5 Cracker
#Author:ManishHacker1
#https://pythonsecret.blogspot.in
#http://krypsec.com
#https://www.facebook.com/ManishHacker1

# import modules we need
import zipfile
import time
import sys
import string

# define the main function
def get_passwords():

    # ask user if they want to mutate items in the wordlist
    mutate_q = input('Use mutate function? y/n ')

    # define the directory to the wordlist file
    pwdfile = sys.argv[2]

    # try/Except section to open the wordlist file
    try:
        f = open(pwdfile,"r")
    except:
        # if file can't be open exit process with message
        print("\nFile not found")
        quit()
    # once file is open read each line into a function as a list
    passes = f.readlines()

    # include facility to mutate words in
    # word list

    # if user input from is y (use lower here to convert whatever)
    # input is to lowercase
    if mutate_q[0].lower() == 'y':

        # instantiate empty list
        # this is where new mutated passwords will go
        new_passes = []

        # for each word in the list from the wordlist file
        for word in passes:

            #for the number of letters in the word
            # range generates a range of length of word
            for idx in range(len(word)):

                # convert the word into a list of each letter
                # in the word eg 'test' -> ['t','e','s','t']
                new_word = list(word)

                # for each letter in basic acii letters
                # upper and lowercase
                for ltr in string.ascii_letters:

                    # change the letter in the list of letters at given index
                    # to letter from ascii characters
                    new_word[idx] = ltr

                    # using join join back together the list of letters into
                    # a string
                    # add that to the empty list of passwords we made earlier
                    new_passes.append(''.join(new_word))

        # after loop has finished add newly created passwords
        # to list of passwords from wordlist
        passes = passes + new_passes

        # this function returns the list of passwords
        return passes

# function for actually trying passwords on zipfile
def try_pass():

    # run the get_passwords function and get a list of passwords
    passes = get_passwords()

    print(passes)
    # for timing start the timer
    start = time.time()

    # try/except block for handling the zip file in python
    try:
        # this just gets 1st command line arguement after .py file
        Zip = sys.argv[1]
        # loads zipfile into python environment
        myZip = zipfile.ZipFile(Zip)
    # error handling if bad file
    except zipfile.BadZipfile:
        print("[!] There was an error opening your zip file.")
        return


    #for each password in the password list
    for pwd in passes:
        # remove any whitespace before or after word
        password = pwd.strip()

        # try/except block for handling trying passwords
        try:
            # using the zipfile extractall command
            # encode here converts password to utf-8
            myZip.extractall(pwd = password.encode())
            # if password works stop timer
            end = time.time()
            # calculate time elasped
            t_time = end - start

            # do some printing of details
            print ("\nPassword cracked: %s\n" % password)
            print ("Total runtime was -- ", t_time, "second")
            time.sleep(3)
            return
        # if extractall fails
        except Exception as e:
            # this slightly complicated if just handles the error message format
            if str(e).split('<')[0].strip() == 'Bad password for file':
                pass
            elif 'Error -3 while decompressing' in str(e).split('<')[0].strip():
                pass
            else:
                print (e)
    # if all passwords attempted then return overall failed to find password
    print ("Sorry, Your password not found.")

# this is python standard for running OOP style scripts
if __name__ == '__main__':

 try_pass()
