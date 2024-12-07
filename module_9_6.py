
def all_variants(text):
    for i in range(0, len(text)):
        for y in range(len(text)):
           if i+y+1 <= len(text):
                yield text[y:i+y+1]

a = all_variants("abc")
for i in a:
    print(i)