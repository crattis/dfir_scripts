#! python3
import base64

baseFile = open('base64.txt', 'r')

decode = baseFile.read()

plainFile = open('b64_plain.txt', 'wb')
plainFile.write(base64.b64decode(decode))


baseFile.close()
plainFile.close()
