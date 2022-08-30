import random, os, datetime
from playsound import playsound 

def rph(randomhasslist):                                                                                      # for password
	 r=random.choice(randomhasslist)
	 return r

def password(password):                                                                                       # password to hashpassword
	rl=[]
	l=[]
	for pw in range(len(password)):
		l.append(password[pw])

	randomhasslist='abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&/'
	for ral in range(len(randomhasslist)):
		rl.append(randomhasslist[ral])
	hashp=[]
	for a in range(len(password)):
		for b in range(5):
			hashp.append(rph(randomhasslist))
		hashp.append(l[a])
	last=str(len(password))
	for ax in range(4):
		hashp.append(rph(randomhasslist))
	hashp.append(f"'{last}")
	hashpassword=''
	for has in hashp:
		hashpassword = hashpassword + has
	return hashpassword

def hash(userhash):                                                                                          #hashpassword to password
	hashpassword=userhash
	password=''
	last=hashpassword.split("'")
	hashp=last[0]
	hashlist=[]
	for li in range(len(hashp)):
		hashlist.append(hashp[li])
	intlast=int(last[1])
	i=0
	for a in range(len(hashlist)):
		if a%5==0:
			if len(password)==intlast:
				pass;
			elif 1<a<len(hashlist)-3:
				b=a+i
				i=i+1
				password=password+hashlist[b]
	return password

def reads():                                               											       #read all id's for match user id
	with open('idstor.txt') as read:
		r=read.read()
		return r

def appends(value):                                            											   #stor new user id's
	with open('idstor.txt','a') as append:
		a=append.write(value)

def diarynamestor(user):                                           										   #stor diary names
	diarynamestor=''
	with open(f'{user}//{user}_records.txt') as diarynameread:
		diarynameread.readline()
		diarynamestor=diarynameread.readline()
		diarynamelist=diarynamestor.split(',')
	return diarynamelist

def WriteHistory(writevalue):                                           								   #write user history
	with open(f'{userl[0]}//{userl[0]}_history.txt' , "a") as wrhis:
		wrhis.write(writevalue)

def readHistory():                                                   								       #read user history
	a=''
	with open(f'{userl[0]}//{userl[0]}_history.txt') as rdhis:
		a=rdhis.read()
	return a

def Writerecords(writevalue):                                             							      #stor user diary name
	with open(f'{userl[0]}//{userl[0]}_records.txt' , "a") as wrrec:
		wrrec.write(writevalue)




