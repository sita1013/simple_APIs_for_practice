# import sys

# lines = [line.strip().split() for line in sys.stdin]

if len(lines) >= 2:
    set1 = lines[0]
    set2 = lines[1]

    # Preallocate common array (max size = len(set1))
    common = [None] * len(set1)
    count = 0

    # Build common values manually
    i = 0
    while i < len(set1):
        j = 0
        while j < len(set2):
            if set1[i] == set2[j]:
                # Check duplicates
                k = 0
                duplicate = False
                while k < count:
                    if common[k] == set1[i]:
                        duplicate = True
                        break
                    k += 1
                if not duplicate:
                    common[count] = set1[i]
                    count += 1
                break
            j += 1
        i += 1

    if count == 0:
        print("NULL")
    else:
        # Manual bubble sort
        m = 0
        while m < count - 1:
            n = 0
            while n < count - 1 - m:
                a = common[n]
                b = common[n+1]

                # Check if a string is numeric
                def is_number(s):
                    idx = 0
                    while idx < len(s):
                        if not ('0' <= s[idx] <= '9'):
                            return False
                        idx += 1
                    return True

                a_num = is_number(a)
                b_num = is_number(b)

                if a_num and b_num:
                    if int(a) > int(b):
                        common[n], common[n+1] = b, a
                elif a_num and not b_num:
                    # numbers stay before letters, so do nothing
                    pass
                elif not a_num and b_num:
                    # swap because letter should come after number
                    common[n], common[n+1] = b, a
                else:
                    # both are letters, compare lexicographically
                    if a > b:
                        common[n], common[n+1] = b, a
                n += 1
            m += 1

        # Build output manually
        result = ""
        p = 0
        while p < count:
            result += common[p]
            if p < count - 1:
                result += " "
            p += 1
        print(result)
