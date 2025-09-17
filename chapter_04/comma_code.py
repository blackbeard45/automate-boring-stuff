def comma_code(list):
    """Return a string of items separated by commas, with 'and' before the last item."""
    if not list:
        return ''
    elif len(list) == 1:
        return list[0]
    else:
        return ', '.join(list[:-1]) + ', and ' + list[-1]

# Example usage:
items = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(items))  # Output: apples, bananas, tofu, and cats

# Example usage:
items = ['apples', 'bananas']
print(comma_code(items))  # Output: apples and bananas

items = ['apples']
print(comma_code(items))  # Output: apples
items = []
print(comma_code(items))  # Output: (an empty string)

# Example usage:
items = ['apples', 'bananas', 'tofu']
print(comma_code(items))  # Output: apples, bananas, and tofu

# Example usage:
items = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
print(comma_code(items))  # Output: apples, bananas, tofu, cats, and dogs
