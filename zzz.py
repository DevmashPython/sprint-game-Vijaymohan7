import msvcrt
import time

finish1=6
finish2=10
finish3=15

count=0


print "enter to get started"

raw_input()
s_time=time.time()

while(1):
	key=msvcrt.getch()
	if key=='d':
		if count < 6:

			count=count+1
			print "---",
			if count==finish1:
				print "|"
		elif count >9:
			
			count=count+1
			
			if count==finish3:
				print "\t\t\t---------------"
					
				

			
		
	elif key=='s':
		count=count+1
		if count < 11:
			print "\t\t\t|\n"
			if count==finish2:
				print "go right"

	

			

	

time_elapsed=time.time()-s_time
print "comgrats you have finished the game"
print "time takem is"+str(time_elapsed)
