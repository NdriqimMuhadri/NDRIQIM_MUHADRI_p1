from socket import *
from builtins import int
import random,datetime,cmath
from _thread import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('Serveri u startua ne localhost:'+str(serverPort))
serverSocket.listen(5)
print('Serveri eshte i gatshem te pranoj kerkesa')
print("------------------------------------------")

def IPADDR (addr):    #IPadresa
    return str(addr[0])

def NUMRIIPORTIT(addr):#Nr i portit
    return str(addr[1])

def EMRIIKOMPJUTERIT():#Hosti
    try:
        hostNAME=gethostname()#E merr IP e hostit edhe e run ne hostName
        return str(hostNAME)
    except socket.error as e:    #Nese ndodh ndonje error socket.error e permban dhe e ruan ne e
        return "Emri i hostit nuk gjet"
     
def KOHA(): #Hosti dhe Koha
    return str(datetime.datetime.now())

def BASHKETINGELLORE (teksti):
    BASHKETINGELLORE = ['B','C','Ç','D','Dh','F','G','Gj','H','J','K','L','Ll','M','N','Nj','P','Q','R','Rr','S','Sh','T','Th','V','X','Xh','Z','Zh'
                         'b','c','ç','d','dh','f','g','gj','h','j','k','l','ll','m','n','nj','p','q','r','rr','s','sh','t','th','v','x','xh','z','zh']
    num=0
    for i in str(teksti):
        if i in BASHKETINGELLORE:
            num+=1
    return str(num) #Bashketinglloret

def PRINTIMI(text):
    text=str(text).strip()
    return str(text) #Printimi

def LOJA():
    num=[]
    for x in range(8):
        num.append(random.randint( 1,49))
    var=str(num)
    return var #Loja

def FIBONACCI(nr):
    vlera1=1
    vlera2=0
    try:
        validimi=int(nr)
    except:
        return "Numri duhet te jete integjer"
    if(validimi<=0):
        return "Numri nuk duhet te jete negativ"
    for i in range(validimi-1):
        vlera1=vlera1+vlera2
        vlera2=vlera1-vlera2
    return str(vlera1) #Fibonacci

def KONVERTIMI(lloji,vlera):
        if(lloji=="KilowattToHorsepower"): #Konvertimi i fuqisë së kilovat ne kuaj-fuqi është dhënë nga:P(hp) = P(kW) / 0.745699872
            return float(vlera/0.745699872)
        elif(lloji=="HorsepowerToKilowatt"): #Konvertimi i fuqisë së kuaj-fuqi në kilovat është dhënë nga:P (kW) = 0.745699872 ⋅ P (hp)
            return float(vlera*0.745699872)
        elif(lloji=="DegreesToRadians"):
            return float((vlera*3.14159265)/180)
        elif(lloji=="RDILadiansToDegrees"):
            return float(vlera*180/3.14159265)
        elif(lloji=="GallonsToLiters"):
            return float(vlera*0.264172052)
        elif(lloji=="LitersToGallons"):
            return float(vlera*3.785412)
        else:
            return "Gabim"
    #METODA SHTESE 1 
def SHUMAENUMRAVEQIFT(m):
   if(m<0):
       print("Sheno nje numer pozitiv")
   else:
       shuma=0
       while(m!=0):
           if(m%2==0):
               shuma+=m
           
           m-=1
   return str(shuma)
#METODA SHTESE 2
def EKKUADRATIK(a,b,c):
    d=(b**2)-(4*a*c)
    zgj1=(-b-cmath.sqrt(d))/(2*a)
    zgj2=(-b+cmath.sqrt(d))/(2*a)
    pergjigje="zgjidhja e pare:",zgj1,"zgjidhja e dyte:",zgj2
    return str(pergjigje)

def thredi(connectionSocket):

    while 1:
       
        print('Klienti u lidh ne serverin %s me port %s' % addr)
        fjalia=(bytes)("string".encode())
        try:

            while str(fjalia.decode())!="":
                try:

                     fjalia = connectionSocket.recv(1024)
                     fjaliaU=fjalia.upper()
                     fjaliaD = fjaliaU.decode();
                     
                     kerkesa=fjaliaD

    
                     kerkesa = kerkesa.split (" ") 
                     kerkesaTjeter="".join(kerkesa[1]) #Ne rastin kur kerkohet kerkesa tjeter rasti tek bashketingelloret qe kerkohet te shkruhet nje fjale(tekst)
                except:
                    print(fjalia.decode())
                    

                if (kerkesa[0] == "IPADRESA"):
                    pergj = IPADDR (addr);
                    pergjFinale = "IP-ja eshte: " + str(pergj);
                
                    connectionSocket.send (pergjFinale.encode("UTF-8"))
                    
                elif(kerkesa[0]=="NUMRIIPORTIT"):
                    pergj=NUMRIIPORTIT(addr)
                    pergjFinale="Numri i portit eshte:"+str(pergj)

                    connectionSocket.send (pergjFinale.encode("UTF-8")) 

                elif(kerkesa[0]=="EMRIIKOMPJUTERIT"):
                    pergj=EMRIIKOMPJUTERIT();
                    pergjFinale="Hosti(EMRIIKOMPJUTERIT) eshte:"+str(pergj);

                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif(kerkesa[0]=="KOHA"):
                    pergj=KOHA();
                    pergjFinale="Koha e serverit eshte:"+str(pergj)

                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif(kerkesa[0]=="BASHKETINGELLORE"):
                    pergj=BASHKETINGELLORE(kerkesaTjeter);
                    pergjFinale="Numri i bashketinglloreve ne tekst eshte:"+str(pergj)

                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif(kerkesa[0]=="PRINTIMI"):
                    pergj=PRINTIMI(kerkesa[1])#ose (kerkesaTjeter)
                    pergjFinale="Teksti i shtyper eshte:"+str(pergj)

                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif(kerkesa[0]=="LOJA"):
                    pergj=LOJA()
                    pergjFinale="Numrat e rendomte jane:"+str(pergj)

                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif (kerkesa[0] == "FIBONACCI"):
                    pergj = FIBONACCI(kerkesa[1])
                    pergjFinale = "Numri Fibonacci eshte: " + pergj

                    connectionSocket.send (pergjFinale.encode("UTF-8"))
                elif (kerkesa[0] == "KONVERTIMI"):
                    pergj = KONVERTIMI(str(kerkesa[1]),int(kerkesa[2]))
                    pergjFinale= "Konvertimi: " + str(pergj)
               
                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif (kerkesa[0]=="SHUMAENUMRAVEQIFT"):
                    pergj=SHUMAENUMRAVEQIFT(int(kerkesa[1]))
                    pergjFinale="SHuma e numrave qift e numrit te dhene eshte:"+pergj
                    connectionSocket.send(pergjFinale.encode("UTF-8"))
                elif (kerkesa[0]=="EKKUADRATIK"):
                    pergj=EKKUADRATIK(float(kerkesa[1]),float(kerkesa[2]),float(kerkesa[3]))
                    pergjFinale="zgjidhjet e ekuacionit kuadratik:\n"+pergj
                    connectionSocket.send(pergjFinale.encode("UTF-8"))

                else:
                    connectionSocket.send("KERKESA NUK ESHTE VALIDE".encode())
            connectionSocket.close()
        except Exception:
            print("Klienti eshte çkyqur ose ka ndonje gabim tjeter")
            break
while True:
     connectionSocket, addr = serverSocket.accept()
     start_new_thread(thredi,(connectionSocket,))
connectionSocket.close()

