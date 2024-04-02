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
import matplotlib.pyplot as pyplot
from matplotlib import font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.font_manager as font_manager
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextToPath
from matplotlib.path import Path
import plotly.graph_objects as go
import seaborn as sns
from customplotlib.customization.config import *
from customplotlib.customization import processing
from cycler import cycler
from datetime import datetime
import numpy as np
import pandas as pd
import os



def format_str(string):
   strings = string.split('_')
   strings = [s.lower().capitalize() for s in strings]
   return " ".join(strings)

  
class Customplotlib():
   def __init__(self, supp_colors=False,
                official_colors=False,
                color_blind_mode=False,
                override_fontpath=False,
                override_autosave=AUTOSAVE):
      
       for i in dir(pyplot):
           if i not in ['scatter', 'plot', 'matshow', 'pie']:
               setattr(self, i, getattr(pyplot, i))
              
      
       self.ROOT_DIR = ROOT_DIR
       font_dirs = [os.path.abspath(ROOT_DIR)]
       font_files = fm.findSystemFonts(fontpaths=font_dirs)
       if not override_fontpath:
           for font_file in font_files:
               fm.fontManager.addfont(font_file)
                      
           self.fontpath = ROOT_DIR + FONT
           self.font = fm.FontProperties(fname=ROOT_DIR + FONT)
       else:
           fm.fontManager.addfont(override_fontpath)
           self.font = fm.FontProperties(fname=override_fontpath)
       self.fontsize = FONT_SIZE    
       self.titlesize = TITLE_SIZE
          
       self.supp_colors = supp_colors
       self.official_colors = official_colors
      
       if self.official_colors:
           self.colors = list(OFFICIAL.values())
       elif self.supp_colors:
           self.colors = list(SUPPS.values())
       else:
           self.colors = list(MAINS.values())
          
       self.color_blind_mode = color_blind_mode
       self.gradients = GRADIENTS
       self.markersize = MARKERSIZE
       self.figsize = FIGSIZE
       self.autosave = override_autosave
       self.savepath = FIGSAVEPATH
       self.legend_loc = LEGEND_LOC       
      
       if not self.color_blind_mode:
           self.rcParams['axes.prop_cycle'] = cycler(color=self.colors)
       else: 
           self.rcParams['axes.prop_cycle'] = (cycler(linestyle=LINESTYLES[:len(self.colors)]) +
                                               cycler(color=self.colors) +
                                               cycler(marker=MARKERSTYLES[:len(self.colors)])
                                              )
      
       self.rcParams['font.family'] = self.font.get_family()
       self.rcParams['font.sans-serif'] = self.font.get_name()
       self.rcParams["font.size"] = self.fontsize
      
       self.rcParams['text.color'] = "#3F3F3F"
       self.rcParams['axes.labelcolor'] = "#3F3F3F"
       self.rcParams['xtick.color'] = "#3F3F3F"
       self.rcParams['ytick.color'] = "#3F3F3F"
      
       self.rcParams["axes.labelsize"] = self.fontsize
       self.rcParams["axes.titlesize"] = self.titlesize
       self.rcParams["axes.titleweight"] = 'bold'
   
      
       self.rcParams["figure.titlesize"] = self.titlesize
      
       self.rcParams["figure.figsize"] = self.figsize
       self.rcParams['lines.markersize'] = self.markersize
       self.rcParams['lines.linewidth'] = 2
  
   def plot(self, **kwargs):
      
       color = kwargs.pop('color', None)
       if color in list(MAINS.keys()):
           color = MAINS[color]
       elif color in list(SUPPS.keys()):
           color = SUPPS[color]
       elif color in list(OFFICIAL.keys()):
           color = OFFICIAL[color]
      
       title = kwargs.pop('title',False)
       xlabel = kwargs.pop('xlabel',False)
       ylabel = kwargs.pop('ylabel',False)
       label = kwargs.get('label', None)
       legend = kwargs.get('legend', True)
       legend_loc = kwargs.get('legend_loc', LEGEND_LOC)
      
       if label is not None:
           if (type(kwargs.get('label')) == str) & ('data' in kwargs.keys()):
               data_df = kwargs.pop('data').copy()

               input_x_name = kwargs.pop('x')
               input_y_name = kwargs.pop('y')

               data_df['x'] = data_df[input_x_name]
               data_df['y'] = data_df[input_y_name]

               xlabel = format_str(input_x_name) if not xlabel else xlabel
               ylabel = format_str(input_y_name) if not ylabel else ylabel
               title = ylabel + " by " + xlabel
              
               data_df.sort_values(by=kwargs.get('label'), inplace=True)
               groups = data_df.groupby(kwargs.pop('label'), sort=True)
           else:
              
               data_df = pd.DataFrame({'x': kwargs.pop('x'),
                                       'y': kwargs.pop('y'),
                                       'label': kwargs.pop('label')})
               data_df.sort_values(by='label', inplace=True)
               groups = data_df.groupby('label', sort=True)
          
           for name, group in groups:
               group.sort_values(by='x', inplace=True)
               pyplot.plot(group.x, group.y, **kwargs, label=name, color=color)

       else:
           x = kwargs.pop('x', None)
           y = kwargs.pop('y', None)
           pyplot.plot(x,y,**kwargs, color=color)
      
       if legend:
           handles, labels = self.gca().get_legend_handles_labels()
           if labels:
               self.legend(bbox_to_anchor=legend_loc)         
      
       if title:
           self.title(title)
      
       if xlabel:
           self.xlabel(xlabel)
      
       if ylabel:
           self.ylabel(ylabel)
      
       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)           
           pyplot.savefig(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"), bbox_inches='tight')
          
   def scatter(self, *args, **kwargs):
      
       color = kwargs.pop('color', None)
       if color in list(MAINS.keys()):
           color = MAINS[color]
       elif color in list(SUPPS.keys()):
           color = SUPPS[color]
       elif color in list(OFFICIAL.keys()):
           color = OFFICIAL[color]
      
       title = kwargs.pop('title',False)
       xlabel = kwargs.pop('xlabel',False)
       ylabel = kwargs.pop('ylabel',False)
       label = kwargs.get('label', None)
       legend = kwargs.get('legend', True)
       legend_loc = kwargs.get('legend_loc', LEGEND_LOC)  
      
       if kwargs.pop('marker',False) == 'logo':
           font_path = f"{ROOT_DIR}/AetnaCVSLogo.ttf"
           fp = FontProperties(fname=font_path)
           v, codes = TextToPath().get_text_path(fp, s='©')
           path = Path(v, codes, closed=False)
           kwargs['marker'] = path
      
       if label is not None:
           if (type(kwargs.get('label')) == str) & ('data' in kwargs.keys()):
               data_df = kwargs.pop('data').copy()
               input_x_name = kwargs.pop('x')
               input_y_name = kwargs.pop('y')

               data_df['x'] = data_df[input_x_name]
               data_df['y'] = data_df[input_y_name]

               xlabel = format_str(input_x_name) if not xlabel else xlabel
               ylabel = format_str(input_y_name) if not ylabel else ylabel
               title = ylabel + " by " + xlabel
              
               data_df.sort_values(by=kwargs.get('label'), inplace=True)
               groups = data_df.groupby(kwargs.pop('label'), sort=True)
           else:
               data_df = pd.DataFrame({'x': kwargs.pop('x'),
                                       'y': kwargs.pop('y'),
                                       'label': kwargs.pop('label')})
               data_df.sort_values(by='label', inplace=True)
               groups = data_df.groupby('label', sort=True)
          
           for name, group in groups:
              
               if self.color_blind_mode:
                   kwargs['marker'] = next(self.gca()._get_lines.prop_cycler)['marker']
              
               pyplot.scatter(*args, **kwargs, x=group.x, y=group.y, label=name, color=color)

       else:
           pyplot.scatter(*args, **kwargs, color=color)
      
       if legend:
           handles, labels = self.gca().get_legend_handles_labels()
           if labels:
               self.legend(bbox_to_anchor=legend_loc)         
      
       if title:
           self.title(title)
      
       if xlabel:
           self.xlabel(xlabel)
      
       if ylabel:
           self.ylabel(ylabel)
      
       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)
           pyplot.savefig(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"), bbox_inches='tight')
          
          
   def matshow(self, *args, **kwargs):
      
       title = kwargs.pop('title',False)
       xlabel = kwargs.pop('xlabel',False)
       ylabel = kwargs.pop('ylabel',False) 
       xtick_rot = kwargs.pop('xtick_rot',45)
      
       gradient = self.gradients[kwargs.pop('gradient', 'hot_cold')]
      
       if kwargs.pop('invert', False):
               gradient.reverse()
              
       cmap = processing.get_gradient(gradient)
      
       pyplot.matshow(*args, **kwargs, cmap=cmap)
      
       df = args[0]
      
       self.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, rotation=xtick_rot)
       self.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns)
      
       cb = self.colorbar()

       if title:
           self.title(title)
      
       if xlabel:
           self.xlabel(xlabel)
      
       if ylabel:
           self.ylabel(ylabel)
      
       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)
           pyplot.savefig(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"), bbox_inches='tight')  
          
   def three_d_plot(self, *args, **kwargs):
      
      
       assert (len(args) >= 3)
      
       title = kwargs.pop('title',False)
       xlabel = kwargs.pop('xlabel',False)
       ylabel = kwargs.pop('ylabel',False) 
      
      
       gradient = self.gradients[kwargs.pop('gradient', 'rainbow')]
       if kwargs.pop('invert', False):
               gradient.reverse()
       cmap = processing.get_gradient(gradient)
      
       x = args[0]
       y = args[1]
       z = args[2]
      
       fig = pyplot.figure()
       ax = Axes3D(fig)
       surf = ax.plot_trisurf(x, y, z,
                              cmap=cmap,
                              linewidth=0.1)
       fig.colorbar(surf, shrink=0.5, aspect=5)

       if title:
           self.title(title)
      
       if xlabel:
           self.xlabel(xlabel)
      
       if ylabel:
           self.ylabel(ylabel)
      
       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)
           pyplot.savefig(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"), bbox_inches='tight')
          
          
   def pie(self, df, label_col, val_col, **kwargs):
      
       title = kwargs.pop('title',False)      
       other_threshold = kwargs.pop('other_threshold',0.1)
       pixels = kwargs.pop('pixels', 400)
      
       df[val_col].fillna(0, inplace=True)
       df[f'{val_col}_norm'] = df[val_col] / df[val_col].sum()
       sub_df = df.sort_values(by=f'{val_col}_norm', ascending=False)[[label_col, f'{val_col}_norm']]
       to_keep = sub_df[sub_df[f'{val_col}_norm'] >= other_threshold][label_col].unique()

       sub_df['slice_names'] = np.where(sub_df[label_col].isin(to_keep),
                                        sub_df[label_col],
                                        'Other')

       to_plot = sub_df.groupby('slice_names')[f'{val_col}_norm'].sum().reset_index()

       to_plot['rank'] = np.where(to_plot['slice_names'] == 'Other',
                                  1,
                                  0)
      
       to_plot.sort_values(by=['rank', f'{val_col}_norm'], ascending=False, inplace=True)
       to_plot = to_plot[to_plot[f'{val_col}_norm'] > 0]

       values = to_plot[f'{val_col}_norm'] * 100
       labels = to_plot['slice_names']
       lookup = dict(zip(values, labels))

       fig = go.Figure()

       # Add a pie chart trace
       fig.add_trace(
           go.Pie(values=values,
                   labels=labels,
                   sort=False,
                   texttemplate="%{label}<br>" "%{percent:.0%}",
                   showlegend=False,
                   rotation=0,
                   direction="clockwise",
                   textposition='outside',
                   titlefont=dict(size =20, color="#3F3F3F", family='Helvetica'),
                   textfont=dict(size =14, color="#3F3F3F", family='Helvetica'),
                   marker = {"line": {"width": 3, "color": 'white'}}
                 )
       )

       if not title:
           title = label_col.capitalize()
      
       fig.update_layout(
           height=pixels,
           width=pixels,
           colorway = self.colors,
           title=dict(
               text=f"<b>{title}</b>",
               font={'color': "#3F3F3F", "size":20},
               x=0.5,
               y=0.9
           )
       )
      

       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)
           fig.write_image(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"))  
       fig.show()
      
      
   def dist(self, x, **kwargs):
      
       title = kwargs.pop('title',False)
       xlabel = kwargs.pop('xlabel',False)
       ylabel = kwargs.pop('ylabel',False) 
      
       fill = kwargs.pop('fill', True)
      
       ax = kwargs.pop('ax',False)
       if not ax:
           fig,ax = pyplot.subplots(1,1)
      
       vals = pd.Series(x)
       sns.kdeplot(data = vals, ax=ax, fill=fill, **kwargs)
       ax.spines['top'].set_visible(False)
       ax.spines['right'].set_visible(False)
       ax.spines['left'].set_visible(False)
       self.yticks([])
       ax.set_ylabel("")
       ax.tick_params(labelbottom=True)
      
       if title:
           self.title(title)
      
       if xlabel:
           self.xlabel(xlabel)
      
       if ylabel:
           self.ylabel(ylabel)
      
       if self.autosave:
           if not os.path.exists(FIGSAVEPATH):
               os.makedirs(FIGSAVEPATH)
           pyplot.savefig(FIGSAVEPATH + datetime.now().strftime("%m-%d-%Y-%H:%M:%S.png"), bbox_inches='tight')
          
       return ax
   