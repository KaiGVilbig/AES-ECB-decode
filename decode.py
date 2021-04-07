from Crypto.Cipher import AES
import time

def genkey(keylen, time):
	n = 278680767812959796815817796531952571
	x = time & 0xffffff
	key = bytearray(keylen)
	for i in range(keylen):
		key[i] = 0
		for j in range(8):
			x = (x*x) % n
			key[i] = (key[i] << 1) ^ (x & 1)
	return(bytes(key))

def main():
	#Open the encrypted message and read the bytes into one byte array
	decFile = input("File to decrypt: ")
	finFile = input("File to save decrypted message to: ")
	try:
		f = open(decFile, "rb")
		hugeText = bytes(f.read())

		#define key/block length to test different standards
		keyLen = 16
		blockLen = 16

		for p in range(6):
			for i in range(60):
				key = bytearray(keyLen)

				#Create timestamp to seed key generation
				t = (2021, 3, 18, 21, p+57, i, 0, 0, 1)
				times = int(time.mktime(t))
				key = genkey(keyLen, int(times))

				try:
					#Create cipher object and decrypt encoded bytes
					cipher = AES.new(key, AES.MODE_ECB)
					dec = cipher.decrypt(hugeText)
					#Hex for BIRDMASTER
					res = b'\x42\x49\x52\x44\x4D\x41\x53\x54\x45\x52'

					#Search decrypted byte array for a BIRDMASTER
					if(dec.find(res) != -1):
						#If match, write decrypted bytes to doc file
						f1 = open(finFile, "wb")
						f1.write(dec)
						f1.close()

				except Exception as e:
					#catch exception with the seed that errored out
					print("p: ", p, " i: ", i, " ", e)
	except:
		print("invalid file")

main()
