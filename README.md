# TensorTonic Solutions

Welcome to my TensorTonic solutions repository!

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, automatically synchronized from the platform.

<!-- tensortonic:start -->
# paulo's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/01pauloo.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| Implement Adam Optimizer Step | Implement one vectorized Adam optimizer step in NumPy with first and second moments, bias correction, and elementwise parameter updates. | https://www.tensortonic.com/problems/adam-optimizer |
| Compute AUC (Area Under ROC) | Calculate binary-classification ROC AUC from false-positive and true-positive rates using trapezoidal integration. | https://www.tensortonic.com/problems/auc |
| Bernoulli Probability Mass Function & Moments | Compute the Bernoulli probability mass function, expected value, and variance for a valid success probability. | https://www.tensortonic.com/problems/bernoulli-pmf |
| Cohen's Kappa | Calculate Cohen's kappa from two label sequences by comparing observed agreement with chance agreement. | https://www.tensortonic.com/problems/cohens-kappa |
| Color to Grayscale | Convert an RGB image to grayscale using weighted color channels while preserving its spatial dimensions. | https://www.tensortonic.com/problems/color-to-grayscale |
| Implement Cosine Similarity | Implement cosine similarity from scratch with NumPy. Covers dot products, Euclidean norms and zero-vector handling, with tests in the browser. | https://www.tensortonic.com/problems/cosine-similarity |
| Implement Dropout (Training Mode) | Implement training-mode dropout in NumPy with random masking and inverted scaling of retained activations. | https://www.tensortonic.com/problems/dropout-training |
| Compute Entropy for a Node | Compute decision-tree node entropy from class labels using empirical class probabilities and base-two logarithms. | https://www.tensortonic.com/problems/entropy-node |
| Expected Value (Discrete Distribution) | Compute the expected value of a discrete distribution from matched outcomes and normalized probabilities. | https://www.tensortonic.com/problems/expected-value-discrete |
| Implement Gradient Descent for a 1D Quadratic | Optimize a one-dimensional quadratic with iterative gradient descent and return the parameter trajectory. | https://www.tensortonic.com/problems/gradient-descent-quadratic |
| Apply 4×4 Homogeneous Transform | Apply a 4x4 homogeneous transformation matrix to 3D points using rotation, translation, and homogeneous coordinates. | https://www.tensortonic.com/problems/homogeneous-transform |
| Logistic Regression Training Loop | Train binary logistic regression in NumPy using sigmoid probabilities, gradient descent, and learned weight and bias parameters. | https://www.tensortonic.com/problems/logistic-regression-training |
| Matrix Transpose | Implement matrix transpose in NumPy without built-in transpose helpers, preserving rectangular shapes and the original input. | https://www.tensortonic.com/problems/matrix-transpose |
| Arange and Linspace | Generate a one-dimensional NumPy sequence using either step-based arange or count-based linspace semantics. | https://www.tensortonic.com/problems/numpy-arange-linspace |
| Create Arrays from Lists | Convert a rectangular Python list of lists into a two-dimensional NumPy float64 array. | https://www.tensortonic.com/problems/numpy-create-array |
| Random Array Generation | Generate seeded float64 NumPy arrays from either a uniform or standard normal distribution. | https://www.tensortonic.com/problems/numpy-random-arrays |
| Reshaping Arrays | Transform a rectangular input into a NumPy float64 array using flattening, transposition, or a leading batch dimension. | https://www.tensortonic.com/problems/numpy-reshape |
| Zeros and Ones | Create a two-dimensional float64 NumPy array of a requested shape filled entirely with zeros or ones. | https://www.tensortonic.com/problems/numpy-zeros-ones |
| Pad Sequences | Pad or truncate variable-length token ID sequences in NumPy with configurable maximum length and padding values. | https://www.tensortonic.com/problems/pad-sequences |
| Percentiles / Quantiles | Calculate requested percentiles from numeric data using the interpolation rule specified by the problem. | https://www.tensortonic.com/problems/percentiles |
| Popularity Ranking | Rank items by interaction popularity with deterministic ordering for equal-frequency items. | https://www.tensortonic.com/problems/popularity-ranking |
| Precision and Recall at K | Compute precision@K and recall@K for recommendation systems by comparing ranked predictions with relevant items, with tests in the browser. | https://www.tensortonic.com/problems/precision-recall-at-k |
| Activation Functions | Implement four common activation functions from scratch using basic PyTorch tensor operations (no torch.nn module). | https://www.tensortonic.com/problems/pytorch-activation-function-from-scratch |
| Basic Autograd | Use PyTorch autograd to evaluate a scalar function and return its derivative at every supplied input value. | https://www.tensortonic.com/problems/pytorch-basic-autograd |
| Batch Normalization | Normalize each feature across the batch, then scale and shift using learnable parameters. | https://www.tensortonic.com/problems/pytorch-batch-normalization |
| Simple Neural Network | Implement a class SimpleNet subclassing nn.Module with two linear layers and ReLU between them. | https://www.tensortonic.com/problems/pytorch-build-simple-nn-from-scratch |
| Custom Linear Layer | Implement a custom linear layer that computes the affine transformation without using any built-in linear layer. | https://www.tensortonic.com/problems/pytorch-custom-linear-layer |
| Dropout from Scratch | Implement PyTorch inverted dropout from a supplied mask during training while returning inputs unchanged in evaluation mode. | https://www.tensortonic.com/problems/pytorch-dropout-from-scratch |
| Loss Functions | Implement three common loss functions from scratch using PyTorch tensor operations: mean squared error, cross-entropy, and Huber loss. | https://www.tensortonic.com/problems/pytorch-loss-functions |
| Tensor Operations | Perform common element-wise and matrix tensor operations: add, multiply, matmul, power, and max. | https://www.tensortonic.com/problems/pytorch-tensor-arithmetic |
| Tensor Factory | Create PyTorch tensors with zeros, ones, or a constant fill value using the requested shape and dtype. | https://www.tensortonic.com/problems/pytorch-tensor-creation |
| Tensor Shape Manipulation | Reshape tensors using three common PyTorch operations: flatten to collapse into 1D, squeeze to remove size-1 dimensions. | https://www.tensortonic.com/problems/pytorch-tensor-reshape |
| RMSProp Optimizer (Single Update Step) | Implement one RMSProp update in NumPy using an exponential squared-gradient average and adaptive scaling. | https://www.tensortonic.com/problems/rmsprop-optimizer |
| RNN Step Forward (Tanh Cell) | Implement one vanilla RNN timestep with affine input and recurrent transforms followed by tanh activation. | https://www.tensortonic.com/problems/rnn-step-forward |
| Implement Sigmoid in NumPy | Implement a vectorized sigmoid activation in NumPy for scalars, lists, vectors, and matrices, including large positive and negative inputs. | https://www.tensortonic.com/problems/sigmoid-numpy |
| Implement Swish Activation | Apply the Swish activation element-wise in NumPy by multiplying each input by its sigmoid, computed without overflow. | https://www.tensortonic.com/problems/swish-activation |
| Implement Tanh Activation | Implement the hyperbolic tangent activation element-wise with outputs bounded between minus one and one. | https://www.tensortonic.com/problems/tanh-activation |
| Text Chunking | Split text into ordered chunks under the requested size and overlap rules without dropping content. | https://www.tensortonic.com/problems/text-chunking |
| Value Iteration Step | Perform one Bellman optimality update across states and actions for a tabular Markov decision process. | https://www.tensortonic.com/problems/value-iteration-step |
| Embedding Layer | Create PyTorch token embeddings and scale each lookup by the square root of the Transformer model dimension. | https://www.tensortonic.com/research/transformer/transformers-embedding |
| Tokenization | Build a word-level Transformer tokenizer with fixed special-token IDs, sorted vocabulary entries, encoding, and decoding. | https://www.tensortonic.com/research/transformer/transformers-tokenization |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/01pauloo)
<!-- tensortonic:end -->
