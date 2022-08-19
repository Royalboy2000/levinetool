from subprocess import call
import shlex

answer = input("hii do you want to start the tool:")
if answer == "yes":

   print("[1]toolsig")
   print("[2]kali linux")
   print("[3]ighack")
   print("[4]mip22")
   print("[5]nexphisher")
   print("[6]zphisher")
   print("[7]infect")
   print("[8]whatsapp bot")
   print("[9]exit")
answer = input("choose your option:")
if answer == "1":

 call(shlex.split('bash hack1.sh'))

if answer == "2":

 call(shlex.split('bash hack2.sh'))
else:

 if answer == "3":

  call(shlex.split('bash hack3.sh'))

if answer == "4":
 call(shlex.split('bash hack4.sh'))
else:

 if answer == "5":

  call(shlex.split('bash hack5.sh'))
 else:

  if answer == "6":

   call(shlex.split('bash hack6.sh'))   

if answer == "7":

 call(shlex.split('bash hack7.sh'))

else:

 if answer == "8":

  call(shlex.split('bash hack8.sh'))

 else:

  if answer == "9":

   call(shlex.split('bash hack9.sh'))