while True:
	log=input('''
|__________ WELCOME_TO_MyDiary.com __________|
    1 for log in
    2 for sign in 
    3 EXIT
	-''')

	if log=='1':                                                                                   #log in start
		playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
		r=reads()                                                                   				#read id's
		userl=[]					
		ls=[]																					#stor id's in list
		l=r.split('\n')

		for el in l:
			a=el.split('\\')
			ls.append(a)
		p=1
		while True:
			print('(Notes- Enter Q for back)')
			user=input("user name\n: ")													#match username
			if user=="Q" or user=='q':
				break;

			elif user=='':
				pass;

			elif ' ' not in user: 
				for a in range(len(ls)):
					if user==ls[a][0]: 
						userl=ls[a]
						break;

			if len(userl)==0 and p<5:												#wrong username
				print('invalid user name')
				p+=1

			elif p==5:																#forget username
				print('forget username')
				f=0
				forget_email=input('Emter you email: ')
				if "@" in forget_email and "." in forget_email: 
					for a in range(len(ls)-1):
						if forget_email==ls[a][1]: 
							print(f'your username is {ls[a][0]}')
							f=1
				if f==0:
					print('email not used enter valid email')
					break;
				break;

			if len(userl)>0:
				break;

		if len(userl)>0:
			i=1
			while i<=6:
				if i<6:																#match password
					userpassword=input("enter password: ")
					z=0
					while z==0:
						userhash=userl[2]
						realpassword=hash(userhash)
						if userpassword==realpassword:
							while True:
								work=input(f''' 
Hallo dear, {userl[0]}
	WELCOME to MyDiary.com
	1 for Create Diary
	2 for Open Diary
	3 for Show Diary
	4 for Show history
	5 for Delete Diary
	6 for Exit or LOG-out
	-''')																												#open user id for work
								diarynamelist=diarynamestor(user)
								if work=='1':																						#creat diary
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									print('(Notes- Enter Q for back)')
									diaryname=input('Enter Diary name: ')
									con=0
									if diaryname=="q" or diarynamelist=="Q":
										break;
									for a in range(len(diarynamelist)-1):
										if diarynamelist[a]==(f'{diaryname}.txt'):												#match unique name
											con=con+1
									if con==0:
										with open(f'{userl[0]}//diary//{diaryname}.txt', "w") as new:							#creat new diary
											new.write(f"Dear, {diaryname}\n")
										print("yes, your diarys create")
										WriteHistory(f'{str(datetime.datetime.now())}\nCreate Diary {diaryname}.txt\n\n')    	#write history
										Writerecords(f'{diaryname}.txt,')														#write records
									else:
										print('this diary already exist')


								elif work=='2':																							#open diary
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									if len(diarynamelist)==1:
										print("Empaty no diary")
									else:
										print("_____Diaries____")
										for re in range(len(diarynamelist)-1):														#show diaries
											print(f'{re+1} for {diarynamelist[re]}')
										print('Q for Back')
										print('')
										opendiaryint=input('enter diary code - ')
										print(len(diarynamelist)-1)
										if opendiaryint=="q" or opendiaryint=="Q":
											break;
										elif 0>int(opendiaryint)>len(diarynamelist)-1:
											print('Enter valid code')
										else:
											while True:
												opendiary=diarynamelist[int((opendiaryint))-1]												#open diary work
												opendiarywork=input('''
				1 for Write
				2 for Read
				3 for Remove all content
				4 for Back
				   -''')
												if opendiarywork=="1":																					#write content in diary
													playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
													print('(Notes- Enter Q for back)')
													writecontent=input('Write (press Enter for save)\n')
													if writecontent=="q" or writecontent=="Q":
														break;
													else:
														with open(f'{user}//diary//{opendiary}', 'a') as wrindiary:										#write content in diary
															wrindiary.write(f'{writecontent}\n')
														WriteHistory(f'{str(datetime.datetime.now())}\nWrite in {opendiary}-\n{writecontent}\n\n')      #write history
														print('------------------------------------>')
														print('              DONE     Write content')
												elif opendiarywork=="2":																					#read content in diary
													playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
													with open(f'{user}//diary//{opendiary}') as rdindiary:
														print('----------------------------------------->')
														print(rdindiary.read())
														print('----------------------------------------->')
												elif opendiarywork=="3":																					#remove content in diary
													perforrm=input("Y/N- ")
													if perforrm=="y" or perforrm=="Y":
														rmcontent=''
														with open(f'{user}//diary//{opendiary}') as rm:
															rmcontent=rm.read()
														x=opendiary.replace(".txt", "")
														with open(f'{user}//diary//{opendiary}', 'w') as wrindiary:     									#write (dear diary) in diary
															wrindiary.write(f'Dear, {x} \n')
														WriteHistory(f'{str(datetime.datetime.now())}\nRemove content in {opendiary}-\n{rmcontent}\n\n')		#write history
														print("Content Remove")
													else:
														pass;

												else:																											#for back
													playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
													break;
											break;

								elif work=='3':																													#show list of diary
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									if len(diarynamelist)==1:
										print("Empaty no diary")
									else:
										print('')
										print("_____Diaries____")
										for re in diarynamelist:
											print(re)
								elif work=='4':																													#show history
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									showhistory=readHistory()
									print('------------------------------>')
									print('            HISTORY')
									print(showhistory)
									print('<------------------------------')
								elif work=='5':																													#delete diary
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									if len(diarynamelist)==1:
										print("Empaty no diary")
									else:
										print("_____Diaries____")																#show diary for delete menu
										for re in range(len(diarynamelist)-1):
											print(f'{re+1} for {diarynamelist[re]}')
										print('Q for Back')
										print('')
										opendiaryint=input('enter diary code - ')
										if opendiaryint=="q" or opendiaryint=="Q":
											break;
										else:																					#delete diary start
											opendiary=diarynamelist[int((opendiaryint))-1]
											decon=input('Y/N- ')
											if decon=='y' or decon=='Y':
												in_diary_content=''
												with open(f'{user}//diary//{opendiary}') as rmdiary:						                   		#remove diary content
													in_diary_content=rmdiary.read()
												os.remove(f'{user}//diary//{opendiary}')																#remove diary
												WriteHistory(f'{str(datetime.datetime.now())}\nRemove {opendiary} diary-\n{in_diary_content}\n\n')			#write history
												rmdiaryname=''
												with open(f'{user}//{user}_records.txt') as rmname:														#remove diary in records
													rmdiaryname=rmname.read()
												x=rmdiaryname.replace(f'{opendiary},', '')
												with open(f'{user}//{user}_records.txt', 'w') as wrname:
													wrname.write(x)

												print('Diary Remove')
											else:
												break;
								elif work=='6':																												#for exit
									playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
									c=input('Y/N- ')																										#exit confirmation
									if c=="Y" or c=="y":
										playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
										print('EXIT')
										exit()
									else:
										playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
										break;
								else:																														#invalid entery
									print('enter only 1, 2, 3, 4, 5 or 6')


						elif i<6:																													#incorrect password more then 5 time
							print('incorrect password')
							i += 1
							z += 1
				else:
					break;
                                                                                                                                #log in end
	elif log=='2':                                                                                            #sign in start
		playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
		r=reads()
		i=1
		while i==1: 
			print('''
	CREATE_LOG_IN_ID
(NOTE- when you enter only q means back to )''')

			email=''
			while i==1:
				em=input('enter e-mail: ')																	#enter e-mail
				if "@" in em and "." in em:
					email=em
					break;
				elif em=="q" or em=="Q":
					i=i+1
					break
				else:
					print('enter valid email addres')

			username=''
			while i==1:																						#enter unique username
				u=input('enter user_name (without space)\n-')
				if " " in u or u=='':
					print('without space')

				elif u=="q" or u=="Q":
					i=i+1
					break;

				elif u in r:
					print("this user name is already use")
					pass;
				
				else:
					username=u
					break;

			while i==1:																					#enter password
				enterpassword=input("enter password: ")
				hashpassword= password(enterpassword)													#password to hashpassword
				os.mkdir(username)																		#creat new user folder
				os.mkdir(f'{username}//diary')
				appends(f'{username}\\{email}\\{hashpassword}\n')     									#stor new user information
				mkdate=str(datetime.datetime.now())
				with open(f'{username}//{username}_records.txt', 'w') as op:							#write new user records
					op.write(f'Open Date and time {mkdate}\n')
				with open(f'{username}//{username}_history.txt', 'w') as op:							#write new user history
					op.write(f'Open Date and time {mkdate}\n\n')
				print("sing in successfully log in again")
				break	
			break;
                                                                                                            #sign in end
	elif log=='3':                                                                                 #for exit
		playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
		con=input('Y/N-')                                                                           #exit confirmation
		if con=='Y' or con=='y':
			playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
			print('EXIT')
			exit()
		else:
			playsound("C:\\Users\\UJJWAL\\Music\\Menu_Game_Button_Click_Sound_Effect(128k).mp3")
			print('hallo')
	else:
		print('invalid entry')
		