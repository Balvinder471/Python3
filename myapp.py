import pyttsx3 as tts
import os

tts.speak('welcome To the command Execution Service.. What can i do for You?')

while True :
	
	x = input("\nTell me what you want me to do : ")
	x = x.lower()  # making sure no problem occurs if anyone uses capslock or shift

	if (("execute" in x) or ("run" in x) or ("start" in x) or ("access" in x) or ("open" in x)) and (("dont" not in x) and ("do not" not in x) and ("never" not in x)) :
		

		if ("mediaplayer" in x) or ("video player" in x) or ("multimedia" in x) or ("media" in x) :
			tts.speak("Okay Running Mediaplayer")
			os.system("wmplayer")

		elif ("webbrowser" in x) or ("web" in x) or ("browser" in x) or ("internet" in x) or ("website" in x) :
			tts.speak("Okay Opening a Browser")

			if ("www" in x) and ((".com" in x) or (".in" in x) or (".org" in x) or (".edu" in x)):
				x = x.split('.')
				y = x[2].split() # so that we only get the .com part and not all the text after the second .
				os.system('chrome  www.' + x[1] + '.' + y[0])	  # opening a website in the browser if specified

			else :
				os.system('chrome')

		elif ("text editor" in x) or ("notepad" in x) or ("editor" in x) :
			tts.speak("Okay Opening Notepad")
			os.system('notepad')	
 
		else :
			print("OOPS i dont know about that program currently.. sorry about that")
	

	elif ("suggest" in x) or (("what can" in x) and ("do" in x)):
		tts.speak("You can ask me to run some commonly used programs such as a text editor or a browser..")


	elif ("exit" in x) or ("quit" in x) or ("stop" in x) or ((("do not" in x) or ("dont" in x)) and (("continue" in x) or ("carry on" in x))):
		tts.speak("Shutting Down.. Thanks for using this service")
		break


	elif ("clear" in x) or ("clean" in x) :
		tts.speak("Clearing Your Environment")
		os.system('cls')


	elif ("dont" in x) or ("do not"  in x) or ("never" in x):
		tts.speak("Okay i wont do that")	


	else :
		print("Please Specify Your Requirements Clearly..")
