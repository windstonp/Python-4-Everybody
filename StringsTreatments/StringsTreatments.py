string = "XDSPAM-Confidence: 0.8475 "

doubledotspos = string.find(":")

string = string[doubledotspos+1:] 
string = string.strip()
string = float(string)

print(string)