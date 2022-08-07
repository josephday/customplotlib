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
import matplotlib.font_manager as font_manager
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
    def __init__(self, supp_colors=False, color_blind_mode=False):
        
        for i in dir(pyplot):
            if i not in ['scatter', 'plot', 'matshow']:
                setattr(self, i, getattr(pyplot, i))
                
        
        self.ROOT_DIR = ROOT_DIR
        font_dirs = [os.path.abspath(ROOT_DIR)]
        font_files = fm.findSystemFonts(fontpaths=font_dirs)

        for font_file in font_files:
            fm.fontManager.addfont(font_file)
                    
        self.font = fm.FontProperties(fname=ROOT_DIR + FONT)
        self.fontsize = FONTSIZE           
            
        self.supp_colors = supp_colors
        if not self.supp_colors:
            self.colors = list(MAINS.values())
        else:
            self.colors = list(SUPPS.values())
        self.color_blind_mode = color_blind_mode
        self.gradients = GRADIENTS
        self.markersize = MARKERSIZE
        self.figsize = FIGSIZE
        self.autosave = AUTOSAVE
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
        self.rcParams["figure.figsize"] = self.figsize
        self.rcParams['lines.markersize'] = self.markersize
        self.rcParams['lines.linewidth'] = 2
    
    def plot(self, **kwargs):
        
        color = kwargs.pop('color', None)
        if color in list(MAINS.keys()):
            color = MAINS[color]
        elif color in list(SUPPS.keys()):
            color = SUPPS[color]
        
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
        
        gradient = self.gradients[kwargs.pop('gradient', 'strong')]
        
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
# -


