"""
A palindrome is a string that is the same read forward or backward.
Example: 'aibohphobia', 'dad'
"""

def naive_palindrome(my_str):
   """Naive Program to check if a string is palindrome or not"""
   # make str suitable for caseless comparison
   my_str = my_str.casefold()
   # reverse the string
   rev_str = reversed(my_str)
   # check if the string is equal to its reverse
   if list(my_str) == list(rev_str):
      print("The string is a palindrome.")
   else:
      print("The string is not a palindrome.")


# DS Aproach
def palindrome(word:str):
   start, end = 0, len(word)-1
   while start < end:
      if word[start] != word[end]:
         return False
      start += 1
      end -= 1
   return True

if __name__ == "__main__":
   my_str = 'aIbohPhoBiA'
   approach = input("Choose a type like naive or ds: ")
   if approach == "naive":
      naive_palindrome(my_str)
   elif approach == "ds":
      palindrome(my_str)
