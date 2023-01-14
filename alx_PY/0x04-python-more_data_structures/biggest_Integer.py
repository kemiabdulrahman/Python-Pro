def double_values(original_dict):
    double_dict = {}
    for key, value in original_dict.items():
        double_dict[key] = value * 2
    return double_dict

original_dict = {"a":1, "b":2, "c": 5}
double_dict = double_values(original_dict)
print(double_dict)
