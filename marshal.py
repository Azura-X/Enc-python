#!/usr/bin/python1.7
#coding=utf-8
import marshal,os,sys,time

aleju = ("""\x1b[92m
     ╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐┬
     ║║║├─┤├┬┘└─┐├─┤├─┤│
     ╩ ╩┴ ┴┴└─└─┘┴ ┴┴ ┴┴─┘\x1b[00m
     Author : Aleeju\n""")
def aleeju():
	try:
		print (aleju)
		print ('\x1b[00mExample > /sdcard/file.py')
		file = input ('\x1b[00myour file:\x1b[92m')
		fileopen = open(file).read()
		a = compile(fileopen, 'dg', 'exec')
		m = marshal.dumps(a)
		s = repr(m)
		b = ('import marshal\nexec(marshal.loads(' + s +'))')
		c = file.replace('.py', '-enc.py')
		d = open(c, 'w')
		d.write(b)
		d.close()
		print ('\x1b[00mHasil > \x1b[92m',c)
		time.sleep(1)
		aq = input ('\x1b[00mIngin encrypt lagi? [\x1b[92mY\x1b[00m/\x1b[91mN\x1b[00m]')
		if aq =="":
			print ('\x1b[91mCommand not found !')
			os.sys.exit()
		elif aq =="y" or aq =="Y":
			aleeju()
		else:
			if aq =="n" or aq =="N":
				print ('\x1b[91mTerimakasih anjeng ;v')
			else:
				print ('\x1b[91mCommand not found !')
				os.sys.exit()
	except IOError:
		print ('\x1b[91mFile Tidak Ditemukan !\x1b[00m')
		time.sleep(1)
		aleeju()

if __name__=='__main__':
	aleeju()
