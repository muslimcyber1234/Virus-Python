import os,sys,time,requests
#Clean screen
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = R+"""
echo "\033[32;1m=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
toilet -f standard -F gay "Virus Python"
echo "\033[31;1m=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
echo ""
echo "Author : " muslimcyber1234"
" Team : " muslimcyber1234"
echo " gmail : " muslimcyber1234@gmail.com"
" message : "don't misuse this script to other people :) because it can harm other people :)"
sleep 1
echo "ThanksTo:"
echo "Allmember muslimcyber1234"
echo "\033[32;1m=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
echo "
       _                              _   _                   _
__   _(_)_ __ _   _ ___   _ __  _   _| |_| |__   ___  _ __   | |__  _   _
\ \ / / | '__| | | / __| | '_ \| | | | __| '_ \ / _ \| '_ \  | '_ \| | | |
 \ V /| | |  | |_| \__ \ | |_) | |_| | |_| | | | (_) | | | | | |_) | |_| |
  \_/ |_|_|   \__,_|___/ | .__/ \__, |\__|_| |_|\___/|_| |_| |_.__/ \__, |
                         |_|    |___/                               |___/


                     _ _                      _
 _ __ ___  _   _ ___| (_)_ __ ___   ___ _   _| |__   ___ _ __
| '_ ` _ \| | | / __| | | '_ ` _ \ / __| | | | '_ \ / _ \ '__|
| | | | | | |_| \__ \ | | | | | | | (__| |_| | |_) |  __/ |
|_| |_| |_|\__,_|___/_|_|_| |_| |_|\___|\__, |_.__/ \___|_|
                                        |___/

 _ ____  _____ _  _
/ |___ \|___ /| || |
| | __) | |_ \| || |_
| |/ __/ ___) |__   _|
|_|_____|____/   |_|


     """+G+"""FRANS-O,CONER"""+R+"""   /___/"""

def run(x):
	for n in x+"\n":
		sys.stdout.write(n)
		sys.stdout.flush()
		time.sleep(0.1)
def main():
	os.system('clear')
	print logo
	print
	no = raw_input(Y+"["+W+"?"+Y+"]["+W+"TARGET"+Y+"]>> "+G)
	run(Y+"[!] Checking Target ...")
	time.sleep(4)
	if no < 5:
		print R+"[!] Target Not Found"
		sys.exit()
	elif '62' in no or '+62' in no or '08' in no:
		print Y+"["+W+"LOCATION"+Y+"]: "+W+"Indonesian"
		time.sleep(4)
		serang(no)
	else:
		print R+"[!] Tool Not Support "+no
		print G+"[!] Tool Support Indonesian Number"
		sys.exit()

def serang(no):
	os.system('clear')
	print logo
	print
	run(Y+"[!] Attack ...")
	time.sleep(2)
	while True:
		try:
			print G+"Success Send Python virus To: "+Y+no
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		print R+"[x] No Connection"
		sys.exit()
