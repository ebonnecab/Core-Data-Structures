#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

def clean_text(text):
    #ignore casing, whitespace, punctuation
    text = text.casefold().replace(" ", "")
    remove_punct = str.maketrans("","", string.punctuation)
    text = text.translate(remove_punct)

    return text

def is_palindrome_iterative(text):
    #implement the is_palindrome function iteratively here
    '''Runtime is O(n) because....(fill out later)'''
    #ignore casing, whitespace, punctuation
    if text:
        text = clean_text(text)
    else:
        raise Exception('empty string')
    #better solution
    first = 0
    last = len(text)-1

    while last > first: #O(n) /2 => O(n)
        if text[last] != text[first]:
            return False
        first+=1
        last-= 1
    return True
   
    


def is_palindrome_recursive(text, left=None, right=None):
    #implement the is_palindrome function recursively here
    if text == "":
        return True
    
    text = clean_text(text)

    if left is None and right is None:
        left = 0
        right = len(text)-1
    
    if left > right:
        return True
    
    if text[left] != text[right]:
        return False
    
    return is_palindrome_recursive(text, left=left+1, right=right-1)
  
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
