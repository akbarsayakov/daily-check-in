class Solution:
  def  freqLetters(self, s: str) -> str:
    countS = {}
    for i in range(len(s)):
      if s[i].isalpha():
        countS[s[i]] = countS.get(s[i], 0) + int(s[i+1])
    print(countS)
    res = ''
    for k in countS:
      res = res + k + str(countS[k])
    print(res)

sol = Solution()
sol.freqLetters('a3c4a1b4c7')