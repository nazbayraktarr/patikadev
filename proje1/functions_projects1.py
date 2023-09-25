input_list =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten_list(input_list):
    output_list = []
    for item in input_list:
        if isinstance(item, list):
            output_list.extend(flatten_list(item))
        else:
            output_list.append(item)
    return output_list
result = flatten_list(input_list)
print(result)



def reverse_nested_lists(lst):
    return [item[::-1] if isinstance(item, list) else item for item in lst][::-1]
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested_lists(input_list)
print(output_list)