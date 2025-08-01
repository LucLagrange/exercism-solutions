def abbreviate(sentence):

    corrected = sentence.replace("-", " ").replace("_", " ")

    print(corrected)

    words = corrected.split()

    result = []

    for word in words:
       result.append(word[0].upper())

    print("".join(result))
    return  "".join(result)