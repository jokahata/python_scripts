from sys import argv
script, filename = argv

print 'Opening the file %r...' % filename
target = open(filename, 'w')

season = raw_input("Season Number?: ")
episodes = raw_input("Number of episodes?: ")
start_num = raw_input("Episode to start counting from (Leave blank for default): ")
if len(start_num) == 0:
	start_num = 1

print 'Formatting season...'
s = "S"
if(season < 10):
	s += "0"
season = s + season + " "

print 'Concatenating strings...'
for i in range(int(start_num), int(episodes) + 1):
	e = "E"
	if(i < 10):
		e += "0"
	target.write(season + e + str(i))
	target.write("\n")

print 'Closing File...'
target.close()

print 'Done!'

