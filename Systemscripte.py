#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# # learning by doing :-)
#
# Author : @ 4Smoky
#
# Maybee this will my start for many different things
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


# Banner
BANNER_TEXT = """
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

# Script start
print("\nHallo")
time.sleep(0.2)
print(f"\nWas möchtest du tun ?")
time.sleep(0.5)
print("")
# Options menu
options = [
  "Systemupdate + mirror refresh (nur für garuda linux)",
  "Systemupdate ohne mirror refresh (nur für garuda linux)",
  "Systeminfo (nur für garuda linux)",
  "Speicherplatz anzeigen",
  "Speichern aller installierten Pakete in eine Textdatei (nur für eine Arch linux distro)",
  "Installieren der Pakete von der erstellten Textdatei (nur für eine Arch linux distro)",
  "Netzwerk SSH Bannergrab",
  "YouTube Download",
  "Hintergrund entfernen",
  "Beenden"
]

while True:
  for index, option in enumerate(options, start=1):
      print(f"\n{index}. {option}")

  choice = input("\nDeine Auswahl: ")

  if choice == "1":
      print(f"Du hast die System Update mit Mirror refresh gewählt:")
      try:
          subprocess.run(["sudo", "pacman", "-Syu"], check=True)
          print("Update erfolgreich durchgeführt.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen des Update-Befehls.")

  elif choice == "2":
      print(f"Du hast die System Update ohne Mirror refresh gewählt:")
      try:
          subprocess.run(["sudo", "pacman", "-Syu", "--ignore", "pacman-mirrorlist"], check=True)
          print("Update erfolgreich durchgeführt.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen des Update-Befehls.")

  elif choice == "3":
      print(f"Du hast die System Info gewählt:")
      try:
          subprocess.run(["uname", "-a"], check=True)
          print("Systeminfo erfolgreich ausgeführt.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen")

  elif choice == "4":
      print(f"Du hast Speicherplatz gewählt:")
      try:
          subprocess.run(["df", "-h"], check=True)
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen")

  elif choice == "5":
      print(f"Du hast Backup der Pakete gewählt:")
      try:
          with open("Pakete.txt", "w") as f:
              subprocess.run(["pacman", "-Qeq"], stdout=f, check=True)
          print("Pakete erfolgreich nach Pakete.txt gesichert.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen")

  elif choice == "6":
      print(f"Du hast Installieren der Pakete gewählt:")
      try:
          with open("Pakete.txt", "r") as f:
              packages = f.read().splitlines()
          subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=True)
          print("Pakete erfolgreich von Pakete.txt installiert.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen")

  elif choice == "7":
      print("\nNetzwerk SSH Bannergrab")
      ip = input("Geben Sie die IP-Adresse ein: ")
      try:
          with socket.create_connection((ip, 22), timeout=5) as s:
              banner = s.recv(1024).decode('utf-8')
              print(f"SSH Banner: {banner}")
      except Exception as e:
          print(f"Fehler beim Verbinden: {e}")

  elif choice == "8":
      print(f"Du willst von YouTube ein Video herunterladen:")
      url = input("Enter URL: ")
      ydl_opts = {}
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
      print("Video erfolgreich heruntergeladen!")

  elif choice == "9":
      print(f"Du willst den Hintergrund von einem Bild entfernen:")
      input_path = input("Gib den Pfad des Bildes ein: ")
      output_path = input("Speicherpfad: ")
      try:
          inp = Image.open(input_path)
          output = remove(inp)
          output.save(output_path)
          print("Hintergrund entfernt und gespeichert.")
      except FileNotFoundError:
          print("Die angegebene Datei wurde nicht gefunden.")
      except Exception as e:
          print("Ein Fehler ist aufgetreten:", str(e))

  elif choice == "10":
      print(f"\nGoodbye")
      sys.exit(0)

  else:
      print("\nFalsche Eingabe!!")

  input("\nDrücken Sie Enter, um fortzufahren")
