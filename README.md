# Dynamic graph plotter
`dynamic-graph-plotter` is utility that creates .gif files with dynamically 
displaying graphs from given .csv data files.

![example](https://github.com/AmaHacka/dynamic-graph-plotter/blob/master/examples/movie.gif)

## Installation
To install `dynamic-graph-plotter`
1. Pull repo
2. pip install -r requirements.txt

## Usage
```
usage: plotter.py [-h] [-s STEP] [--l1 L1] [--l2 L2] [--xlabel XLABEL] [--ylabel YLABEL] f [f ...]

positional arguments:
  f                     CSV files with data

optional arguments:
  -h, --help            show this help message and exit
  -s STEP, --step STEP  Sampling frequency
  --l1 L1               First plot name
  --l2 L2               Second plot name
  --xlabel XLABEL       X axis name
  --ylabel YLABEL       Y axis name
```