import firebase_admin
from firebase_admin import db,credentials
from firebase_admin import firestore
import datetime
import win32api
import time
import pywinauto
import psutil


# Fetch the service account key file from the Firebase project settings
cred = credentials.Certificate('credential.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {"databaseURL": "https://storeactions-bdf68-default-rtdb.firebaseio.com/"})

ref = db.reference("/")

# Get a reference to the Firestore database
# print(ref.get())
# db.reference("/").update({"language": "python"})

#To store browser information
db.reference("/Sindhura").update({"browser": ''})
desktop = pywinauto.Desktop(backend="uia")
window = desktop.windows(title_re=".* Google Chrome", control_type="Pane")[0]
wrapper_list = window.descendants(control_type="TabItem")
for wrapper in wrapper_list:
    x=str(wrapper)
    y=x.strip('uiawrapper.UIAWrapper - ')
    db.reference("Sindhura/browser").push().set(y.strip(",TabItem"))

#to store number of process runnimg
def get_process():
    pross=0
    for process in psutil.process_iter(['pid', 'name']):
        pross+=1
    return pross
prosss=get_process()
db.reference("/Sindhura").update({"process": prosss})


currtime = datetime.datetime.now()
#To store the mouse and keyboard events
start_time = time.time()
duration = 20
count=0
countal=0
while time.time() - start_time < duration:
    ml=win32api.GetKeyState(0x01) ##mouse left
    mr=win32api.GetKeyState(0x02) #mouse right
    a=win32api.GetKeyState(0x41) #a in keyboard
    b=win32api.GetKeyState(0x41) #b in keyboard
    c=win32api.GetKeyState(0x41) #c in keyboard
    d=win32api.GetKeyState(0x41) #d in keyboard
    e=win32api.GetKeyState(0x41) #e in keyboard
    f=win32api.GetKeyState(0x41) #f in keyboard
    g=win32api.GetKeyState(0x41) #g in keyboard
    h=win32api.GetKeyState(0x41) #h in keyboard
    i=win32api.GetKeyState(0x41) #i in keyboard
    j=win32api.GetKeyState(0x41) #j in keyboard
    k=win32api.GetKeyState(0x41) #k in keyboard
    l=win32api.GetKeyState(0x41) #l in keyboard
    m=win32api.GetKeyState(0x41) #m in keyboard
    n=win32api.GetKeyState(0x41) #n in keyboard
    o=win32api.GetKeyState(0x41) #o in keyboard
    p=win32api.GetKeyState(0x41) #p in keyboard
    q=win32api.GetKeyState(0x41) #q in keyboard
    r=win32api.GetKeyState(0x41) #r in keyboard
    s=win32api.GetKeyState(0x41) #s in keyboard
    t=win32api.GetKeyState(0x41) #t in keyboard
    u=win32api.GetKeyState(0x41) #u in keyboard
    v=win32api.GetKeyState(0x41) #v in keyboard
    w=win32api.GetKeyState(0x41) #w in keyboard
    x=win32api.GetKeyState(0x41) #x in keyboard
    y=win32api.GetKeyState(0x41) #y in keyboard
    z=win32api.GetKeyState(0x41) #z in keyboard
    
    time.sleep(0.1)

    if(a<-10 or b<-10 or c<-10 or d<-10 or e<-10 or f<-10 or g<-10 or h<-10 or i<-10 or j<-10 or k<-10 or l<-10 or m<-10 or n<-10 or o<-10 or p<-10 or q<-10 or r<-10 or s<-10 or t<-10 or u<-10 or v<-10 or w<-10 or x<-10 or y<-10 or z<-10):
        countal+=1
    if(ml<-10 or mr<-10):
        count=count+1

db.reference("/Sindhura").update({"time": str(currtime)})
db.reference("/Sindhura").update({"keyboardkey": countal})
db.reference("/Sindhura").update({"mousekey": count})




