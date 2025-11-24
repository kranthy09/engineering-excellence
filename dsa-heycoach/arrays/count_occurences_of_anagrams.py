"""
Count Occurences of Anagrams:

Raman is a keen observer, he can easily see the jumbled words
so one day one of his friend challenged him to count the
occurrences of all the anagrams of string C in a given string S.
Raman accepted the challenge but he is facing some problems in it .
Can you help them ?
"""


# Brute Force
class BruteForceOne:
    def count_anagrams(self, S: str, C: str):
        """
        returns no.of anagrams of C in S
        """

        # BruteForce
        # Find all subsequences of S
        anagram_cnt = 0
        for i in range(len(S) - len(C) + 1):
            subarray = [S[inx] for inx in range(i, i + len(C))]
            is_anagram = True
            found = False
            for j in range(len(C)):
                for k in range(len(subarray)):
                    if C[j] == subarray[k]:
                        found = True
                        subarray[k] = "\0"
                        break
                    else:
                        found = False
                if not found:
                    is_anagram = False
                    break
            if is_anagram:
                anagram_cnt += 1
        return anagram_cnt


# Optimised
class BruteForceTwo:
    def count_anagrams(self, s, c):
        n = len(s)
        count = 0
        for i in range(n - len(c) + 1):
            if self.check_anagrams(s[i : i + len(c)], c):
                count += 1
        return count

    def check_anagrams(self, subs, c):
        chash = {}
        for ele in c:
            if chash.get(ele):
                chash[ele] += 1
            else:
                chash[ele] = 1
        for k in range(len(subs)):
            if chash.get(subs[k]):
                chash[subs[k]] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    S = "fororfrdofr"
    C = "for"
    solution = BruteForceOne()
    answer = BruteForceOne.count_anagrams(S, C)
    print(answer)
