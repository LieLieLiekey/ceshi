#!/usr/python3

import os
import time
import logging
import  os.path as path

import shutil

PREURL_LIST = ["https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.38.tar.bz2",
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
    logging.info(s)
    time.sleep(1)
def errorhandle(s):
    print("!!!!!    error",s)
    exit(1)
def executecommand(cmd,url=""):
    logging.info("execute "+cmd)
    status = os.system(cmd)
    if status != 0:
        logging.error(" cmd:"+cmd+"url:"+url )
        errorhandle(" cmd:"+cmd+"url:"+url )
def run(url):
    urlbasename = getbasename(url)
    tarbasename = removetar(urlbasename)

    #enter  home
    logging.info("execute cd ~")
    os.chdir(os.getenv("HOME"))

    #download file
    if not path.exists(urlbasename):
        executecommand(r'wget {}'.format(url),url)

    #tar -jxvf
    if not path.exists(tarbasename):
        executecommand(r'tar -jxf {}'.format(urlbasename),url)

    #enter dir
    logging.info("execute cd "+tarbasename)
    os.chdir(tarbasename)

    ##./configure
    executecommand("./configure",url)

    ##make
    executecommand("make",url)

    ##make install
    executecommand("make install",url)

if __name__ == '__main__':
    logging.basicConfig(filename= "autopgp.log",level=logging.DEBUG)
    for i in PREURL_LIST :
        run(i)
        logging.info("down file:" + i + "already ok.")
