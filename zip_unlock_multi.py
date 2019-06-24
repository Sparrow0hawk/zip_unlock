#md5 Cracker
#Author:ManishHacker1
#https://pythonsecret.blogspot.in
#http://krypsec.com
#https://www.facebook.com/ManishHacker1

import zipfile
import time
import sys
import string
import multiprocessing as mp
import math

def main():

    mutate_q = input('Use mutate function? ')

    password = ''

    pwdfile = sys.argv[2]
    try:
        f = open(pwdfile,"r")
    except:
        print("\nFile not found")
        quit()
    passes = f.readlines()

    # include facility to mutate words in
    # word list

    if mutate_q[0].lower() == 'y':

        new_passes = []

        for word in passes:

            for idx in range(len(word)):

                new_word = list(word)

                for ltr in string.ascii_letters:

                    new_word[idx] = ltr

                    new_passes.append(''.join(new_word))

        passes = passes + new_passes

        return passes

def try_pass(passes=None):

    start = time.time()

    password = passes.strip()

    try:
        Zip = sys.argv[1]
        myZip = zipfile.ZipFile(Zip)
    except zipfile.BadZipfile:
        print("[!] There was an error opening your zip file.")
        return

    # multiprocessing takes iterable that is passed
    # to function so this section isn't required
    #for pass_count, x in enumerate(passes):
    #    password = x.strip()
    #    print(password)

    try:
        myZip.extractall(pwd = password.encode())
        end = time.time()
        t_time = end - start

        print ("\nPassword cracked: %s\n" % password)
        print ("Total runtime was -- ", t_time, "second")
        time.sleep(3)
        pool.close()
        pool.terminate()
        pool.join()
        return
    except Exception as e:
        if str(e).split('<')[0].strip() == 'Bad password for file':
            pass
        elif 'Error -3 while decompressing' in str(e).split('<')[0].strip():
            pass
        else:
            print (e)
    print ("Sorry, Your password not found.")

if __name__ == '__main__':

    pool = mp.Pool(mp.cpu_count())

    to_try = main()

    break_points = []

    for i in range(mp.cpu_count()):
        break_points.append({'start' : math.ceil(len(to_try)/mp.cpu_count() * i),'stop' : math.ceil(len(to_try)/mp.cpu_count() * (i +1))})

    for point in break_points:
        print(point['start'],' ',point['stop'])
        pool.map(try_pass, to_try[point['start']:point['stop']])

    pool.close()
    pool.join()
