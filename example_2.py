"""X butun soni berilgan bo'lsa, agar x a bo'lsa, true qiymatini qaytaring
palindrom
, aks holda false."""

# bu dasturda x biror bir son kiritsak uni palindrom yoki palindrom emasligini anqilab beradi misol: 121 palindrome


class Solution:
    def __init__(self, x):
        self.x = x

    def ispalindrome(self):
        d = []
        xx = ""
        for i in self.x:
            d.append(i)
        d.reverse()
        for j in d:
            xx += j
        if xx == self.x:
            print("palindrome")
        else:
            print(False)


x = input("insert x= ")
data = Solution(x)
data.ispalindrome()
