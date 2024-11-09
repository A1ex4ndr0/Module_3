data_structure = ([
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
],
5,
{'peoples': [5, '7'], 12: {2: 'gold'}})

def calculate_structure_sum(structure_):
    result_ = 0
    for i in structure_:
        if isinstance(i, str):
            result_ += len(i)
        elif isinstance(i, int):
            result_ += i
        elif isinstance(i, dict):
            for j in i.items():
                result_ += calculate_structure_sum(j)
        else:
           result_ += calculate_structure_sum(i)
    return result_

print(calculate_structure_sum(data_structure))
