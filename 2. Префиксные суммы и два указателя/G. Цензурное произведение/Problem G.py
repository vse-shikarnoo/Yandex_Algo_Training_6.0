# cook your dish here
n, g = map(int, input().split())
a = input()


cA = 0
cB = 0

maxl=0
grub=0

left=0
right=0


while right<n:
    #print(left,right, maxl)
    #print(cA,cB,grub)
    #print("###########################")
    
    if grub>g:
        while grub>g:
            if a[left]=="a":
                grub-=cB
                cA-=1
            if a[left]=="b":
                cB-=1
            left+=1
    else:
        if a[right]=="a":
            cA+=1
        elif a[right]=="b":
            cB+=1
            grub+=cA
    
    if grub <= g:
        maxl=max(maxl, right-left+1)
        right+=1

print(maxl)
        