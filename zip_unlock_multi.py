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

    start = time.time()
    pwdfile = sys.argv[2]
    try:
        f = open(pwdfile,"r")
    except:
        print("\nFile not found")
        quit()
    passes = f.readlines()

    # include facility to mutate words in
    # word list

    if mutate_q.lower() == 'y':

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
    try:
        Zip = sys.argv[1]
        myZip = zipfile.ZipFile(Zip)
    except zipfile.BadZipfile:
        print("[!] There was an error opening your zip file.")
        return

    password = passes.strip()

    try:
        myZip.extractall(pwd = password.encode())
        end = time.time()
        t_time = end - start

        print ("\nPassword cracked: %s\n" % password)
        print ("Total runtime was -- ", t_time, "second")
        time.sleep(10)
        return

    except Exception as e:
        if str(e) == 'Bad password for file':
            pass
        elif 'Error -3 while decompressing' in str(e):
            pass
        else:
            print (e)
    print ("Sorry, Your password not found.")

if __name__ == '__main__':

    pool = mp.Pool(mp.cpu_count())

    to_try = main()

    break_points = []

    for i in range(mp.cpu_count()):
        break_points.append({'start' : math.ceil(len(to_try)/mp.cpu_count() * i),
                            'stop' : math.ceil(len(to_try)/mp.cpu_count() * (i +1))})

    result_objects = []

    for x in break_points:
        print(x)
        result_objects = [pool.apply_async(try_pass,
                                            args=(i)) for i in to_try[x['start']: x['stop']]
                                            ]

        [print(r.get()[1]) for r in result_objects]

    pool.close()
    pool.join()
