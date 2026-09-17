class Solution:
    def uniqueOccurrences(self, arr):
        frequency = {}

        for x in arr:
            frequency[x] = frequency.get(x, 0) + 1

        seen = set()

        for count in frequency.values():
            if count in seen:
                return False

            seen.add(count)

        return True