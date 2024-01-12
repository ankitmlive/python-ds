import unittest
"""
A string rotation check can be simply identitifed by repeating a string and all the word will be rotated in the string.
String: "ankit" => "nkita" => "kitan" => "itank" => "tanki"
multiply the original string => "ankit" *2 => "ankitankit" => In this new string all the string above will exist
"""

def check_rotation(s1, s2):
  if len(s1) == len(s2):
    return s2 in s1*2
  return False


class Test(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
