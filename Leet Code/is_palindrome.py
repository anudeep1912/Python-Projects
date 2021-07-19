# Given a string s, determine if it is a palindrome, considering only alphanumeric characters
# and ignoring cases.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome_mysolution (s) -> bool:
    # 572 ms speed.
    words = s.split()
    sentence_without_spaces = "".join(words)
    final = sentence_without_spaces.lower()

    for i in final:
        if not i.isalnum():
            final = final.replace(i, "")

    if final == final[::-1]:
        return True
    else:
        return False

def isPalindrome_solution_1 (s):
    #time = 56ms
    news = ''
    for w in s:
        if (w.isalpha()): news += str(w.lower())
    return news == news[::-1]

def isPalindrome_solution_2 (s):
    #time = 28ms fastest
    clean_s = ''.join(filter(str.isalnum, s)).lower()
    return clean_s == clean_s[::-1]
