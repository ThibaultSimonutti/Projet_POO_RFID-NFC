import sys
import nxppy

mifare=nxppy.Mifare()
uid = mifare.select()

print (sys.argv[1])
data = sys.argv[1]
longueur = len(sys.argv[1])
x = 0
y = 4
block = 10

mifare.write_block(block,HEX'0000')
while longueur > 0:
	towrite = data[x:y]
	b = bytes(towrite)
	mifare.write_block(block,b)
	longueur = longueur - 4
	x = x+4
	y = y+4
	block = block + 1

