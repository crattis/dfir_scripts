#! python3
import base64

base_file = open('base64.txt', 'r')

decode = base_file.read()

plainFile = open('b64_plain.txt', 'wb')
plainFile.write(base64.b64decode(decode))

base_file.close()
plainFile.close()
