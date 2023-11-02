class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_list = list(counter.items())

        def quicksort(left,right):
            pivot=random.randint(left,right)
            counter_list[left],counter_list[pivot]=counter_list[pivot],counter_list[left]
            i = left+1
            for j in range(left+1,right+1):
                if counter_list[j][1]>=counter_list[left][1]:
                    counter_list[j],counter_list[i]=counter_list[i],counter_list[j]
                    i+=1
            counter_list[left],counter_list[i-1]=counter_list[i-1],counter_list[left]

            if k==i:
                return
            if k<i:
                quicksort(left,i-2)
            else:
                quicksort(i,right)
        
        quicksort(0,len(counter_list)-1)
        return [counter_list[i][0] for i in range(k)]