import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10

class TestSolution(unittest.TestCase):
    def test_is_palindrome(self):
        # Test case 1:
        self.assertTrue(Solution().isPalindrome(121))
        # Test case 2:
        self.assertFalse(Solution().isPalindrome(-121))
        # Test case 3:
        self.assertFalse(Solution().isPalindrome(10))

if __name__ == '__main__':
    unittest.main()
