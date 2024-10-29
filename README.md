# Scalable Enumeration of Trap Spaces in Boolean Networks via Answer Set Programming

This repository provides `tsconj`. A Python package for scalable enumeration of minimal and maximal trap spaces of Boolean networks.

## Installation

The package can be installed using `pip`. First, download the contents of this repository and navigate to the repository root. Then execute `pip install .`.

## Usage

In the folder `examples`, we provide two simple scripts showcasing the use of `tsconj`:

```bash
python3 examples/max_traps.py 0 examples/model.bnet
# Should output:
# 0----------------------------
# 1----------------------------
# ------------------0----------

python3 examples/min_traps.py 0 examples/model.bnet
# Should output:
# 0000000-000000000000000000000
# 1000000-000000000000000000000
```