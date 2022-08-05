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
from matplotlib import font_manager
from customplotlib.customization.config import *
from customplotlib.customization import processing
from cycler import cycler
from datetime import datetime
import numpy as np
import pandas as pd
import os

    
class Customplotlib():
    def __init__(self, supp_colors=False, color_blind_mode=False):
        
        for i in dir(pyplot):
            if i not in ['scatter', 'plot', 'matshow']:
                setattr(self, i, getattr(pyplot, i))
            
        font_dirs = ['customplotlib/customization/fonts/']
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

        for font_file in font_files:
            font_manager.fontManager.addfont(font_file)
        
        self.supp_colors = supp_colors
        if not self.supp_colors:
            self.colors = list(MAINS.values())
        else:
            self.colors = list(SUPPS.values())
            
        self.color_blind_mode = color_blind_mode
        
        self.gradients = GRADIENTS
        
        self.font = FONT.lower()
        self.fontsize = FONTSIZE
        
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
            
            
        
        self.rcParams["font.family"] = self.font
        self.rcParams["font.size"] = self.fontsize
        self.rcParams["figure.figsize"] = self.figsize
        self.rcParams['lines.markersize'] = self.markersize
        self.rcParams['lines.linewidth'] = 2
    
    def plot(self, **kwargs):
        
        title = kwargs.pop('title',False)
        xlabel = kwargs.pop('xlabel',False)
        ylabel = kwargs.pop('ylabel',False)
        label = kwargs.get('label', None)
        legend = kwargs.get('legend', True)
        legend_loc = kwargs.get('legend_loc', LEGEND_LOC)
        
        if label:
            if (type(kwargs.get('label')) == str) & ('data' in kwargs.keys()):
                data_df = kwargs.pop('data').copy()

                input_x_name = kwargs.pop('x')
                input_y_name = kwargs.pop('y')

                data_df['x'] = data_df[input_x_name]
                data_df['y'] = data_df[input_y_name]

                xlabel = input_x_name if not xlabel else xlabel
                ylabel = input_y_name if not ylabel else ylabel
                
                data_df.sort_values(by=kwargs.get('label'), inplace=True)
                groups = data_df.groupby(kwargs.pop('label'), sort=True)
            else:
                data_df = pd.DataFrame({'x': kwargs.pop('x'),
                                        'y': kwargs.pop('y'),
                                        'label': kwargs.pop('label')})
                data_df.sort_values(by='label', inplace=True)
                groups = data_df.groupby('label', sort=True)
            
            for name, group in groups:                
                pyplot.plot(group.x, group.y, **kwargs, label=name)

        else:
            x = kwargs.pop('x', None)
            y = kwargs.pop('y', None)
            pyplot.plot(x,y,**kwargs)
        
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
        
        title = kwargs.pop('title',False)
        xlabel = kwargs.pop('xlabel',False)
        ylabel = kwargs.pop('ylabel',False)
        label = kwargs.get('label', None)
        legend = kwargs.get('legend', True)
        legend_loc = kwargs.get('legend_loc', LEGEND_LOC)
        
        if label:
            if (type(kwargs.get('label')) == str) & ('data' in kwargs.keys()):
                data_df = kwargs.pop('data').copy()
                input_x_name = kwargs.pop('x')
                input_y_name = kwargs.pop('y')

                data_df['x'] = data_df[input_x_name]
                data_df['y'] = data_df[input_y_name]

                xlabel = input_x_name if not xlabel else xlabel
                ylabel = input_y_name if not ylabel else ylabel
                
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
                
                pyplot.scatter(*args, **kwargs, x=group.x, y=group.y, label=name)

        else:
            pyplot.scatter(*args, **kwargs)
        
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
        
        gradient = self.gradients[kwargs.pop('gradient', 'strong')]
        
        if kwargs.pop('invert', False):
                gradient.reverse()
                
        cmap = processing.get_gradient(gradient)
        
        pyplot.matshow(*args, **kwargs, cmap=cmap) 
        
        #self.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=45)
        #self.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
        
        cb = self.colorbar()
        #cb.ax.tick_params(labelsize=14)
        
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


