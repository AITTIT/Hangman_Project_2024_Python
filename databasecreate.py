import sqlite3
import random

def getWordFromDatabase():
    """" Connects to the word database, picks a word at random, and returns it. """
    connection = sqlite3.connect("worddatabase.db")
    randomID = random.randrange(2, 55)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Words WHERE ID = {randomID}")
    data = cursor.fetchall()

    for record in data:
        tempWord = record[1]
    
    return tempWord

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


if __name__ == "__main__":
    listAllWords()
