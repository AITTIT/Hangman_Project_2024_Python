import sqlite3
import random


def getWordFromDatabase():
    connection = sqlite3.connect("worddatabase.db")
    randomID = random.randrange(2, 55)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Words WHERE ID = {randomID}")
    data = cursor.fetchall()

    for record in data:
        tempWord = record[1]
    
    return tempWord


chosenWord = getWordFromDatabase()

print(chosenWord)