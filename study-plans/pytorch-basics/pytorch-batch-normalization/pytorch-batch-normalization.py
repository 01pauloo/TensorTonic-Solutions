import torch
def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    pass
    mu_j = X.mean(dim=0)
    sigma_j_2 = ((X-mu_j)**2).mean(dim=0)
    y = gamma * ((X-mu_j)/torch.sqrt(sigma_j_2 + eps)) + beta
    return y 