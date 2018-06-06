# -*- coding: utf-8 -*-
from ftplib import FTP
import os
import datetime
import time
from time import strftime

class Fuzzy_Match:
    def __init__(self):
        self.ip = '10.199.148.146'
        self.port = 60621
        self.user = 'appjqr'
        self.password = 'eWgLBpxmU6V6'
        self.bufsize = 1024
        self.ftp = FTP()

    def ftp_connect(self):
        try:
            self.ftp.connect(self.ip, self.port)
            self.ftp.login(self.user,self.password)
            self.ftp.encoding = 'utf8'
        except ftplib.error_perm:
            self.ftp_connect()

    def ls(self, path):
        self.ftp.cwd(path)
        ll = self.ftp.nlst()
        self.ftp.cwd('/')
        return ll

    def ftp_download(self, path):
        self.ftp.cwd('/DM/JQR/PLAZA/'+path)
        l = self.ftp.nlst()       
        for i in l:
            file_handle = open('/home/appuser/plaza_match/gc/'+i,"wb")
            self.ftp.retrbinary('RETR '+i, file_handle.write, self.bufsize)
            file_handle.close()

    def ftp_upload(self,path):
        self.ftp.cwd('/DM/JQR/PLAZA/'+path)
        file_handle = open('/home/appuser/plaza_match/Plaza_Match.csv',"rb")
        self.ftp.storbinary('STOR '+'Plaza_Match_'+path+'csv', file_handle, self.bufsize)
        file_handle.close()

if __name__ == '__main__':
    fm = Fuzzy_Match()
    fm.ftp_connect()
    while True:
        a = fm.ls('/DM/JQR/PLAZA/')
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days = 1)
        yesterday = yesterday.strftime('%Y%m%d') 
        if yesterday in a:
            l = fm.ls('/DM/JQR/PLAZA/'+yesterday)
            if ('Plaza_Match.csv' not in l) & (len(l)==8):
                print '\n'+strftime("%Y-%m-%d %H:%M:%S"), 'download starting...'
                fm.ftp_download(yesterday)
                print('download complete, start model')
                os.system('python /home/appuser/plaza_match/plaza_match.py')
                print('model complete,upload starting...')
                fm.ftp_upload(yesterday)
                print strftime("%Y-%m-%d %H:%M:%S"), 'upload complete\n'
            else:
                fm.ftp.quit()
                time.sleep(600)
        else:
            fm.ftp.quit()
            time.sleep(3600)










