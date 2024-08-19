class positional_encoding(nn.Module):
  def _init_(self, d_model, max_length):
    super()._init_()

    pe = torch.zeros(max_length, d_model)

    position = torch.arange(0, max_length, step=1).float().unsqueeze(1)
    embedded_index = torch.arange(0, d_model, step=2).float() #i    #step = 2 because i = 0 can be use for sin and cos

    div_term = 1/10000 ** (embedded_index / d_model)
    # fill in the zeros table
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)

    self.register_buffer("pe", pe)

  def feed_forward(self, word_embedding): #take output from word_embedding then calculate
    return word_embedding + self.pe[:word_embedding.size(0)] # just self.pe since all inputs are already uniform due to padding 
