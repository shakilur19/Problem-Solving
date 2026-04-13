class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        ans = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        print(even, odd)
        
        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])
        
        print(ans)
            

        return ans