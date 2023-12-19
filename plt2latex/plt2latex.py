from .units import *
import matplotlib


def set_figsize(width_pt, height_pt):
    width_in = convert_units('pt', 'in', width_pt)
    height_in = convert_units('pt', 'in', height_pt)
    matplotlib.rcParams.update({
        'figure.figsize': (width_in, height_in)
    })


def set_font(fontsize=12):
    matplotlib.rcParams.update({
        'legend.title_fontsize': fontsize,
        'font.size': fontsize,  # controls default text sizes
        'axes.titlesize': fontsize,  # fontsize of the axes title
        'axes.labelsize': fontsize,  # fontsize of the x and y labels
        'xtick.labelsize': fontsize,  # fontsize of the tick labels
        'ytick.labelsize': fontsize,  # fontsize of the tick labels
        'legend.fontsize': fontsize,  # legend fontsize
        'figure.titlesize': fontsize,  # fontsize of the figure title
    })
