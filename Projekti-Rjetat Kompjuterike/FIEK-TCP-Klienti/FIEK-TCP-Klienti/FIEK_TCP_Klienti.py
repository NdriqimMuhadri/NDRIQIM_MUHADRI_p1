import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverName=input("Emri i Serverit:")
while(serverName!="localhost"):
    print("Shenoni perseri")
    serverName=input("EMRI I SERVERIT:")
def porti():
    while 1:
        try:
            numriportit=int(input("PORTI: "))
            if(numriportit>1 or numriportit<65665):
                return int(numriportit)
            break
        except:
            print("Numri duhet te jete ne mes 1 dhe 65665")
while True:
    try:
        serverPort=porti()
        s.connect((serverName,serverPort))
        break
    except:
        print("Porti nuk eshte i hapur")
print("Jeni lidhur me serverin\n")
print("KUJDESS!! Pas perdorimit te cilesdo metode duhet perdorur nje hapsire\n")
print("Pergjigje nga serveri mund te merrni per keto metoda:\n\nIPADDR,PORT,ZANORE,HOST,PRINTO,TIME,LOJA,FIBONACCI,KONVERTO,SHUMAENUMRAVEQIFT\n")
print("--------------------------------------------------------------------------------")
print("1)Per te ditur IP adresen e klienti shkruaj: IPADRESA\n--------------------------------------------------------------------------------\n2)Per te ditur numrin e portit shkruaj:NUMRIIPORTIT :\n--------------------------------------------------------------------------------\n3)Per metoden BASHKETINGELLORE  shkruaj:BASHKETINGELLORE 'FJALIA'\n--------------------------------------------------------------------------------\n4)Per metoden PRINTIMI shkruaj:PRINTIMI \n--------------------------------------------------------------------------------\n5)Per metoden EMRIIKOMPJUTERIT shkruaj:EMRIIKOMPJUTERIT \n--------------------------------------------------------------------------------\n6)Per metoden KOHA shkruaj:KOHA\n--------------------------------------------------------------------------------\n7)Per metoden LOJA shkruaj:LOJA\n--------------------------------------------------------------------------------\n8)Per metoden FIBONACCI shkruaj: FIBONACCI numrin\n--------------------------------------------------------------------------------\n9)Per metoden Konverto shkruaj:KONVERTIMI 'llojin e konvertimit' numrin\n--------------------------------------------------------------------------------\n10)Per shumen e numrave çift nga 0 deri te numri n shkruaj:SHUMAENUMRAVEQIFT numri\n--------------------------------------------------------------------------------\n11)Per zgjidhjen e EKKUADRATIK sheno:EKKUADRATIK numri1 numri2 numri3\n--------------------------------------------------------------------------------\n")

while 1:

    var = input("Kerkesa juaj: ")
    s.sendall(var.encode("UTF-8"))
    data = s.recv(128)
    print('Te dhenat e pranuara nga serveri jane :\n' + data.decode("UTF-8"))
    if(var=="DIL"):
        print("KENI KERKUAR TE MBYLLNI KLIENTIN")
        break
    
  
s.close()


