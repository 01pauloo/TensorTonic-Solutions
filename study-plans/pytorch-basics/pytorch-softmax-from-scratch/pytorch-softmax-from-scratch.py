import torch

def softmax(logits: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 probability tensor with the same shape as logits.
    """
    pass
    m = logits.max(dim=1, keepdim=True).values
    e = torch.exp(logits - m)
    p = e/e.sum(dim=1, keepdim=True)
    return p