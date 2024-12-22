class Solution(object):
    def merge(self, arr, low, mid, high):
        temp = []  
        left = low  
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    def countPairs(self, arr, low, mid, high):
        right = mid + 1
        cnt = 0
        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += (right - (mid + 1))
        return cnt
    def mergeSort(self, arr, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(arr, low, mid)  
        cnt += self.mergeSort(arr, mid + 1, high)  
        cnt += self.countPairs(arr, low, mid, high)  
        self.merge(arr, low, mid, high)
        return cnt
    def reversePairs(self, nums):
        n = len(nums)
        return self.mergeSort(nums, 0, n - 1)
