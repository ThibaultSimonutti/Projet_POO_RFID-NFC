import nxppy
import time
import sqlite3


mifare=nxppy.Mifare()
conn = sqlite3.connect('BDD_NFC.sqlite')
c = conn.cursor()


while True:
	try:
		uid = mifare.select()
		print "Read uid", uid
		Date = time.strftime('%d/%m/%y %H:%M',time.localtime())
		print (Date)
		c.execute("""SELECT * FROM Utilisateur WHERE uid=?""",(uid,))
		row = c.fetchone()
		if row is None:
			print "Utiisateur Inconnu"
		else:
			print (row[1])
			c.execute("""INSERT INTO Historique(uid, time) VALUES(?, ?)""",(row[3], Date,))
			
			c.execute("""SELECT * FROM Historique WHERE uid=?""",(uid,))
			row = c.fetchall()
			for d in row:
				print(d[1])
			
		time.sleep(3)
	except nxppy.SelectError:
		pass
	except (KeyboardInterrupt, SystemExit):
		conn.close()
