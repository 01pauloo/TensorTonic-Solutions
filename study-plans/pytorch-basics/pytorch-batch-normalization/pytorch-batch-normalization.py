import torch
def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    pass
    mu = X.mean(dim=0)
    sigma_2 = ((X-mu)**2).mean(dim=0)
    y = gamma * ((X-mu)/torch.sqrt(sigma_2 + eps)) + beta
    return y 