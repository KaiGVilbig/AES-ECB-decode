# AES-ECB-decode
Decodes two files encoded with 128bit AES in ECB mode


I already konw the files are origionally .doc files because of the repeated lines which are also present in .doc files
I already know it is encoded in AES-ECB because it leaves the repeated lines of hex after encoding. 

I also konw that the sender is codename "BIRDMASTER" so I can search hex values for that in the decoded messages to see if I have decoded properly. 

The given genkey file creates a key to which the message was encoded in and I can see that it uses time.time() to generate a key.
I can use this to find the key because I was given a text file of the files creation timestamp which I can use time.mktime() 
Because the time of creation is not the same as the key generation time, I gave it a 6 minute window
Because the timestamps do not include seconds I had to create a key for each second within that 6 min window
