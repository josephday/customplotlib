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
from collections import OrderedDict
import os

### basics
FIGSIZE = (10,6)
FIGSAVEPATH = '../saved_figs/'
AUTOSAVE = True


### font
# download .ttf for your desired font and place at customplotlib/customization/fonts/
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/fonts/'       
FONT = 'proxima_nova.ttf'
FONTSIZE = 16
LEGEND_LOC = (1.05,0.65)



### main colors
MAINS = OrderedDict()

MAINS['strong-blue'] = "#4C6FE7"
MAINS['strong-dark-gray'] = "#4F4F4F"
MAINS['strong-light-blue'] = "#B5C3FF"
MAINS['strong-off-black'] = "#2a2a2a"
MAINS['strong-dark-blue'] = "#3958C4"
MAINS['strong-off-white'] = '#F4F4F4'


# +
### supplementary colors
SUPPS = OrderedDict()

SUPPS['strong-blue'] = "#4C6FE7"
SUPPS['strong-red'] = "#DE364F"
SUPPS['strong-orange'] = "#FFC65F"
SUPPS['strong-green'] = "#1FC198"
SUPPS['strong-purple'] = '#D065D3'
SUPPS['strong-yellow'] = '#F9F871'
SUPPS['strong-dark-orange'] = '#D24B00'
SUPPS['strong-dark-green'] = '#008A65'
SUPPS['strong-light-purple']= '#A5A7DD'
SUPPS['strong-dark-red'] = '#9F0023'

# +
### pre-defined gradients
GRADIENT_LIGHT_DARK = ['strong-off-white', 'strong-light-blue', 'strong-blue', 'strong-dark-blue'] 
GRADIENT_HOT_COLD = ['dark-red', 'red', 'strong-off-white','strong-light-blue', 'strong-blue', 'strong-dark-blue']
GRADIENT_RAINBOW = ['dark-red', 'red', 'orange', 'yellow', 'green', 'strong-blue', 'strong-dark-blue']
GRADIENT_BW = ['strong-off-white', '#D0D0D0', '#808080', 'strong-dark-gray', 'strong-off-black']

GRADIENTS = {'strong': GRADIENT_LIGHT_DARK, 
            'hot_cold': GRADIENT_HOT_COLD,
            'rainbow': GRADIENT_RAINBOW,
            'bw': GRADIENT_BW}

# +
### line styles

linestyle_tuple = [
     ('solid',                 (0, ())),
     ('dotted',                (0, (1, 1))),
     ('dashed',                (0, (5, 5))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dotted',        (0, (1, 1))),
     ('densely dashed',        (0, (5, 1))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

LINESTYLES = [i[1] for i in linestyle_tuple]

# +
### marker styles

MARKERSTYLES = ['o', 'v', '*', '^', '<', '>', '8', 's', 'p', 'h', 'H', 'D', 'd', 'P', 'X']
MARKERSIZE = 12
