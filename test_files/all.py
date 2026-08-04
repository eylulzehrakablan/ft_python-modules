lst = ["zehra", 42, "deniz", "eylul"]

def f(name_list):
    return all(isinstance(item, str) for item in name_list)

print(f(lst))