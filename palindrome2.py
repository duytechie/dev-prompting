import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        org_x = x
        rev = 0
        print(f"x is {org_x}")
        # print(f"rev is {rev}")
        
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
            print(f"rev is {rev}")
            print(f"x is {x}")

        print(f"Original x is {org_x}")
        print(f"Rev after loop is {rev}")

        return org_x == rev

class TestSolution(unittest.TestCase):
    def test_is_palindrome(self):
        # Test case 1:
        self.assertTrue(Solution().isPalindrome(121))
        # Test case 2:
        self.assertFalse(Solution().isPalindrome(-121))
        # Test case 3:
        self.assertFalse(Solution().isPalindrome(10))
        # Test case 4:
        self.assertTrue(Solution().isPalindrome(0))

if __name__ == '__main__':
   unittest.main()
    # solution = Solution()
    # result = solution.isPalindrome(0)
    # print(result)
