from Crypto.Cipher import AES
import base64

secret_key = "1234"
msg_text = "$A7$P#p?KHdb"

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

encoded = base64.b64encode(cipher.encrypt(msg_text))

print(encoded)