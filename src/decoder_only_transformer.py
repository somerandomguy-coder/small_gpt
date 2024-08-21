class Attention(nn.Module):
  def __init__(self, d_model):
    super().__init__()
    self.w_Q = nn.Linear(in_features=d_model, out_features=d_model)
    self.w_K = nn.Linear(in_features=d_model, out_features=d_model)
    self.w_V = nn.Linear(in_features=d_model, out_features=d_model)

    self.row_dim = 64
    self.col_dim = d_model

  def forward(self, encodings_Q, encodings_K, encodings_V, mask=None):
    Q = self.w_Q(encodings_Q) #self.w_Q, w_K, w_V is a linear layer with the formula: out = in*W + b (the layer already include W and b to train itself)
    K = self.w_K(encodings_K)
    V = self.w_V(encodings_V)

    sims = torch.matmul(Q, K.transpose(self.row_dim, self.col_dim))

    scaled_sims = sim / torch.tensor(k.size(self.col_dim)).sqrt()

    if mask is not None:
      scaled_sims = scaled_sims.masked_fill(mask == 0, -1e9)

    attention_weights = F.softmax(scaled_sims, dim=self.col_dim) # which dimension should the weight after softmax add up to 1 in this case the sum of all column in one row equal 1

    attention_score = torch.matmul(attention_weights, V)

    return attention_score

    return torch.matmul(scaled_sims, V)
