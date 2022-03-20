import turtle
import time
import sys


simone=turtle.Turtle()

class Comandi:
    
    def forward():
        simone.forward(misura)

    def back():
        simone.back(misura)

    def right():
        simone.right(misura)

    def left():
        simone.left(misura)

    def speed():
        simone.speed(misura)
try:
    game_name="Create Your Drawing!\n"
    game_name_color=sys.stdout.shell
    game_name_color.write(game_name,"BUILTIN")
    time.sleep(2)
    print()
    developer="App Developed by CaptainBeluga\n"
    developer_color=sys.stdout.shell
    developer_color.write(developer,"COMMENT")
    time.sleep(2)
    print()
    option1="Digita 1 per CREARE UN DISEGNO\n"
    option2="Digita 2 per LEGGERE il MANUALE dei COMANDI\n"
    options_color=sys.stdout.shell
    options_color.write(option1,"console")
    options_color.write(option2,"console")
    scegli=int(input("Scegli: "))
    print()

    if scegli==1:
        
        while True:
            comando=input("COMANDO: ")
            misura=int(input("MISURA: "))
            print()
            print()

            if comando=="avanti" or comando=="AVANTI" or comando=="forward":
                forward_command=Comandi
                forward_command.forward()

            if comando=="indietro" or comando=="INDIETRO" or comando=="back":
                back_command=Comandi
                back_command.back()

            if comando=="destra" or comando=="DESTRA" or comando=="right":
                right_command=Comandi
                right_command.right()
                

            if comando=="sinistra" or comando=="SINISTRA" or comando=="left":
                left_command=Comandi
                left_command.left()


            if comando=="velocità" or comando=="VELOCITÀ" or comando=="speed":
                speed_command=Comandi
                speed_command.speed()
                
    if scegli==2:
        print("""        MANUALE DEI COMANDI: 


                AVANTI = avanti /PREMI ENTER/  misura = pixel schermo
                INDIETRO = indietro /PREMI ENTER/ misura = pixel schermo
                DESTRA = destra /PREMI ENTER/ misura = gradi
                SINISTRA = sinistra /PREMI ENTER/ misura = gradi
                VELOCITÀ = velocità /PREMI ENTER/ misura = velocità""")
                     
        

               
except ValueError:
    print()
    print("ERRORE DI VALUTA; ricorda di scrivere solo numeri!")
