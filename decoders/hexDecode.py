#! python3
import codecs

hexFile = open('hex.txt', 'r')

decode = hexFile.read()

plainFile = open('hex_plain.txt', 'wb')
plainFile.write(codecs.decode(decode, "hex"))

hexFile.close()
plainFile.close()
