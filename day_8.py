# -*- coding: utf-8 -*-
"""
Advent of Code: Day 8
"""

def number_converter(sample):
    numbers = sample.split('|')[0].split()
    codes = sample.split('|')[1].split()
    
    decode = {
        'a':'',
        'b':'',
        'c':'',
        'd':'',
        'e':'',
        'f':'',
        'g':''
        }
    
    code_to_number = {
        '0':'abcefg',
        '1':'cf',
        '2':'acdeg',
        '3':'acdfg',
        '4':'bcdf',
        '5':'abdfg',
        '6':'abdefg',
        '7':'acf',
        '8':'abcdefg',
        '9':'abcdfg'
        }
    
    b_or_d = []
    g_or_e = []
    
    # get 'f' and 'c' equilvalents:
    for num in numbers:
        if len(num) == 2:
            for num2 in numbers:
                if len(num2) == 6:
                    if num[0] in num2 and num[1] not in num2:
                        decode['f'] = num[0]
                        decode['c'] = num[1]
                    elif num[1] in num2 and num[0] not in num2:
                        decode['f'] = num[1]
                        decode['c'] = num[0]
    # get 'a' equivalent:
    for num in numbers:
        if len(num) == 3:
            for char in list(num):
                if char not in decode.values():
                    decode['a'] = char
    # get 'd' and 'b' equivalents:
    for num in numbers:
        if len(num) == 4:
            for char in list(num):
                if char not in decode.values():
                    b_or_d.append(char)
            for num2 in numbers:
                if len(num2) == 5:
                    if b_or_d[0] in num2 and b_or_d[1] not in num2:
                        decode['d'] = b_or_d[0]
                        decode['b'] = b_or_d[1]
                    elif b_or_d[1] in num2 and b_or_d[0] not in num2:
                        decode['d'] = b_or_d[1]
                        decode['b'] = b_or_d[0]
    # get 'g' and 'e' equivalents:
    for num in numbers:
        if len(num) == 7:
            for char in list(num):
                if char not in decode.values():
                    g_or_e.append(char)
            for num2 in numbers:
                if len(num2) == 6:
                    if g_or_e[0] in num2 and g_or_e[1] not in num2:
                        decode['g'] = g_or_e[0]
                        decode['e'] = g_or_e[1]
                    elif g_or_e[1] in num2 and g_or_e[0] not in num2:
                        decode['g'] = g_or_e[1]
                        decode['e'] = g_or_e[0]
                        
    # Converting the code to values:
    new_codes = []
    for code in codes:
        for num in range(0, len(decode)):
            code = code.replace(list(decode.values())[num], str(num))
        for num in range(0, len(decode)):
            code = code.replace(str(num), list(decode.keys())[num])
        new_codes.append(code)
                        
    sorted_codes = []
    for code in new_codes:
        sorted_codes.append(''.join(sorted(code)))
                        
    result = ''
    for code in sorted_codes:
        key = next(key for key, value in code_to_number.items() if value == code)
        result += key
    return result
                    
# sample = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'                    
# print(number_converter(sample))                    
                
big_sample = [
'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
]
                
answer_1 = ''
for sample in big_sample:
    answer_1 += number_converter(sample)
                
part_1 = answer_1.count('1') + answer_1.count('4') + answer_1.count('7') + answer_1.count('8')
print(part_1)

answer_2 = 0
for sample in input_sample.split('\n'):
    answer_2 += int(number_converter(sample))
print(answer_2)












