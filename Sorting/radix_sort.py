def radix_sort(collection):
    RADIX = 10
    placement = 1

    max_digit = max(collection)

    while placement<max_digit:
        buckets = [list() for _ in range(RADIX)]

        for i in collection:
            tmp = int((i/placement) % RADIX)
            buckets[tmp].append(i)

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                collection[a] = i
                a+= 1

            placement*=RADIX
