"""
File: Milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    if name not in name_data:
        name_data[name][year] = rank
    else:
        if year not in name_data[name]:
            name_data[name][year] = rank
        else:
            rank_original = name_data[name][year]
            if int(rank_original) > int(rank):
                name_data[name][year] = rank

    # year_rank = {}
    # if name not in name_data:
    #     year_rank[year] = rank
    #     name_data[name] = year_rank
    # else:
    #     if year not in year_rank:
    #         name_data[name][year] = rank
    #     else:
    #         rank_original = name_data[name][year]
    #         if int(rank_original) > int(rank):
    #             name_data[name][year] = rank


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #
def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')




def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
