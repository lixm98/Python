def reverse_string(s):
    return s[::-1]

def keep_only_alphanum(s):
    return ''.join(c for c in s if c.isalnum())
  
def is_palindrome(teststr):
    # Your code goes here.
    unified_case = str.lower(teststr)
    alphanum_str = keep_only_alphanum(unified_case)
    reversed_str = reverse_string(alphanum_str)
    if alphanum_str == reversed_str:
        return True
    else:
        return False
      
test_word1 = "Madam, I'm Adam."
test_word2 = "Hello, World!"
print(is_palindrome(test_word1))  # Should return True
print(is_palindrome(test_word2))  # Should return False

