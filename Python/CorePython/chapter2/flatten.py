res = []

def flatten(lst):
    for sub in lst:
        try:
            flatten(sub)
        except TypeError:
            res.append(sub)

source = [1, 3, [3, 45, 13123, [2, 3], 234, [213]], 2, 1]
flatten(source)
print(res)