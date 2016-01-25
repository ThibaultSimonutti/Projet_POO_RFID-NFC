import sqlite3
import sys
import nxppy
import time

mifare=nxppy.Mifare()
conn = sqlite3.connect('BDD_NFC.sqlite')
c = conn.cursor()

while True:
	try:
	
		uid = mifare.select()
		print"read uid", uid
		data = uid
		c.execute("""SELECT * FROM Historique WHERE uid=?""",(data,))
		rows = c.fetchall()
		if rows:
			for row in rows:
				print('{0} : {1} - {2} '.format(row[0], row[1], row[2]))
			
		else:
			print "Utiisateur Inconnu"
		time.sleep(3)
	except nxppy.SelectError:
		pass
	except (KeyboardInterrupt, SystemExit):
		conn.close()
