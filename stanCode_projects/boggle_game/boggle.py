"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []


def main():
	"""
	TODO:
	"""
	result_lst = []
	empty_lst = []
	lst_all = []
	read_dictionary()
	f_row = input('1 row of letter: ')
	s_row = input('2 row of letter: ')
	t_row = input('3 row of letter: ')
	l_row = input('4 row of letter: ')
	f_row = f_row.lower().split()
	s_row = s_row.lower().split()
	t_row = t_row.lower().split()
	l_row = l_row.lower().split()
	lst_all.append(f_row)
	lst_all.append(s_row)
	lst_all.append(t_row)
	lst_all.append(l_row)
	word_x = 0
	word_y = 0
	find_all_words(lst_all, empty_lst, result_lst, word_x, word_y)


def find_all_words(lst_all, empty_lst, result_lst, word_x, word_y):
	helper(lst_all, '', empty_lst, result_lst, word_x, word_y)


def helper(lst_all, currrent_s, empty_lst,result_lst, a, b):
	# base case
	if len(currrent_s) == 4:
		if currrent_s in dict_list:
			if currrent_s not in result_lst:
				print('Found', currrent_s)
				result_lst.append(currrent_s)
	else:
		print('Searching...')
		for x in range(len(lst_all)):
			for y in range(len(lst_all[x])):
				for i in range(-1, 2):
					for j in range(-1, 2):
						word_x = a + x + i
						word_y = b + y + j
						if 0 <= word_x < len(lst_all):
							if 0 <= word_y < len(lst_all[x]):
								word = lst_all[word_x][word_y]
								if [word_x, word_y] not in empty_lst:
									empty_lst.append([word_x, word_y])
									if has_prefix(currrent_s) is True:
										helper(lst_all, currrent_s + lst_all[word_x][word_y], empty_lst, result_lst, word_x, word_y)
										empty_lst.pop()
									else:
										empty_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_list
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			dict_list.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if str(word).startswith(sub_s) is True:
			return True
		else:
			pass


if __name__ == '__main__':
	main()
