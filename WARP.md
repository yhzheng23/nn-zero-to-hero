# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is Andrej Karpathy's "Neural Networks: Zero to Hero" educational repository - a course on neural networks starting from the fundamentals. The repo contains Jupyter notebooks that accompany YouTube video lectures building neural networks from scratch in Python.

## Project Structure

### Core Architecture
- **Educational Course Format**: Sequential lectures building complexity progressively
- **Two Main Learning Tracks**:
  1. **micrograd** - Building backpropagation and neural network fundamentals
  2. **makemore** - Character-level language modeling progressing to modern architectures

### Directory Structure
```
lectures/
├── micrograd/           # Lecture 1: Backpropagation fundamentals
│   ├── micrograd_lecture_first_half_roughly.ipynb
│   ├── micrograd_lecture_second_half_roughly.ipynb
│   └── micrograd_exercises.ipynb
└── makemore/           # Lectures 2-6: Language modeling progression
    ├── makemore_part1_bigrams.ipynb        # Bigram models
    ├── makemore_part2_mlp.ipynb           # Multi-layer perceptrons
    ├── makemore_part3_bn.ipynb            # Batch normalization
    ├── makemore_part4_backprop.ipynb      # Manual backpropagation
    ├── makemore_part5_cnn1.ipynb          # Convolutional networks (WaveNet-style)
    └── names.txt                          # Dataset for character-level modeling
```

## Common Development Commands

### Running Jupyter Notebooks
```bash
# Start Jupyter Lab (recommended for multiple notebooks)
jupyter lab

# Start Jupyter Notebook server
jupyter notebook

# Convert notebook to Python script
jupyter nbconvert --to python lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb
```

### Python Environment Setup
```bash
# Install common dependencies (the notebooks use standard libraries)
pip install numpy matplotlib torch

# For comprehensive ML environment
pip install numpy matplotlib torch torchvision jupyter
```

## Key Learning Architecture Concepts

### micrograd (Lecture 1)
- **Automatic Differentiation**: Building a scalar-valued autograd engine
- **Neural Network Fundamentals**: Forward pass, backward pass, gradient computation
- **Core Classes**: `Value` class implementing automatic differentiation for scalars
- **Dependencies**: Pure Python with minimal external libraries (numpy, matplotlib)

### makemore (Lectures 2-6)  
- **Language Modeling Progression**: From simple bigrams to modern architectures
- **Character-Level Processing**: Working with character sequences rather than word tokens
- **Architecture Evolution**:
  - Part 1: Bigram statistical models
  - Part 2: Multi-layer perceptrons (MLPs)
  - Part 3: Batch normalization and training dynamics
  - Part 4: Manual backpropagation implementation
  - Part 5: Convolutional architectures (WaveNet-inspired)

### Key Technical Concepts Covered
- **Backpropagation**: Manual implementation to understand gradient flow
- **Training Dynamics**: Learning rates, overfitting, train/dev/test splits
- **Modern Techniques**: Batch normalization, residual connections
- **Efficient Tensor Operations**: PyTorch fundamentals and efficient computation

## Development Workflow

### Working with Individual Lectures
```bash
# Navigate to specific lecture
cd lectures/micrograd
# or
cd lectures/makemore

# Open specific notebook
jupyter notebook micrograd_lecture_first_half_roughly.ipynb
```

### Testing Code from Notebooks
```bash
# Extract and run Python code from notebook cells
jupyter nbconvert --to python --execute notebook_name.ipynb

# Run specific notebook and output results
jupyter nbconvert --to notebook --execute --inplace notebook_name.ipynb
```

## Data Files
- `lectures/makemore/names.txt`: Character-level dataset containing ~32K names for language modeling experiments

## External Resources Referenced
- **micrograd GitHub repo**: https://github.com/karpathy/micrograd
- **makemore GitHub repo**: https://github.com/karpathy/makemore  
- **minBPE repo**: https://github.com/karpathy/minbpe (for tokenizer lecture)
- **YouTube lectures**: Each notebook corresponds to a specific YouTube video lecture

## Technical Notes

### Dependencies
- **Core**: Python 3, Jupyter, numpy, matplotlib
- **Deep Learning**: PyTorch (torch, torchvision)
- **Visualization**: matplotlib for plotting training dynamics and results
- **No complex build system**: Educational repo focused on learning, not production

### Educational Philosophy
- **From Scratch Implementation**: Understanding fundamentals by building everything manually
- **Gradual Complexity**: Each lecture builds on previous concepts
- **Practical Implementation**: Real code that runs and trains actual neural networks
- **Mathematical Understanding**: Focus on understanding backpropagation and gradient computation

This repository is designed for learning and experimentation rather than production use. Each notebook is self-contained and can be run independently, though the sequence builds conceptual understanding progressively.
