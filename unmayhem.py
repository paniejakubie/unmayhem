import os
import errno
import shutil

HOME = os.getenv("HOME")
DOWNLOADS = os.path.join(HOME, 'Downloads')
os.chdir(DOWNLOADS)

CATEGORIES = {
    'archives': ['zip', 'tar', 'gz', 'rar', '7zip'],
    'documents': ['pdf', 'doc', 'xls', 'odt', 'odp', 'ppt', 'txt'],
    'books': ['epub', 'mobi'],
    'images': ['jpg', 'jpeg', 'png', 'bmp', 'gif'],
    'audio': ['mp3', 'wav', 'ogg'],
    'packages': ['deb', 'rpm'],
    'fonts': ['otf', 'ttf'],
    'web-files': ['html', 'css'],
    'torrent': ['torrent'],
    'scripts': ['sh', 'py', 'rb', 'ru'],
}

for d in CATEGORIES.keys():
    try:
        os.makedirs(os.path.join(DOWNLOADS, d))
        print "Created %s directory" % os.path.join(DOWNLOADS, d)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def get_filetype(filename):
    return filename.split('.')[-1]

def move_files(filename):
    filetype = get_filetype(filename)
    
    r = [k for k, v in CATEGORIES.iteritems() if filetype in v]

    if len(r) == 0:
        if os.path.isdir(filename):
            print "%s is directory" % filename
        else:
            return "%s goes to /other" % filename
    else:
        SRC = os.path.realpath(filename)
        DST = os.path.join(DOWNLOADS, r[0])
        shutil.move(SRC, DST)
        return "%s goes to /%s" % (filename, r[0])
    
for f in os.listdir(DOWNLOADS):
    print move_files(f)
