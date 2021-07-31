startNumber = input("Test all numbers from 1 to this whole number:")
endCondition = [4,2,1,4,2,1]
count = 0
longestCount = 0
longestCountNumber = 0


def test(number):
	global count
	global endCondition
	global longestCount
	global longestCountNumber

	originalNumber = number
	localCount = 0
	numberArray = []
	while numberArray[-6:] != endCondition:
		print(count,localCount, ':', number)
		if number % 2 == 0:
			number = number / 2
		elif number % 2 == 1:
			number = (number * 3) + 1
		numberArray.append(number)

		if (localCount > longestCount):
			longestCount = localCount
			longestCountNumber = originalNumber

		count = count + 1
		localCount = localCount + 1
	return False


for x in range(1, int(startNumber)+1):
	print('Testing number', x)
	runTest = test(x)
	if runTest == True:
		print('Solved with', x) # Pretty optimistic
		break

print('The longest count was', longestCount, 'from number', longestCountNumber)