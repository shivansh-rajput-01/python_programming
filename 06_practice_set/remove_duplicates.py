# WAF to remove duplicates from list

def r_d(l):
    l = list(set(l))
    return l

l = [1, 1, 2, 2, 3, 3, 3, 4, 5]

print(r_d(l))

# WAF to remove duplicated from list preserving the order


def r_d_s_o(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl

print(r_d_s_o(l))
