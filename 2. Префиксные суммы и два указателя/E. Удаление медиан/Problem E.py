n = int(input())
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
        
#print(a)
heap_sort(a)
#print(a)

center = int(n/2)
res=[]

if n%2==0:
    left=center-1
    right=center
else:
    left=center-1
    right=center+1
    res.append(a[center])
    
#print(left,right)

while left>=0 and right<=n-1:
    #print(res, left, right)
    res.append(a[left])
    left-=1
    res.append(a[right])
    right+=1
    
print(*res)