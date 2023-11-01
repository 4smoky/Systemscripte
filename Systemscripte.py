#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# # learning by doing :-)
#
# Author : @ 4Smoky
#Maybee this will my start for many different things
#
#
# Import der shutil-Bibliothek um die Breite des Terminals zu erhalten
import shutil
# die socket bibliothek laden um eine netzwerkverbindung zu erhalten
import socket
# import des moduls für systembefehle
import subprocess
# import des modules time benötigt für sleep befehl
import time

# modul youtube downloader
import yt_dlp
# import für Hintergrund entfernung
from rembg import remove

from PIL import Image

# Farben
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
#Banner
BANNER_TEXT="""
   _____           _                               _       _        
  / ____|         | |                             (_)     | |       
 | (___  _   _ ___| |_ ___ _ __ ___  ___  ___ _ __ _ _ __ | |_ ___  
  \___ \| | | / __| __/ _ \ '_ ` _ \/ __|/ __| '__| | '_ \| __/ _ \ 
  ____) | |_| \__ \ ||  __/ | | | | \__ \ (__| |  | | |_) | ||  __/ 
 |_____/ \__, |___/\__\___|_| |_| |_|___/\___|_|  |_| .__/ \__\___| 
 |  _ \   __/ |                                     | |             
 | |_) |_|___/                                      |_|             
 |  _ <| | | |                                                      
 | |_) | |_| |                                                      
 |____/ \__, |                                                      
         __/ |                                                      
        |___/                                                       




  ██████  ███▄ ▄███▓ ▒█████   ██ ▄█▀▓██   ██▓
▒██    ▒ ▓██▒▀█▀ ██▒▒██▒  ██▒ ██▄█▒  ▒██  ██▒
░ ▓██▄   ▓██    ▓██░▒██░  ██▒▓███▄░   ▒██ ██░
  ▒   ██▒▒██    ▒██ ▒██   ██░▓██ █▄   ░ ▐██▓░
▒██████▒▒▒██▒   ░██▒░ ████▓▒░▒██▒ █▄  ░ ██▒▓░
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ██▒▒▒ 
░ ░▒  ░ ░░  ░      ░  ░ ▒ ▒░ ░ ░▒ ▒░ ▓██ ░▒░ 
░  ░  ░  ░      ░   ░ ░ ░ ▒  ░ ░░ ░  ▒ ▒ ░░  
      ░         ░       ░ ░  ░  ░    ░ ░     
                                     ░ ░     



"""""

# berechne die breite vom terminal
WIDTH = shutil.get_terminal_size().columns

# Banner
print('*' * WIDTH)
banner_centered = BANNER_TEXT.center(WIDTH)
print(f"{Color.RED}{banner_centered}{Color.RESET}")
print('*' * WIDTH)


#Beginn des scripts
print ()
print ("Hallo")
time.sleep(0.5)
name = input ("Wie ist dein Name ? : ")
print("")
print ("")
time.sleep(0.5)
print ("Hallo  " + name + ", Freut mich das du mein program testen willst.")
print ("")
print ("Ich hoffe es gefällt dir und hilft dir ein bischen ;)")

time.sleep(0.5)
print ("")
print (name + " ,was kann ich heute für dich tun ?")
time.sleep(0.5)

#optionen (menü für 6 aufgaben)

options = ["Systemupdate + mirror refresh", "Systemupdate ohne mirror refresh", "Systeminfo", "Speicherplatz mit duf Anzeigen", "Speichern aller installierten pakete in eine textdatei", "Installieren der Pakete von der erstellten Textdatei", "netzwerk SSH Bannergrab", "youtube dl", "hintergrund entfernen", "Beenden"]


#eindlosschleife und index erstellen beginnend mit 1
while True:
    for index, option in enumerate(options, start=1):
        print(f"\n{index}. {option}")
    # Auswahl der optionen
    choice = input("\nDeine Auswahl: ")

