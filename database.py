import mysql.connector
import functions

password = "TK28#MySQL"

#Songsuche
def search_song(song_name):
    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name FROM musikplayer.lieder WHERE name LIKE '%"+ song_name +"%';")
    name = mycursor.fetchone()

    if name is None:
        print("Dieser Song konnte leider nicht gefunden werden")
        mycursor.close()
        mydb.close()
    else:
        name = name[0].strip()

        mycursor.close()
        mydb.close()

    return name


#Playlist erstellen
def create_table(table_name):
    
    functions.clear_console()

    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE TABLE musikplayer."+ table_name +"(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
    #sichern
    mydb.commit()
    print("Die Playlist "+ table_name +" wurde erstellt.")

    mycursor.close
    mydb.close()

#Playlist löschen
def delete_table(table_name):
    
    functions.clear_console()

    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    does_exist(table_name)
    table_name = does_exist(table_name)
    
    mycursor.execute("DROP TABLE musikplayer."+ table_name +";")
    #sichern
    mydb.commit()
    print("Die Playlist "+ table_name +" wurde gelöscht.")

    mycursor.close
    mydb.close()

#datenbank existiert ned error catchen
def does_exist(table_name):
    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()


    mycursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'musikplayer' AND table_name = '{table_name}');")
    table_exists = mycursor.fetchone()

    while table_exists[0] == 0:
        table_name = input("Diese Playlist konnte nicht gefunden werden, bitte geben Sie eine andere Playlist ein: ")
        mycursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'musikplayer' AND table_name = '{table_name}');")
        table_exists = mycursor.fetchone()

    return table_name

#Playlist anzeigen
def show_table(table_name):
    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    #daten aus table entnehmen
    mycursor.execute("SELECT name, interpreter FROM musikplayer."+ table_name +";")
    zeilen = mycursor.fetchall()

    functions.clear_console()

    print(table_name +":\n")
    for zeile in zeilen:
        name = zeile[0].strip()
        interpreter = zeile[1].strip()
        print("-"+ name +":", interpreter)
    print("\n")

    mycursor.close
    mydb.close()
    return table_name

#Lied hinzufügen
def add_song(table_name):
    functions.clear_console()
    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    #song anfragen
    print("Hier sind alle Lieder, die Verfügbar sind und noch nicht in der Playlist sind:")
    #
    mycursor.execute(f"SELECT name FROM (SELECT name FROM musikplayer.lieder UNION ALL SELECT name FROM musikplayer.{table_name}) AS combined_table GROUP BY name HAVING COUNT(*) = 1 ORDER BY name;")
    zeilen = mycursor.fetchall()

    for zeile in zeilen:
        name = zeile[0].strip()
        print("-"+ name)
    
    song_name = input("\nWenn Sie zurück zum Hauptmenü wollen schreiben Sie beenden\nWelches Lied wollen Sie zu dieser Playlist hinzufügen? ")
    #song name mglweise korrigieren
    song_name = search_song(song_name)

    if song_name is not None:
        #interpreten holen
        mycursor.execute("SELECT name, interpreter FROM musikplayer.lieder WHERE name = '"+ song_name +"';")
        newsong = mycursor.fetchone()

        mycursor.execute(f"INSERT INTO musikplayer.{table_name} (name, interpreter) VALUES {newsong};")
        #speichern der operation
        mydb.commit()

        #kosmetik
        functions.clear_console()

        print("Das Lied "+ song_name +" wurde zur Playlist "+ table_name +" hinzugefügt.")
        mycursor.close
        mydb.close()
    elif song_name == "beenden":
        return

#Lied entfernen
def remove_song(table_name):
    config = {
        "user": "root",
        "password": f"{password}",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    #song anfragen
    song_name = input("Wenn Sie zurück zum Hauptmenü wollen schreiben Sie beenden\nWelches Lied wollen Sie aus dieser Playlist löschen? ")
    #song name mglweise korrigieren
    song_name = search_song(song_name)

    #existiert song in playlist?
    mycursor.execute(f"SELECT name FROM musikplayer.{table_name} WHERE name = '{song_name}'")
    song_exists = mycursor.fetchall()

    #prüfen nach nonetype und ob song existiert wenn existiert wurde ein wert aus sql genommen daher liste mit 1 namen befüllt
    if song_name is not None and len(song_exists) == 1:
        #id holen wegen safe update mode nur durch id löschbar
        mycursor.execute(f"SELECT id FROM musikplayer.{table_name} WHERE name = '{song_name}';")
        del_id = mycursor.fetchone()
        newdel_id = int(del_id[0])
        mycursor.execute(f"DELETE FROM musikplayer.{table_name} WHERE id = {newdel_id};")
        #speichern der operation
        mydb.commit()

        #kostmetik
        functions.clear_console()

        print("Das Lied "+ song_name +" wurde aus der Playlist "+ table_name +" entfernt.")
        mycursor.close
        mydb.close()
    elif song_name == "beenden":
        return
        
