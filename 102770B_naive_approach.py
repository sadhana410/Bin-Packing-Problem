import math as m

def first_fit(n,c,l):
    bin_count=0
    bins=[c]*n
    curr_bin=0
    for i in range(n):
        while (curr_bin<n):
            diff=bins[curr_bin]-l[i]
            if diff>=0:
                bins[curr_bin]-=l[i]
                break
            else:
                curr_bin+=1
    #print(bins)            
    for i in range(1,n):
        if bins[i-1]<c and bins[i]==c:
            bin_count=i
    return bin_count

def best_fit(n,c,l):
    bins=[c]*n #worst case one item in a separate bin
    bin_count=0
    for i in range(n):
        curr_bin=0
        min_diff=m.inf
        min_ind=None
        while (curr_bin<n):
            diff=bins[curr_bin]-l[i]
            if diff>=0 and diff<min_diff:
                min_diff=diff
                min_ind=curr_bin
            else:
                curr_bin+=1
        bins[min_ind]-=l[i]
        
    for i in range(1,n):
        if bins[i-1]<c and bins[i]==c:
            bin_count=i
    return bin_count
    

t=int(input())

for x in range(t):
    n,c=map(int,input().split())
    l=list(map(int,input().split()))
    res1=first_fit(n,c,l)
    res2=best_fit(n,c,l)
    if res1==0:
        res1=n
    if res2==0:
        res2=n
    print(res1,res2)
    