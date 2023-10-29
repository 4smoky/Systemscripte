#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# # learning by doing :-)
#
# Author : @ Elfo
#
#Maybee this will my start for many different things
#
#
# Import der shutil-Bibliothek um die Breite des Terminals zu erhalten
import shutil
#import des modules time benötigt für sleep befehl
import time
#import des moduls für systembefehle
import subprocess
import sys
# die socket bibliothek laden um eine netzwerkverbindung zu erhalten
import socket
# youtube downloder modul
import yt_dlp
# Farben
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
#Banner
BANNER_TEXT="""

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

options = ["Systemupdate + mirror refresh", "Systemupdate ohne mirror refresh", "Systeminfo", "Speicherplatz mit duf Anzeigen", "Speichern aller installierten pakete in eine textdatei", "Installieren der Pakete von der erstellten Textdatei", "netzwerk SSH Bannergrab", "youtube video download", "Beenden"]


#eindlosschleife und index erstellen beginnend mit 1
while True:
    for index, option in enumerate(options, start=1):
        print(f"\n{index}. {option}")
    # Auswahl der optionen
    choice = input("\nDeine Auswahl: ")

# Verarbeitung der Benutzerwahl
    if choice == "1":
        print (name + " Du hast die Sytem Update mit Mirror refresh gewählt :")

        # aktualisierung + mirror upgrade
        try:
            subprocess.run(["garuda-update"], shell=True)
            print("Update erfolgreich durchgeführt.")
        except subprocess.CalledProcessError:
            print("Fehler beim Ausführen des Update-Befehls.")

    elif choice == "2":
        print(f"\n  ")

        print(name + " Du hast die Sytem Update gewählt :")

        # Befehl für die Aktualisierung
        try:
            subprocess.run(["garuda-update --skip-mirrorlist"], shell=True)
            print("Update erfolgreich durchgeführt.")
        except subprocess.CalledProcessError:
            print("Fehler beim Ausführen des Update-Befehls.")


    elif choice == "3":

        print(f"\n   ")

        print(name + " Du hast die Sytem Info gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["garuda-inxi"], shell=True)

            print("Systeminfo erfolgreich ausgeführt.")

        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")





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

    elif choice == "5":

        print(f"\n   ")

        print(name + " Du hast Backup der Pakete gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["pacman -Qeq > Pakete.txt"], shell=True)

            print("Pakete erfolgreich nach Pakete.txt gesichert.")


        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")

    elif choice == "6":

        print(f"\n   ")

        print(name + " Du hast Installieren der Pakete gewählt :")

        # Befehl für die Aktualisierung

        try:

            subprocess.run(["sudo pacman -S $(cat Pakete.txt)"], shell=True)

            print("Pakete erfolgreich von Pakete.txt installiert.")


        except subprocess.CalledProcessError:

            print("Fehler beim Ausführen")

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

    elif choice == "8":
        print(f"\n   ")
        print(name + " Du willst von YouTube ein Video herunterladen:")

        # Import von yt_dlp sollte bereits oben erfolgen, nicht hier
        url = input("Enter URL: ")
        ydl_opts = {}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video erfolgreich heruntergeladen!")
    
    elif choice == '9':
        print(f"\n  Viel Spaß")
        exit()  # Beenden des Skripts

    else:
        print(f"\n   Falsche Eingabe!!")
        print(f"\n   ")
        input(f"\n   Drücken Sie Enter, um fortzufahren")
