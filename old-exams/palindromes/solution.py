# Write your solution in this file


def isPalindrome(s):
    return s == s[::-1]

file_in = open(r'/Users/greek/PycharmProjects/exercises/old-exams/palindromes/input.txt', 'r+')
file_out = open(r'/Users/greek/PycharmProjects/exercises/old-exams/palindromes/output.txt', 'a')
file_out.truncate(0)
with open('input.txt') as temp_file:
  woorden = [line.rstrip('\n') for line in temp_file]
  with open('output.txt','w') as out:
      for word in woorden:
          if isPalindrome(word) == True:
              out.write(word + '\n')