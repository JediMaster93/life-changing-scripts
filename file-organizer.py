'''
Script that organizes my ~./Downloads 
Moves files and folders into Music, Pictures and Videos

'''

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

def move(f, where, confirm = False):
    userInput = None
    while userInput not in ("y", "n"):
        print "moving " +f + " to " + where
        print "confirm y/n ?"
        userInput = raw_input() 
    if userInput is "y":
        shutil.move(f,where)


def doesContainFolders(f):
    fileList = os.listdir(f)
    dirs  = [name for name in fileList if  os.path.isdir(f + name)]
    if len(dirs) == 0:
        return False
    return True
def get_directory_file_stats(directory):
    #gets a counter dictionary of extension :  filesize for a directory
    #goes into all subfolders of directory

    #Counter object is needed in order to merge dictionaries together when they come out of recursion
    #ie. {a:1, b:1} + {a:1, b:2} == {a:2, b:3} would not work if not for the counter object.
    
    fileList = os.listdir(directory)
    files = [name for name in fileList if os.path.isfile(directory + name)]
    directories = [name for name in fileList if  os.path.isdir(directory + name)]

    stats = collections.Counter({})
    for f in files:
        #get extension and filesize for each file root, ext = os.path.splitext(f)
        root, ext = os.path.splitext(directory  + f)
        fileSize = os.path.getsize(directory + f)
        #update dictionary
        stats[ext] += fileSize
        
    if doesContainFolders(directory):
        #call itself an all folders inside
        for childDir in directories:
            stats +=  get_directory_file_stats(directory + childDir + "/")

    return stats


def getSubFolders(folder):
    fileList = os.listdir(folder)
    subfolders = [name for name in fileList if  os.path.isdir(folder + name)]
    return subfolders 
def organizeSubFolders(folder, confirm =True):
    #moves whole subfolders of a folder around based on number of files in subfolders
    #confirm -> ask for confirmation of folder moving
    subFolders = getSubFolders(folder)
    for subfolder in subFolders:
        #format subfolder to have a forwardSlash (everymethod expects a folder with a forwardslash
        #get filestats for earch subolder -> Counter dictionary object
        #get most common fileStats  -> array of tuples ("ext", bytes) sorted by bytes
        #get most common extension for each list -> one tuple, eg (".mp3", 1024)

        subfolder = subfolder + "/"
        fileStats = get_directory_file_stats(folder + subfolder )
        fileStats = fileStats.most_common()
        mostCommonExt = fileStats[0]
        print subfolder, "  ", fileStats
        if mostCommonExt[0] in movie:
            move(folder + subfolder, movie_dir,confirm)
        if mostCommonExt[0] in music:
            move(folder + subfolder, music_dir,confirm)
        if mostCommonExt[0] in picture:
            move(folder + subfolder, picture_dir, confirm)


#print get_directory_file_stats(rootFolder )
#print get_directory_file_stats(rootFolder )
organizeSubFolders(rootFolder)
