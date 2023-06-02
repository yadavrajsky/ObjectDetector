import os,cv2
from os import listdir,makedirs
from os.path import isfile,join

def greyImage():
    path = r'C:\\Users\\vikas\\Desktop\\Fabric identification and defect detection\\data' # Source Folder
    dstpath = r'C:\\Users\\vikas\\Desktop\\Fabric identification and defect detection\\modifiedData' # Destination Folder

    try:
        os.makedirs(dstpath)
    except:
        print ("Directory already exist, images will be written in same folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(dstpath,image),gray)

path = r'C:\\Users\\vikas\\Desktop\\Fabric identification and defect detection\\data' # Source Folder
dstpath = r'C:\\Users\\vikas\\Desktop\\Fabric identification and defect detection\\modifiedData' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in asme folder")

# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 

for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))