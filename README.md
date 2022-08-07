# customplotlib


A package for easily configuring better defaults for Matplotlib plots.


# Install

Clone the repo with the following:

```python
git clone https://github.com/josephday/customplotlib.git
```

Navigate to the packages root directory and install like so

```python
python -m pip install -e 
```

By default, the package refers to a .ttf file for the font Proxima Nova. This file comes with the cloned repo, but you could download and use any .ttf file and place it in the `customplotlib/customizations/fonts/` directory.


## Use

At the top of your notebook, import as below. Then proceed to refer to `plt` as you would `matplotlib.pyplot`

```python
from customplotlib.base import Customplotlib
plt = Customplotlib()
```
