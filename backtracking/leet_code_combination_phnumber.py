"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""

"""
digits = "23"
out = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


The mapping 

mapper = {2:['a','b','c'], 3:['d','e','f'],4:['g','h','i'],5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}


brute force approach 

using dual loop 

#base case 

if len(digits) == 0:
    return ""




"""


class solution():
    def letter_combinations(digits):
        if not digits:
            return []

        # Define the mapping of digits to letters
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(path)
                return
            
            for letter in mapping[digits[index]]:
                backtrack(index + 1, path + letter)

        combinations = []
        backtrack(0, '')
        return combinations

# Example usage:
sol = solution()
digits = "23"
print(sol.letter_combinations(digits))  # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
