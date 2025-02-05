import heapq

def first_fit(n, c, l):
    bins = []
    bin_count = 0

    for item in l:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= item:
                bins[i] -= item
                placed = True
                break

        if not placed:
            # Use a new bin
            bins.append(c - item)
            bin_count += 1

    return len(bins)
    
# O(n log n) approach
def best_fit(n, c, l):
    bins = []

    for item in l:
        found_bin = None
        new_heap = []

        while bins:
            bin_capacity = heapq.heappop(bins)
            if bin_capacity >= item and found_bin is None:
                found_bin = bin_capacity - item
            else:
                new_heap.append(bin_capacity)
                
        if found_bin is not None:
            heapq.heappush(new_heap, found_bin)

        if found_bin is None:
            heapq.heappush(new_heap, c - item)
        bins = new_heap

    return len(bins)

t=int(input())

for x in range(t):
    n,c=map(int,input().split())
    l=list(map(int,input().split()))
    res1=first_fit(n,c,l)
    res2=best_fit(n,c,l)
    print(res1,res2)
    