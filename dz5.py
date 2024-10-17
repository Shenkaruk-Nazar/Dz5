result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("....")
    if a < b:
        raise ValueError("....")
    if b > 100:
        raise IndexError("....")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Error {key}: {e}")

print(result)
