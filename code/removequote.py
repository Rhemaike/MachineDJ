def removequote(word):
    quote = "\'"
    dubquote = "\""

    if word.find(dubquote) >= 0:
        wordSplit = word.split(dubquote)
        return wordSplit[1]
    else:
        return word


if __name__ == "__main__":
    exString = "\'Why you gotta be so rude\'"
    newString = removequote(exString)
    print("Old string: {}, new string: {}".format(exString,newString))
    