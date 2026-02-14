"""
First non repeating characters in stream of characters

Given an input stream "s" containing only lowercase alphabets. while
reading the characters from the stream, you have to tell which character
has appeared only once in the stream upto that point. If there are many
characters that have appeared only once, you have to tell which one of
them was first to appear. If there is no such character, append "#" to
the output.

i/o: "aabbcc"
o/p: "a#b#c#"
"""


class Solution:

    def brute_force(self, stream):
        """
        For each stream of character check from start (0) to
        its index, whether the character is non repeating by
        maitaining frquencies of alphabets.

        TC: O(n^2)
        AS: O(1), even though we are maintaing hashmap,
        it can only extend to a length of 26.
        """
        print(stream)
        n = len(stream)
        res = ""
        hmap = {}
        for i in range(n):
            # variable holds "#" deliverable if no unqiue element
            # obtained from stream
            found = False

            # add the characters in hmap, for checking
            # thier uniqueness over the stream
            if hmap.get(stream[i]):
                # add repeated chars count
                hmap[stream[i]] += 1
            else:
                # add new char found
                hmap[stream[i]] = 1
            for j in range(i+1):

                # check count of each char from start to i
                # if they are unique
                if hmap.get(stream[j]) == 1:
                    # add to result
                    res += stream[j]
                    found = True
                    break

            # if there is no non repeating element,
            # append "#"
            if not found:
                res += "#"
        return res

    def expected_queue(self, stream):
        """
        Maintain queue for storing the elements,
        such that, unique elements are stored in queue
        and removed from left when we see a repeated character
        so that the front element is always, first non repeating

        TC: O(n)
        AS: O(n), for maintaining queue
        """
        from collections import deque

        res = []
        hmap = dict()
        deq = deque()
        for ch in stream:

            # add the char count in hashmap,
            if hmap.get(ch):
                hmap[ch] += 1
            else:
                hmap[ch] = 1
                # if the character is new add to queue such that
                # it can be a non repeating character, from start of
                # stream
                deq.append(ch)
            # remove repeating characters from the queue, so that
            # they cannot contribute to first non repeating until, the
            # queue has first unique at left.
            while deq and hmap[deq[0]] > 1:
                deq.popleft()
            # deq becomes, empty when there are all repeating chars,
            if not deq:
                # in that case append, "#"
                res += "#"
            else:
                # else, append, current front non-repeating character
                # from queue.
                res += deq[0]
        return "".join(res)


if __name__ == "__main__":
    stream = "aajhfhjajaajhfhujdajfnowhuhrg"
    s = Solution()
    print(s.brute_force(stream))
    print(s.expected_queue(stream))
