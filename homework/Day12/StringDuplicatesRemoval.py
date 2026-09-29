class Solution:
	def removeDuplicates(self, s):
		set_s=set()
		res = []
		for i in s:
			if i not in set_s:
				set_s.add(i)
				res.append(i)
		k = "".join(res)
		return k