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


assert tokenize("i hAVe a brother, and a sister. <EOS>") == ['i', 'have', 'a', 'brother', ',', 'and', 'a', 'sister', '.', '<EOS>']

def pad_sequences(ins, labs):
  combine = ins+labs
  length = [len(sentence) for sentence in combine]
  max_length = max(length)
  padded_ins = []
  padded_labs = []
  for sequence in ins:
    padding = [0] * (max_length - len(sequence))
    padded_sequence = sequence + padding
    padded_ins.append(padded_sequence)
  for sequence in labs:
    padding = [0] * (max_length - len(sequence))
    padded_sequence = sequence + padding
    padded_labs.append(padded_sequence)
  return padded_ins, padded_labs

one, two = pad_sequences([[3,2,4,2,3,2,3], [3,2,2]],
                         [[3,2],[3,2,1]])

assert len(one) == len(two)
assert two[1] == [3,2,1,0,0,0,0]
