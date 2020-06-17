#!/usr/python3

import os
import time
import logging
import  os.path as path

import shutil

__prename = ["https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.38.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.5.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/libksba/libksba-1.4.0.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/ntbtls/ntbtls-0.1.2.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/npth/npth-1.6.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.1.0.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/gpgme/gpgme-1.13.1.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/scute/scute-1.6.0.tar.bz2",
             "https://gnupg.org/ftp/gcrypt/gpa/gpa-0.10.0.tar.bz2"
             ]
def getbasename(s):
    basename = path.basename(s)
    return s.split('/')[-1]

def removetar(s):
    return s[:-8]

def ptlog(s):
    print("!!!      log: ",s)
    print("!!!!!!!!         pause ............ enter to continue")
    time.sleep(1)
def errorhandle(s):
    print("!!!      error: ", s)
    input("!!!!!!!!         pause ............ enter to continue")
    exit(1)
def run(url):
    urlbasename = getbasename(url)
    tarbasename = removetar(urlbasename)

    #enter  home
    os.chdir(os.getenv("HOME"))

    #download file
    if not path.exists(urlbasename):
        status = os.system(r'wget {}'.format(url))
        if status != 0:
            errorhandle("wget error")

    #tar -jxvf
    if not path.exists(tarbasename):
        status = os.system(r'tar -jxf {}'.format(urlbasename))
        if status != 0:
            errorhandle("wget error")

    #enter dir
    os.chdir(tarbasename)

    ##./configure
    status = os.system("./configure")
    if status !=0:
        os.system('make distclean')
        errorhandle("./configure error")

    ##make
        ##afresh
    status = os.system("make")
    if status != 0:
        os.system('make clean')
        errorhandle("make error")

    ##make install
    status = os.system("make install")
    if status != 0:
        os.system('make clean')
        errorhandle("make install error")
if __name__ == '__main__':
    for i in __prename :
        run(i)
        ptlog("down file:" + i + "already ok.")
