"""MISC"""

text = """Hello world this is a text!"""

print(text[0]) #H

print(len(text))

"""String Methods"""

"""
I am too lazy to write each and every string methods
"""

# https://www.w3schools.com/python/python_strings_methods.asp
# String Methods are here ^



# Python string methods with examples by GPT ↓

# Variable, text, equals, string
text = "Hello, World!"

# 1. capitalize(): "Hello, world!"
capitalized_text = text.capitalize()  # "Hello, world!"

# 2. casefold(): "hello, world!"
casefolded_text = text.casefold()  # "hello, world!"

# 3. center(width[, fillchar]): "  Hello, World!  "
centered_text = text.center(17)  # "  Hello, World!  "

# 4. count(sub[, start[, end]]): 1
counted_occurrences = text.count("o")  # 1

# 5. encode(encoding="utf-8", errors="strict"): b'Hello, World!'
encoded_text = text.encode()  # b'Hello, World!'

# 6. endswith(suffix[, start[, end]]): True
ends_with = text.endswith("!")  # True

# 7. expandtabs(tabsize=8): "Hello,    World!"
expanded_tabs = "Hello,\tWorld!".expandtabs()  # "Hello,    World!"

# 8. find(sub[, start[, end]]): 7
found_index = text.find("World")  # 7

# 9. format(*args, **kwargs): "Hello, World!"
formatted_text = "Hello, {}!".format("World")  # "Hello, World!"

# 10. format_map(mapping): "Hello, World!"
formatted_text_map = "Hello, {place}!".format_map({"place": "World"})  # "Hello, World!"

# 11. index(sub[, start[, end]]): 7
index_of_substring = text.index("World")  # 7

# 12. isalnum(): False
is_alphanumeric = text.isalnum()  # False

# 13. isalpha(): False
is_alpha = text.isalpha()  # False

# 14. isascii(): True
is_ascii = text.isascii()  # True

# 15. isdecimal(): False
is_decimal = text.isdecimal()  # False

# 16. isdigit(): False
is_digit = text.isdigit()  # False

# 17. isidentifier(): False
is_identifier = text.isidentifier()  # False

# 18. islower(): False
is_lower = text.islower()  # False

# 19. isnumeric(): False
is_numeric = text.isnumeric()  # False

# 20. isprintable(): True
is_printable = text.isprintable()  # True

# 21. isspace(): False
is_space = text.isspace()  # False

# 22. istitle(): True
is_title = text.istitle()  # True

# 23. isupper(): False
is_upper = text.isupper()  # False

# 24. join(iterable): "H-e-l-l-o-,- -W-o-r-l-d-!"
joined_text = "-".join(["Hello", "World"])  # "H-e-l-l-o-,- -W-o-r-l-d-!"

# 25. ljust(width[, fillchar]): "Hello, World!      "
left_justified_text = text.ljust(20)  # "Hello, World!      "

# 26. lower(): "hello, world!"
lowercased_text = text.lower()  # "hello, world!"

# 27. lstrip([chars]): "Hello, World!  "
left_stripped_text = "   Hello, World!  ".lstrip()  # "Hello, World!  "

# 28. partition(sep): ('Hello', ', ', 'World!')
partitioned_text = text.partition(",")  # ('Hello', ', ', 'World!')

# 29. replace(old, new[, count]): "Hi, World!"
replaced_text = text.replace("Hello", "Hi")  # "Hi, World!"

# 30. rfind(sub[, start[, end]]): 7
reverse_find = text.rfind("World")  # 7

# 31. rindex(sub[, start[, end]]): 7
reverse_index = text.rindex("World")  # 7

# 32. rjust(width[, fillchar]): "      Hello, World!"
right_justified_text = text.rjust(20)  # "      Hello, World!"

# 33. rpartition(sep): ('Hello', ', ', 'World!')
right_partitioned_text = text.rpartition(",")  # ('Hello', ', ', 'World!')

# 34. rsplit(sep=None, maxsplit=-1): ['Hello,', 'World!']
right_split_text = text.rsplit(",")  # ['Hello,', 'World!']

# 35. rstrip([chars]): "   Hello, World!"
right_stripped_text = "   Hello, World!   ".rstrip()  # "   Hello, World!"

# 36. split(sep=None, maxsplit=-1): ['Hello,', 'World!']
split_text = text.split(",")  # ['Hello', ' World!']

# 37. splitlines([keepends]): ['Hello, World!']
split_lines = text.splitlines()  # ['Hello, World!']

# 38. startswith(prefix[, start[, end]]): True
starts_with = text.startswith("Hello")  # True

# 39. strip([chars]): "Hello, World!"
stripped_text = "   Hello, World!   ".strip()  # "Hello, World!"

# 40. swapcase(): "hELLO, wORLD!"
swapped_case_text = text.swapcase()  # "hELLO, wORLD!"

# 41. title(): "Hello, World!"
title_case_text = text.title()  # "Hello, World!"

# 42. translate(table): Dependent on implementation
# No direct result, as it requires a translation table.

# 43. upper(): "HELLO, WORLD!"
uppercased_text = text.upper()  # "HELLO, WORLD!"

# 44. zfill(width): "Hello, World!"
zero_filled_text = text.zfill(13)  # "Hello, World!"

# 45. __add__(string): "Hello, World! Welcome to Python!"
concatenated_text = text + " Welcome to Python!"  # "Hello, World! Welcome to Python!"

# 46. __contains__(string): True
contains_substring = "World" in text  # True

# 47. __getitem__(index): "W"
char_at_index = text[7]  # "W"

# Print results
print("Original text:", text)
print("Capitalized text:", capitalized_text)
print("Casefolded text:", casefolded_text)
print("Centered text:", centered_text)
print("Counted occurrences:", counted_occurrences)
print("Encoded text:", encoded_text)
print("Ends with:", ends_with)
print("Expanded tabs:", expanded_tabs)
print("Found index:", found_index)
print("Formatted text:", formatted_text)
print("Formatted text using mapping:", formatted_text_map)
print("Index of substring