import os
from collections import OrderedDict


### basics
FIGSIZE = (10,6)
FIGSAVEPATH = '../saved_figs/'
AUTOSAVE = True


### font
# download .ttf for your desired font and place at customplotlib/customization/fonts/
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/fonts/'
TITLE_FONT = 'NunitoSans-VariableFont_YTLC,opsz,wdth,wght.ttf'
FONT = TITLE_FONT
TITLE_SIZE = 15
FONT_SIZE = 12
LEGEND_LOC = (1.05,0.65)



### main colors
MAINS = OrderedDict()

MAINS['green'] = "#20b498"
MAINS['light-green'] = "#89FBDB"
MAINS['dark-green'] = "#285C6F"
MAINS['dark-gray'] = "#575757"
MAINS['light-gray'] = "#CCCCCC"
MAINS['black'] = "#000000"

# +
### supplementary colors
SUPPS = OrderedDict()

SUPPS['green'] = "#20b498"
SUPPS['orange'] = "#faa613"
SUPPS['violet'] = "#52489C"
SUPPS['blue'] = "#48acf0"
SUPPS['pink'] = "#f06c9b"
SUPPS['yellow'] = "#eeff41"
SUPPS['navy'] = "#0B315E"
SUPPS['burgundy'] = "#550527"
SUPPS['gray'] = "#767676"
SUPPS['red'] = "#C2203E"

SUPPS['light-violet'] = "#B18CC1"

SUPPS['light-navy'] = "#0A4B8C"
SUPPS['light-teal'] = "#78EAD7"
SUPPS['light-yellow'] = "#FFE97D"
SUPPS['light-orange'] = "#F99F5D"
SUPPS['light-pink'] = "#FFBDD1"
SUPPS['light-blue'] = "#B8E3EB"
SUPPS['light-green'] = "#89FBDB"
SUPPS['light-gray'] = "#CCCCCC"

SUPPS['dark-violet'] = "#641987"
SUPPS['dark-navy'] = "#021F42"
SUPPS['dark-teal'] = "#00A78E"
SUPPS['dark-yellow'] = "#F4B822"
SUPPS['dark-orange'] = "#F4642A"
SUPPS['dark-pink'] = "#E46B95"
SUPPS['dark-blue'] = "#09A7E3"
SUPPS['dark-green'] = "#285C6F"
SUPPS['dark-gray'] = "#575757"

SUPPS['black'] = '#000000'
SUPPS['white'] = '#FFFFFF'
SUPPS['off-white'] = '#F7F7F7'


OFFICIAL = OrderedDict()


# +
### pre-defined gradients
GRADIENT_LIGHT_DARK = ['off-white', '#C6FCED', 'light-green', 'green', 'dark-green']
GRADIENT_HOT_COLD = ['red', 'pink', 'light-pink', 'off-white', 'light-blue', 'blue', 'navy']
GRADIENT_RAINBOW = ['burgundy', 'red', 'orange', 'yellow', 'green', 'blue', 'light-navy', 'violet', 'dark-violet']
GRADIENT_BW = ['off-white', 'light-gray', 'gray', 'dark-gray', 'black']

GRADIENTS = {'joe_green': GRADIENT_LIGHT_DARK,
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
