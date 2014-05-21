import os

for f in os.listdir(os.getcwd()):
	if f.endswith(".avi") | f.endswith(".mp4") | f.endswith(".wmv") | f.endswith(".mkv"):
		try:
			start = f.index("[")
			end = f.index("]")
			name = f[start + 1: end]
			file = open(name + '.txt', 'w')
		except ValueError:
			print 'Whoops! Substring not found'
