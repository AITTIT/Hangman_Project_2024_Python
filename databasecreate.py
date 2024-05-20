import sqlite3

#connection = sqlite3.connect("worddatabase.db")


#connection.execute("""
#DROP TABLE IF EXISTS Words;
#""")

#connection.commit()

#connection.execute("""
#CREATE TABLE Words
#(ID INT PRIMARY KEY NOT NULL,
#WORD TEXT NOT NULL
#);
#""")

#connection.commit()

#connection.close()


#Tiedon lisääminen kantaan.
#connection = sqlite3.connect("worddatabase.db")

#connection.execute("""
#INSERT INTO Words (ID, WORD)
#VALUES (1, "submarine");                  
#""")

#connection.commit()

#connection.close()

#print("Add records END")

#KOKEILE AUTOINCREMENTILLÄ

#primaryKey = 2

#connection = sqlite3.connect("worddatabase.db")
#print("Add records")


#connection.execute(f"""
#INSERT INTO Words (ID, WORD)
#VALUES ({primaryKey}, "marine");                  
#""")

#connection.commit()

#connection.close()

#print("Add records END")



#connection = sqlite3.connect("worddatabase.db")


#connection.execute("""
#DROP TABLE IF EXISTS Words;
#""")

#connection.commit()

#connection.execute("""
#CREATE TABLE Words
#(ID INTEGER PRIMARY KEY,
#WORD TEXT NOT NULL
#);
#""")

#connection.commit()

#connection.execute("""
#INSERT INTO Words (WORD)
#VALUES ("marine");
#""")

#connection.execute("""
#INSERT INTO Words (WORD)
#VALUES ("marmelade");
#""")

#connection.commit()

#connection.close()

#print("It ran!")

def addWordtoDatabase(newWord):
    connection = sqlite3.connect("worddatabase.db")
    connection.execute(f"""
    INSERT INTO Words (WORD)
    VALUES ("{newWord}");
    """)
    connection.commit()
    connection.close()

def updateWordinDatabase(newWord):
    connection = sqlite3.connect("worddatabase.db")
    connection.execute(f"""
    UPDATE Words
    SET WORD = "{newWord}"
    WHERE ID = 2;
    """)
    connection.commit()
    connection.close()

def DeleteWordFromDatabase():
    connection = sqlite3.connect("worddatabase.db")
    tempID = int(input("Give ID of the word you wish to delete "))
    connection.execute(f"""
    DELETE FROM Words
    WHERE ID = {tempID};
    """)
    connection.commit()
    connection.close()

def listAllWords():
    connection = sqlite3.connect("worddatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Words")
    rows = cursor.fetchall()

    print("All words in the database:")
    for row in rows:
        print(f"ID: {row[0]} WORD: {row[1]}")
    
    connection.close()

def database_input():
    word = input("Enter word to add to database: ")
    return word

def readOneRecord(id):
    connection = sqlite3.connect("worddatabase.db")

    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Words WHERE ID = {id}")
    data = cur.fetchall()

    for record in data:
        print(f"{record[1]}")
    
    connection.close()

while(True):
    addWordtoDatabase(database_input())




#updateWordinDatabase(database_input())
#DeleteWordFromDatabase()
#listAllWords()
#readOneRecord(2)

#print("Ran.")