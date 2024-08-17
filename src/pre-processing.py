def tokenize(sentence):
    sentence = sentence.split()
    tokens = []
    for word in sentence:
      if word == "<EOS>":
        tokens.append(word)
      else:
        word = word.lower()
        if word[-1] in [",", ".", "!", "?", ":", ";", ")", "]", "}", "'", '"']:
          tokens.append(word[:-1])
          tokens.append(word[-1])
        elif word[0] in ["(", "[", "{", "'", '"']:
          tokens.append(word[0])
          tokens.append(word[1:])
        else:
          tokens.append(word)
    return tokens


# test: print(tokenize("i hAVe a brother, and a sister. <EOS>"))