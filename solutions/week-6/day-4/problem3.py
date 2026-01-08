class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        d1 = self.convert(s1)
        d2 = self.convert(s2)
        return d1 * d2

    def convert(self, s1):
        sign1 = 1
        i0 = -1
        for i in range(len(s1)):
            if s1[i] == "-":
                sign1 = -1
            if s1[i] != "0":
                i0 = i
                break
        s1 = s1[i0:]
        d1 = 0
        i1 = 0
        while i1 < len(s1):
            if s1[i1] == "-":
                i1 += 1
                continue
            d1 = d1*10 + (ord(s1[i1])-ord('0'))
            i1 += 1
        d1 = sign1 * d1
        return d1
