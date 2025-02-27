def branch_and_bound(weights, bin_capacity):
    n = len(weights)
    best_solution = float('inf')
    best_bins = None

    weights.sort(reverse=True)

    lower_bound = (sum(weights) + bin_capacity - 1) // bin_capacity

    stack = [(0, [[]], weights)]

    while stack:
        bins_used, bins, remaining = stack.pop()

        #pruning if already having a better solution
        if bins_used >= best_solution:
            continue

        if not remaining:
            best_solution = bins_used
            best_bins = bins
            continue

        #taking first item
        item = remaining[0]
        new_remaining = remaining[1:]

        #trial and error placing one by one in existing bins
        for i, bin in enumerate(bins):
            if sum(bin) + item <= bin_capacity:
                new_bins = bins[:i] + [bin + [item]] + bins[i+1:]
                stack.append((bins_used, new_bins, new_remaining))

        new_bins = bins + [[item]]
        stack.append((bins_used + 1, new_bins, new_remaining))

    return best_bins

weights = [10, 20, 15, 25, 30, 5, 10, 20]
bin_capacity = 50
print(branch_and_bound(weights, bin_capacity))
