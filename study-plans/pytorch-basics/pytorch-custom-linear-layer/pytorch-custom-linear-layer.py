import torch
import torch.nn as nn

class CustomLinear(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        pass
        t0 = torch.empty(out_features, in_features)
        self.weight = nn.Parameter(torch.nn.init.kaiming_uniform_(t0))
        t1 = torch.ones(out_features)
        self.bias = nn.Parameter(torch.tensor(t1))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        pass
        y = x @ self.weight.T + self.bias
        return y