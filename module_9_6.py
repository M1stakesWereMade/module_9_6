def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            yield text[start:start+length]

text = "abc"
variants = list(all_variants(text))
for variant in variants:
    print(variant)