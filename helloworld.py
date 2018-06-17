f = open('text.txt')
count = 0
for line in f:
	if 'hello world!' in line:
		print 'Found "' + line + '"',
	else:
		count += 1

f.close()

print 'Counted ' + str(count) + ' lines besides "hello world"'
