from sys import argv
#short is a variable to skip through to processing
short = False
season = ""
#python epGenerator.py <number or filename>
if len(argv) == 2:
	#Pass in number
	try:
		episodes = int(argv[1])
		short = True
	#Pass in string for filename
	except ValueError:
		script, filename = argv
#python epGenerator.py <number> <number or filename>
elif len(argv) == 3: 
	try: #Pass in two numbers
		season = argv[1]
		episodes = int(argv[2])
		short = True
	#Pass in string for filename
	except ValueError:
		episodes = int(argv[1])
		filename = argv[2]

#If no arguments given or shortened form
if len(argv) == 1 or short:
	filename = 'output_epGen'
	print 'No filename specified'
	print 'Generating output file %r...' % filename
	
print 'Opening the file %r...' % filename
target = open(filename, 'w')
is_valid_range = False

while(True):
	if short:
		start_num = 1
		break;
	if is_valid_range:
		break;
	if len(season) == 0:
		season = raw_input("Season Number?: ")

	start_num = raw_input("Episode to start counting from (Leave blank for default): ")
	episodes = raw_input("Total number of episodes?: ")

	if len(start_num) == 0:
		start_num = 1
	if (int(start_num) > int(episodes)):
		print 'Error: You are starting passed the number of episodes'
	else:
		is_valid_range = True
	if (start_num == episodes):
		print 'Come on you could have done that yourself...'


print 'Formatting season...'
s = "S"
if (len(season) == 0):
	s += "1"
elif(season < 10):
	s += "0"
season = '() ' + s + season + " "

print 'Writing to file %r...' % filename
for i in range(int(start_num), int(episodes) + 1):
	e = "E"
	if(i < 10):
		e += "0"
	target.write(season + e + str(i))
	target.write("\n")

print 'Closing File...'
target.close()

print 'Done!'

