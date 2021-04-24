import re
print(re.sub(r"([aieouAEIOU]+)", r"ib\1", input()))