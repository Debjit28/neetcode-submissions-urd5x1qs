class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_frequency={}
        for i in nums:
            key=i
            if key not in result_frequency:
                result_frequency[key]=0
            result_frequency[key]+=1
        
        pair=[]
        for j in result_frequency:
            pair.append((result_frequency[j],j))

        pair.sort(reverse=True)

        answer=[]
        for i in range(k):
            answer.append(pair[i][1])
        return answer

        
    
    
