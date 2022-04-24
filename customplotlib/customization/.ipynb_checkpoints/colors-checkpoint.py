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
from sctriangulate.colors import build_custom_divergent_cmap

MAINS = OrderedDict()

MAINS['strong-blue'] = "#4C6FE7"
MAINS['strong-dark-gray'] = "#4F4F4F"
MAINS['strong-light-blue'] = "#B5C3FF"
MAINS['strong-off-black'] = "#2a2a2a"
MAINS['strong-dark-blue'] = "#3958C4"
MAINS['strong-off-white'] = '#F4F4F4'



# +
SUPPS = OrderedDict()

SUPPS['red'] = "#DE364F"
SUPPS['orange'] = "#FFC65F"
SUPPS['green'] = "#1FC198"
SUPPS['purple'] = '#D065D3'
SUPPS['yellow'] = '#F9F871'
SUPPS['dark-orange'] = '#D24B00'
SUPPS['dark-green'] = '#008A65'
SUPPS['light-purple']= '#A5A7DD'
SUPPS['dark-red'] = '#9F0023'
# -

GRADIENT_LIGHT_DARK = ['strong-off-white', 'strong-light-blue', 'strong-blue', 'strong-dark-blue'] 
GRADIENT_HOT_COLD = ['dark-red', 'red', 'purple', 'strong-blue', 'strong-dark-blue']
GRADIENT_RAINBOW = ['dark-red', 'red', 'orange', 'yellow', 'green', 'strong-blue', 'strong-dark-blue']
GRADIENT_BW = ['strong-off-white', '#D0D0D0', '#808080', 'strong-dark-gray', 'strong-off-black']
