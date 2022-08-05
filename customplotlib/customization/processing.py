# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
from matplotlib import colors as matplotcolors
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import cm

from customplotlib.customization.config import MAINS, SUPPS
from customplotlib.customization.config import GRADIENT_LIGHT_DARK, GRADIENT_HOT_COLD, GRADIENT_RAINBOW, GRADIENT_BW


# +
def clamp(x): 
    return max(0, min(x, 255))

vclamp = np.vectorize(clamp)

def hex_to_rgb(h):
    h = h.replace('#', "")
    assert(len(h) == 6)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    rgb = vclamp(rgb)
    return '#%02x%02x%02x'.upper() % (rgb[0], rgb[1], rgb[2])

def get_hex_color(c):
    if len(c) == 7 and c[0] == '#':
        return c
    elif (type(c) == tuple or type(c) == list) and len(c) == 3:
        return rgb_to_hex(c)
    elif c in MAINS.keys():
        return get_hex_color(MAINS[c])
    elif c in SUPPS.keys():
        return get_hex_color(SUPPS[c])
    else:
        raise ValueError(f"{c} is invalid. Either not a hexcolor, RGB tuple, or aliased color name")
        

def get_rgb_color(c):
    if (type(c) == tuple or type(c) == list) and len(c) == 3:
        return vclamp(c)
    elif len(c) == 7 and c[0] == '#':
        return hex_to_rgb(c)
    elif c in MAINS.keys():
        return get_rgb_color(MAINS[c])
    elif c in SUPPS.keys():
        return get_rgb_color(SUPPS[c])
    else:
        raise ValueError(f"{c} is invalid. Either not a hexcolor, RGB tuple, or aliased color name")


# -

def inter_from_256(x):
    return np.interp(x=x,xp=[0,255],fp=[0,1])


def get_gradient(colors):
    wts = np.linspace(0,1, len(colors))
    colors = [get_rgb_color(c) for c in colors]
    
    cdict = {
    'red':[(wts[ix],
            inter_from_256(colors[ix][0]),
            inter_from_256(colors[ix][0])) for ix in range(len(colors))],
    'green':[(wts[ix],
              inter_from_256(colors[ix][1]),
              inter_from_256(colors[ix][1])) for ix in range(len(colors))],
    'blue': [(wts[ix],
              inter_from_256(colors[ix][2]),
              inter_from_256(colors[ix][2])) for ix in range(len(colors))],
    }
    return matplotcolors.LinearSegmentedColormap('gradient',segmentdata=cdict)
