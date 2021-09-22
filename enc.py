import sys
import base64
import hashlib
from Crypto.Cipher import AES
  
class passwordHashing :

	def pwHash(self, pw) :
		#base64
		plainPassword        = pw
		plainPasswordToAscii = plainPassword.encode("ascii")
		base64_bytes = base64.b64encode(plainPasswordToAscii)
		base64_string = base64_bytes.decode("ascii")

		#md5
		base64String = base64_string.encode('utf-8')
		md5_string = hashlib.md5(base64String).hexdigest()

		#sha512
		md5String = md5_string.encode('utf-8')
		sha512_string = hashlib.sha512(md5String)

		return sha512_string.hexdigest()

print(passwordHashing().pwHash(pw=sys.argv[1]))