class Solution:
    def romanToInt(self, s: str) -> int:
        numeralmapping = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000,
                          "IV": 4,
                          "IX": 9,
                          "XL": 40,
                          "XC": 90,
                          "CD": 400,
                          "CM": 900}
        listsum = []
        testrange = list(range(len(s)))
        for i in list(range(len(s))):
            if i in testrange and i+1 in testrange:
                if s[i:i+2] in list(numeralmapping.keys()):
                    listsum.append(numeralmapping[s[i:i+2]])
                    testrange.remove(i)
                    testrange.remove(i+1)
            if i in testrange:
                listsum.append(numeralmapping[s[i]])
                testrange.remove(i)
        print(listsum)
        return sum(listsum)
test = Solution()
x = test.romanToInt(s="MCMXCIV")
