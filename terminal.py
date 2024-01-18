import subprocess
import ctypes
import os
from os import *
import fade

cwd=getcwd()

# Title
console_title = "title " + "ColorCMD in " + cwd

# Banner
banner = '''
╔══╗   ╔╗       ╔══╗         ╔╗      
║╔═╝   ║║       ║╔═╝         ║║      
║║  ╔══╣║ ╔══╗══╣║  ╔══════╦═╝║
║║  ║╔╗║║ ║╔╗║ ╔╣║  ║╔═╗╔═╗║╔╗║
║╚══╣╚╝║╚═╣╚╝║ ║║╚══╣║ ║║ ║║╚╝║
╚═══╩══╩══╩══╩═╝╚═══╩╝ ╚╝ ╚╩══╝
===============================
Created by Quang DZ
'''

success=True
user_input=""
system(console_title)

def check_names(infile):
	if path.isdir(infile):
		return True
	else:
		return False
	
def isAdmin():
	try:
		is_admin = (os.getuid() == 0)
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	return is_admin

def run_command(command):
	global success, user_input, cwd
	try:
		process = subprocess.Popen(command,shell=True)
		if user_input.find("cd ")==0:
			cwd=user_input.replace("cd ", "")
			chdir(cwd)
		if check_names(user_input) == True:
			cwd = user_input.replace("cd ", "")
			chdir(cwd)
		success = True
		process.wait()
	except subprocess.CalledProcessError as e:
		e = '\033[0m' + str(e)
		print('\033[91m'+'E: '+'\033[0m', e)
		success = False

def main():
	global user_input, admin_ip_suscess, admin_ip_not_suscess, user_ip_suscess, user_ip_not_suscess
	while True:
		cwd=getcwd()
		# Input theme
		admin_ip_suscess = '\033[94m' + '    ' + '\033[0m'+ '\033[1;43m' + '    ' + '\033[1;42m' + '    ' + '\033[7;49;93m' + '    '  + cwd + ' ' + '\033[1;41;40m' + ' ❯❯❯ ' + '\033[0m'+ ' '
		admin_ip_not_suscess = '\033[94m' + '    ' + '\033[0m'+ '\033[1;43m' + '    '  + '\033[0m'+ '\033[1;7;91m' + '    ' + '\033[0m'+ '\033[7;49;93m' + '    ' + cwd + ' ' + '\033[1;41;40m' + ' ❯❯❯ ' + '\033[0m'+ ' '
		user_ip_suscess = '\033[94m' + '    ' + '\033[0m'+ '\033[1;42m' + '    ' + '\033[0m'+ '\033[7;49;93m' + '    ' + cwd + ' ' + '\033[1;41;40m' + ' ❯❯❯ ' + '\033[0m'+ ' '
		user_ip_not_suscess = '\033[94m' + '    ' + '\033[1;7;91m' + '    ' + '\033[0m'+ '\033[7;49;93m' + '    ' + cwd + ' ' + '\033[1;41;40m' + ' ❯❯❯ ' + '\033[0m'+ ' '
		if isAdmin():
			if success == True:
				user_input=input(admin_ip_suscess)
			else:
				user_input=input(admin_ip_not_suscess)
		else:
			if success == True:
				user_input=input(user_ip_suscess)
			else:
				user_input=input(user_ip_not_suscess)
		run_command(user_input)
		system("title " + "ColorCMD in " + cwd)
		# print(getcwd()) #Debug only
print(fade.greenblue(banner))
main()

