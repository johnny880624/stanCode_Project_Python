"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	return helper(n, 0)
	# return get_largest_num_helper(n, 0)
	# return find_largest_digit_helper2(n, 0)


def helper(n, max):
	"""
	從後面取過來ex: 281， 找281%10餘數 = 1， 再找28%10餘數 = 8， 再找2%10餘數 = 2
	每次取跟max值比較，取大的最後在return。
	"""
	# abs 代表絕對值
	n = abs(n)
	n1 = n % 10
	n2 = n // 10
	if n1 > max:
		max = n1
	# base case
	if n2 == 0:
		return max
	# recursive case
	else:
		return helper(n2, max)


def get_digit_num_helper(n, count):
	"""
	找出要求的數是幾位數。
	"""
	# base case
	if n == 0:
		return count
	else:
		# recursive case
		return get_digit_num_helper(n//10, count+1)


def get_largest_num_helper(n, max):
	"""
	從前面取過來， ex:281， 281//100取商數 = 2，再來81//10取商數 = 8，再來1//1取商數 = 1。
	每次取每次比較，最後return max。
	"""
	n = abs(n)
	count = get_digit_num_helper(n, 0)
	# divisor = 10**(get_digit_num_helper(n, 0)-1)
	# if n//divisor > max:
	# 	max = n//divisor
	if n//(10**(count-1)) > max:
		max = n//(10**(count-1))
	# base case
	if n//(10**(count-1)) == 0:
	# if n //divisor ==0:
		return max
	else:
		return get_largest_num_helper(n % 10, max)


def find_largest_digit_helper2(n, count):
	"""
	轉換成str，可以更精簡。
	"""
	if len(str(n)) == 1:
		return n
	else:
		if str(n)[0].isdigit():
			if int(str(n)[0]) > int(str(n)[len(str(n))-1]):
				return find_largest_digit(int(str(n)[:len(str(n))-1]))
			else:
				return find_largest_digit(int(str(n)[1:len(str(n))]))

		else:
			n = str(n)[1:]
			n = int(n)
			if int(str(n)[0]) > int(str(n)[len(str(n))-1]):
				return find_largest_digit(int(str(n)[:len(str(n))-1]))
			else:
				return find_largest_digit(int(str(n)[13:len(str(n))]))


if __name__ == '__main__':
	main()
