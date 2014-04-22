from sys import argv
script, filename = argv

print 'Opening the file %r...' % filename
target = open(filename, 'w')

season = raw_input("Season Number?: ")
episodes = raw_input("Number of episodes?: ")

print 'Formatting season...'
s = "S"
if(season < 10):
	s += "0"
season = s + season + " "

print 'Concatenating strings...'
for i in range(int(episodes)):
	ep = i + 1 
	e = "E"
	if(ep < 10):
		e += "0"
	target.write(season + e + str(ep))
	target.write("\n")

print 'Closing File...'
target.close()

print 'Done!'

