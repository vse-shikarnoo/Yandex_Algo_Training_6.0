n, k = map(int, input().split())
a = list(map(int, input().split()))

def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        

heap_sort(a)
#print(a)

left=0
right=1

res = 1
t=1
while right<n:

    if a[right]-a[left]<=k:
        right+=1
        t+=1
    else:
        left+=1
        t=right-left
    if t>res:
        res=t
print(res)