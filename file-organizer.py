import shutil
import os
import collections

rootFolder = "/home/jedi/Downloads/"
#for root file of folder move files individualy
#for folders do antoher thing(move entire folders based on file paths), ask for confirms
movie = [".mp4", ".avi", ".flv", ".mpeg2", ".ogg"]
picture = [".jpg", ".png"]
music = [".mp3", ".flac"]

movie_dir = "/home/jedi/Videos/"
music_dir = "/home/jedi/Music/"
picture_dir = "/home/jedi/Pictures/"


def organizeRootFolder():
    #get all files
    #for their filetpye put in directory
    fileList = os.listdir(rootFolder)
    files = [name for name in fileList if os.path.isfile(rootFolder + name)]
    for f in files:
        root, ext = os.path.splitext(f)
        if ext in movie:
            move(rootFolder + f, movie_dir)
        if ext in music:
            move(rootFolder + f, music_dir)
        if ext in picture:
            move(rootFolder + f, picture_dir)

def move(f, where):
    print f
    shutil.move(f,where)
    print "moving " +f + " to " + where

def doesContainFolders(f):
    fileList = os.listdir(f)
    dirs  = [name for name in fileList if  os.path.isdir(f + name)]
    if len(dirs) == 0:
        return False
    return True
def get_directory_file_stats(directory):
    #gets a counter tuple of extensions + filesize for a directory
    #goes into all subfolders of directory
    print directory
    fileList = os.listdir(directory)
    files = [name for name in fileList if os.path.isfile(directory + name)]
    directories = [name for name in fileList if  os.path.isdir(directory + name)]
    stats = []
    for f in files:
        #get extension and filesize for each file
        root, ext = os.path.splitext(f)
        fileSize = os.path.getsize(directory + f)
        stats.append((ext, fileSize))
        
    if doesContainFolders(directory):
        #call itself an all folders inside
        print directories
        for childDir in directories:
            stats +=  get_directory_file_stats(directory + childDir + "/")

    return collections.Counter(stats)


def getSubFolders(folder):
    fileList = os.listdir(folder)
    suvfolders = [name for name in fileList if  os.path.isdir(directory + name)]
    return subfolders 
def organizeSubFolders(folder, confirm =True):
    #moves whole subfolders of a folder around based on number of files in subfolders
    #confirm -> ask for confirmation of folder moving
    subFolders = getSubFolders(folder)
    for subFolder in subFolders:
        fileStats = get_directory_file_stats(subfolder)

#print get_directory_file_stats(rootFolder )
#print get_directory_file_stats(rootFolder )
print get_directory_file_stats(rootFolder )