# Verarbeitung der Benutzerwahl
# option für Systemaktualisierung  mit mirrorliste
    if choice == "1":
        print (name + " Du hast die Sytem Update mit Mirror refresh gewählt :")

        # aktualisierung + mirror upgrade
        try:
            subprocess.run(["garuda-update"], shell=True)
            print("Update erfolgreich durchgeführt.")
        except subprocess.CalledProcessError:
            print("Fehler beim Ausführen des Update-Befehls.")

    # option für Systemaktualisierung ohne mirroliste

    elif choice == "2":
        print(f"\n  ")

        print(name + " Du hast die Sytem Update gewählt :")

        # Befehl für die Aktualisierung
        try:
            subprocess.run(["garuda-update --skip-mirrorlist"], shell=True)
            print("Update erfolgreich durchgeführt.")
        except subprocess.CalledProcessError:
            print("Fehler beim Ausführen des Update-Befehls.")

    # option für SystemINFO

    elif choice == "3":

        print(f"\n   ")

        print(name + " Du hast die Sytem Info gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["garuda-inxi"], shell=True)

            print("Systeminfo erfolgreich ausgeführt.")

        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")



    # option für Speicherplatzanzeige mit Duf

    elif choice == "4":

        print(f"\n   ")

        print(name + " Du hast Speicherplatz gewählt :")


        def install_and_execute(command):
            try:
                # Führe den Befehl aus
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                print("programm nicht installiert . Es wird nun Duf installiert und sie müßen ihr root password eingeben")
                # Installiere das Paket und führe den Befehl erneut aus
                install_command = "paru -S " + command.split()[0] + " --noconfirm"  # Extrahiere den Paketnamen aus dem Befehl
                subprocess.run(install_command, shell=True, check=True)
                subprocess.run(command, shell=True, check=True)


        # Hier ist ein Beispielaufruf:
        command_to_execute = "duf"
        install_and_execute(command_to_execute)

    # option für Systempackete sichern

    elif choice == "5":

        print(f"\n   ")

        print(name + " Du hast Backup der Pakete gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["pacman -Qeq > Pakete.txt"], shell=True)

            print("Pakete erfolgreich nach Pakete.txt gesichert.")


        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")

    # option für installieren der packete der sicherung

    elif choice == "6":

        print(f"\n   ")

        print(name + " Du hast Installieren der Pakete gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["sudo pacman -S $(cat Pakete.txt)"], shell=True)

            print("Pakete erfolgreich von Pakete.txt installiert.")


        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")

    # option für Bannergrab

    elif choice == "7":
        print()
        print(f"\n   Netzwerk SSH Bannercrab")
        # frage nach der ip addresse
        ip = input("geben sie die ip adresse ein :  ")

        s = socket.socket()

        s.connect((ip, 22))

        answer = s.recv(1024)

        print(answer)

        print("SSH bannergrab erfolgreich ausgeführt.")

        s.close

    # option für Youtube video downloader

    elif choice == "8":
        print(f"\n   ")
        print(name + " Du willst von YouTube ein Video herunterladen:")

        url = input("Enter URL: ")
        ydl_opts = {}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video erfolgreich heruntergeladen!")


    # Option 9: Hintergrund entfernen


    elif choice == "9":

        print(f"\n   ")

        print(name + " Du willst den Hintergrund von einem Bild entfernen :")

        input_path = input("Gib den Pfad des Bildes ein: ")

        output_path = input("Speicherpfad: ")

        try:

            inp = Image.open(input_path)

            # Hintergrund mit rembg entfernen

            output = remove(inp)

            output.save(output_path)

            print("Hintergrund entfernt und gespeichert.")


        except FileNotFoundError:

            print("Die angegebene Datei wurde nicht gefunden.")

        except Exception as e:

            print("Ein Fehler ist aufgetreten:", str(e))

            #option 10 beenden

    elif choice == "10":
        print(f"\n  Viel Spaß")
        exit()  # Beenden des Skripts

    # option für Falsche eingabe

    else:
        print(f"\n   Falsche Eingabe!!")
        print(f"\n   ")
        input(f"\n   Drücken Sie Enter, um fortzufahren")
