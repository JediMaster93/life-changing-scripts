import shutil
import os
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
    files = [name for name in fileList if not os.path.isfile(f + name)]
    if len(files) == 0:
        return False
    return True
def get_directory_file_stats(directory):
    fileList = os.listdir(directory)
    files = [name for name in fileList if os.path.isfile(rootFolder + name)]
    directories = [name for name in fileList if not os.path.isfile(rootFolder + name)]
    stats = []
    for f in files:
        root, ext = os.path.splitext(f)
        stats += ext

    if doesContainFolders(directory):
        for childDir in directories:
           stats +=  get_directory_file_stats(directory + childDir + "/")

    return stats

print get_directory_file_stats(rootFolder )
