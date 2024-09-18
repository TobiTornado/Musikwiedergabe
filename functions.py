import pygame
import os
import database

def clear_console():
    if os.name == "nt":
        os.system("cls")


def play_music():

    #pygame schrift löschen
    clear_console()

    #Klassen initialisieren
    pygame.init()
    pygame.mixer.init()

    #namens vereinfachung
    player = pygame.mixer.music

    song_wahlneu = None
   
    while song_wahlneu is None:    
        #MUSIKHÖREN
        #song auswahl

        song_wahl = input("Wenn sie zurück ins Hauptmenü wollen schreiben Sie beenden\nWelchen Song wollen Sie hören: ")
        clear_console()

        if song_wahl == "beenden":
            return

        song_wahlneu = database.search_song(song_wahl)


    #lied laden
    player.load(f"{song_wahlneu}.mp3")
    print(f"{song_wahlneu} wird abgespielt...")

    #lautstärke einstellen
    player.set_volume(0.5)

    player.play()

    #einfacher player
    while True:
        choice = input("aktion (pause/unpause/play/stop/lied ändern/lautstärke ändern/beenden): ")

        match choice:
            case "pause":
                player.pause()
                clear_console()
            case "unpause":
                player.unpause()
                clear_console()
            case "stop":
                player.stop()
                clear_console()
            case "play":
                player.play()
                clear_console()
            case "lied ändern":
                song_wahl = input("Zu welchem Song wollen Sie wechseln? ")
                
                song_wahl = database.search_song(song_wahl)
                player.stop()
                
                player.load(f"{song_wahl}.mp3")
                clear_console()
                
                print(f"{song_wahl} wird abgespielt...")
                player.play()
            case "lautstärke ändern":
                volume_wahl = float(input("Wie laut wollen Sie die Musik abspielen (Werte von 0 bis 1)? "))
                player.set_volume(volume_wahl)
                clear_console()
            case "beenden":
                clear_console()
                player.stop()
                print("Der Musikplayer wird beendet...")
                break
            case other:
                #?? sagt isnt accessed aber erreichbar
                print("Ihre Anfrage konnte nicht verarbeitet werden :(")