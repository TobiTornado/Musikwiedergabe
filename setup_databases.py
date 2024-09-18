
#####################################################################################################
##################### NUR EINMAL AUSFÜHREN UM DATENBANKEN ERSTMALS ZU ERSTELLEN #####################
#####################################################################################################

import mysql.connector

config = {
    "user": "root",
    "password": "****",
    "host": "localhost",
    "database": "MySQL"
}
# Establish the connection
mydb = mysql.connector.connect(**config)

#interactionsmglkeit mit DB
mycursor = mydb.cursor()

#Datenbank
mycursor.execute("CREATE DATABASE musikplayer;")
mydb.commit()

#Hauptdatenbank
mycursor.execute("CREATE TABLE musikplayer.lieder (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
mydb.commit()

#beispieldatenbanken
mycursor.execute("CREATE TABLE musikplayer.pop (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
mydb.commit()
mycursor.execute("CREATE TABLE musikplayer.rock (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
mydb.commit()
mycursor.execute("CREATE TABLE musikplayer.80s (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
mydb.commit()

#datenbanken befüllen
mycursor.execute("INSERT INTO musikplayer.lieder (name, interpreter) VALUES ('back in black', 'ACDC'), ('comfortably numb', 'Pink Floyd'), ('hotel california', 'Eagles'), ('stairway to heaven', 'Led Zeppelin'), ('sweet child o mine', 'Guns N Roses'), ('billie jean', 'Michael Jackson'), ('take on me', 'A-ha'), ('living on a prayer', 'Bon Jovi'), ('eye of the tiger', 'Survivor'), ('africa', 'Toto'), ('bad habits', 'Ed Sheeran'), ('Harleys in Hawaii', 'Katy Perry'), ('rolling in the deep', 'Adele'), ('shape of you', 'Ed Sheeran'), ('viva la vida', 'Coldplay'), ('good life', 'OneRepublic');")
mydb.commit()
mycursor.execute("INSERT INTO musikplayer.pop (name, interpreter) VALUES ('bad habits', 'Ed Sheeran'), ('harleys in hawaii', 'Katy Perry'), ('rolling in the deep', 'Adele'), ('shape of you', 'Ed Sheeran'), ('viva la vida', 'Coldplay'), ('good life', 'OneRepublic');")
mydb.commit()
mycursor.execute("INSERT INTO musikplayer.rock (name, interpreter) VALUES ('back in black', 'ACDC'), ('comfortably numb', 'Pink Floyd'), ('hotel california', 'Eagles'), ('stairway to heaven', 'Led Zeppelin'), ('sweet child o mine', 'Guns N Roses');")
mydb.commit()
mycursor.execute("INSERT INTO musikplayer.80s (name, interpreter) VALUES ('back in black', 'ACDC'), ('sweet child o mine', 'Guns N Roses'), ('billie jean', 'Michael Jackson'), ('take on me', 'A-ha'), ('living on a prayer', 'Bon Jovi'), ('eye of the tiger', 'Survivor'), ('africa', 'Toto');")
mydb.commit()