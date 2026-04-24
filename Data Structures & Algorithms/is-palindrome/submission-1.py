class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointerA = 0
        pointerB = len(s)-1

        while pointerA < pointerB:
            while pointerA < pointerB and not self.alphaNum(s[pointerA]):
                pointerA +=1
            while pointerB > pointerA and not self.alphaNum(s[pointerB]):
                pointerB -= 1
            if s[pointerA].lower() != s[pointerB].lower():
                return False
            pointerA += 1
            pointerB -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            

        