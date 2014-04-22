from sys import argv
script, filename = argv

print 'Opening the file %r...' % filename
target = open(filename, 'w')
is_valid_range = False
season = raw_input("Season Number?: ")

while(not is_valid_range):
	start_num = raw_input("Episode to start counting from (Leave blank for default): ")
	episodes = raw_input("Total number of episodes?: ")
	if len(start_num) == 0:
		start_num = 1
	if (start_num > episodes):
		print 'Error: You starting passed the number of episodes'
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
season = s + season + " "

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

