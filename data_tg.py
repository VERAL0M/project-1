import sqlite3

conn = sqlite3.connect('data_gp.db')
cur = conn.cursor()


photos = cur.execute('SELECT photo FROM photos')

k=1
for photo in photos:
    with open(f'{k}.jpg','wb') as file:
        file.write(photo[0])
        k+=1
        
conn.commit()
cur.close()
conn.close()