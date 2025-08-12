def bucket_sort_letters(arr):
    # Create buckets for 'a', 'b', and 'c'
    buckets = {
        'a': [],
        'b': [],
        'c': []
    }

    # Distribute elements into buckets
    for letter in arr:
        if letter in buckets:
            buckets[letter].append(letter)
        else:
            raise ValueError(f"Invalid value: {letter}")

    # Concatenate buckets in sorted order
    sorted_arr = buckets['a'] + buckets['b'] + buckets['c']
    return sorted_arr


# Example usage
data = ['b', 'c', 'a', 'b', 'a', 'c', 'a']
sorted_data = bucket_sort_letters(data)
print(sorted_data)  # Output: ['a', 'a', 'a', 'b', 'b', 'c', 'c']

def bucket_sort_abc(values, order=("a", "b", "c")):
    if len(set(order)) != len(order):
        raise ValueError("Order must not contain duplicates.")

    buckets = {k: [] for k in order}

    for v in values:
        if v not in buckets:
            raise ValueError(
                f"Value {v!r} not allowed. Allowed: {list(order)}"
            )
        buckets[v].append(v)

    out = []
    for key in order:
        out.extend(buckets[key])
    return out

data = ['b', 'c', 'a', 'b', 'a', 'c', 'a']
sorted_data = bucket_sort_abc(data)
print(sorted_data)  # Output: ['a', 'a', 'a', 'b', 'b', 'c', 'c']
