# Use map with lambda to get lengths of words

words = ["python", "ai", "lambda", "function"]
lengths = list(map(lambda w: len(w), words))
print(lengths)  # [6, 2, 6, 8]
