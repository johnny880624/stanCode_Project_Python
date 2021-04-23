"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []
# anagram_list = []
# anagram_number = 0


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        s = input('Find anagrams for:')
        s = s.lower()
        if s == EXIT:
            break
        else:
            lst = []
            anagram_list = []
            find_anagrams(s, anagram_list, lst)
            anagram_number = len(anagram_list)
            print(anagram_number, 'anagram(s):', anagram_list)
    # s = 'eraser'
    # anagram_list = []
    # find_anagrams(s, anagram_list)
    # s = 'stop'
    # lst = []
    # anagram_list = []
    # find_anagrams(s, anagram_list, lst)


def read_dictionary():
    # 這裡要先宣稱 才會改變全域變數的dict_list.
    global dict_list
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            dict_list.append(word)


def find_anagrams(s, anagram_list, lst):
    """
    :param s:
    :return:
    """
    helper(s, '', anagram_list, lst)


# s為輸入進去的string, current_s為空字串
def helper(s, current_s, anagram_list, lst):
    global dict_list
    # global anagram_list
    # global anagram_number
    # read_dictionary()
    # base case
    if len(current_s) == len(s):
        if current_s not in anagram_list:
            if current_s in dict_list:
                print('Found', current_s)
                anagram_list.append(current_s)
                print('Searching...')
    else:
        for i in range(len(s)):
            word = s[i]
            if i not in lst:
                lst.append(i)
                # has_prefix(current_s)
                # choose
                # explore
                if has_prefix(current_s) is True:
                    current_s += s[i]
                    helper(s, current_s, anagram_list, lst)
                    lst.pop()
                    current_s = current_s[:-1]
                # un_choose
                # current_s = current_s.strip()
                else:
                    lst.pop()


def has_prefix(sub_s):
    global dict_list
    """
    :param sub_s:
    :return:
    """
    # read_dictionary()
    for word in dict_list:
        if str(word).startswith(sub_s) is True:
            return True
        else:
            pass


if __name__ == '__main__':
    main()
