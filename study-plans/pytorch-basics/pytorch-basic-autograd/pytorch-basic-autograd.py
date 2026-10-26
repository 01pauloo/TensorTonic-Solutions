import torch

def compute_gradient(values: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 gradient tensor with the same shape as values.
    """
    pass
    values1 = values.requires_grad_()
    y = (values1**3+2*values1).sum()
    values_backw = y.backward()
    return values1.grad
        