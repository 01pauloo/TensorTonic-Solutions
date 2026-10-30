import torch
import torch.nn as nn

def train_epoch(model: nn.Module, dataloader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer) -> float:
    """
    Returns the mean batch loss as a Python float.
    """
    pass
    model.train()
    c = 0
    l = 0.0
    for (input, target) in dataloader:
        optimizer.zero_grad()
        pred = model(input)
        loss = criterion(pred, target)
        loss.backward()
        optimizer.step()
        l += loss.item()
        c += 1
    return float(l/c)
        
        