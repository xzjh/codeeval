import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	data = map(int, test.strip().split(','))
	if (data[0] >> (max(data[1], data[2]) - 1)) == 0:
		print 'false'
		continue
	if (data[0] >> (data[1] - 1)) % 2 == (data[0] >> (data[2] - 1)) % 2:
		print 'true'
	else:
		print 'false'

test_cases.close()