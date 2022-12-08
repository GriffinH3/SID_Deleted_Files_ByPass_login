'''
J.Griffin Harrington
December 17, 2020
Version 1

Script Description:
This script is designed to translate the SID into a more readable output.
SID is a long string our computers use to identfiy the user. This script is also desgined to
show what files have been deleted (more accuractely placed in the recycle bin) and by whom.
The idea behind this script is to help a foresnic investigation easily find files that have been
deleted and to identify who deleted them. 
'''
import os 
import optparse
from winreg import *

'''Sid2User takes in the sid and returns a readable user name or returns the sid back'''
def sid2User(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'+ sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid
'''returnDir is a function that goes through the possible names of the directory that contains the trash bin for
 operating systems that support NTFS, Windows 98, Windows NT, Windows 2000, Windows XP, Windows Vista, and Windows 7'''
def returnDir():
    dirs = ['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None
'''findRecycled takes in the directory for the trash bin and prints the User and which file they have deleted '''
def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2User(sid)
        print('\n[*] Listing Files for Users: '+ str(user))
        for file in files:
            print('\n [+] Found File: '+ str(file))
            
def main():
    recycledDir = returnDir()
    findRecycled(recycledDir)
    
if __name__ == '__main__':
    main()