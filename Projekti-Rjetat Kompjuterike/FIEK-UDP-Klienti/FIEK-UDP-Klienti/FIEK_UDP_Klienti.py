import socket
from socket import *
s =socket(AF_INET,SOCK_DGRAM)
serverName=input("Emri i Serverit:")
try:
    if(serverName=="localhost" or serverName=="127.0.0.1"):
        print("Sheno portin")
    else:
        ("Sheno perseri")
except:
    serverName=input("Emri i serverit:")
serverPort=input("Porti:")
while(serverPort!="12000"):
    print("Sheno perseri")
    serverPort=input("Porti:")

print("Pergjigje nga serveri mund te merrni per keto metoda:\n\nIPADDR,PORT,ZANORE,HOST,PRINTO,TIME,LOJA,FIBONACCI,KONVERTO,SHUMAENUMRAVEQIFT\n")
print("--------------------------------------------------------------------------------")
print("1)Per te ditur IP adresen e klienti shkruaj: IPADRESA\n--------------------------------------------------------------------------------\n2)Per te ditur numrin e portit shkruaj:NUMRIIPORTIT :\n--------------------------------------------------------------------------------\n3)Per metoden BASHKETINGELLORE  shkruaj:BASHKETINGELLORE 'FJALIA'\n--------------------------------------------------------------------------------\n4)Per metoden PRINTIMI shkruaj:PRINTIMI \n--------------------------------------------------------------------------------\n5)Per metoden EMRIIKOMPJUTERIT shkruaj:EMRIIKOMPJUTERIT \n--------------------------------------------------------------------------------\n6)Per metoden KOHA shkruaj:KOHA\n--------------------------------------------------------------------------------\n7)Per metoden LOJA shkruaj:LOJA\n--------------------------------------------------------------------------------\n8)Per metoden FIBONACCI shkruaj: FIBONACCI numrin\n--------------------------------------------------------------------------------\n9)Per metoden Konverto shkruaj:KONVERTIMI 'llojin e konvertimit' numrin\n--------------------------------------------------------------------------------\n10)Per shumen e numrave çift nga 0 deri te numri n shkruaj:SHUMAENUMRAVEQIFT numri\n--------------------------------------------------------------------------------\n11)Per zgjidhjen e EKKUADRATIK sheno:EKKUADRATIK numri1 numri2 numri3\n--------------------------------------------------------------------------------\n")

while 1:
   try:
    var = input("Kerkesa juaj: ")
    s.sendto(str(var).encode(),(serverName,int(serverPort)))
    data,addr = s.recvfrom(128)
    print(data.decode("UTF-8"))
   except Exception as e:
       print(e)
   if(var=="DIL"):
       print("KENI KERKUAR TE MBYLLNI KLIENTIN")
       break
s.close()

