class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            max_num = 0
            for j in range(i+1,len(arr)):
                if arr[j] > max_num:
                    max_num = arr[j]
            arr[i] = max_num
        arr[-1] = -1
        return arr


            

        