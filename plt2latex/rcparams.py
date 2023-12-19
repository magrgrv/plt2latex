from .units import *
import matplotlib
import matplotlib.pyplot as plt


def rcparams_initial_update():

    textwidth = 300  # pt
    ratio = 4/3
    textwidth = convert_units('pt', 'in', textwidth)
    fontsize = 10
    plt.style.use('classic')

    matplotlib.rcParams.update({
        'pgf.texsystem': "pdflatex",
        'lines.linewidth': 0.5,
        'font.family': 'serif',
        'text.usetex': True,
        # 'text.latex.preamble': LaTeX,
        'pgf.rcfonts': False,
        'legend.title_fontsize': fontsize,
        'font.size': fontsize,  # controls default text sizes
        'axes.titlesize': fontsize,  # fontsize of the axes title
        'axes.labelsize': fontsize,  # fontsize of the x and y labels
        'xtick.labelsize': fontsize,  # fontsize of the tick labels
        'ytick.labelsize': fontsize,  # fontsize of the tick labels
        'legend.fontsize': fontsize,  # legend fontsize
        'figure.titlesize': fontsize,  # fontsize of the figure title
        'figure.figsize': (textwidth, textwidth/ratio),
        'axes.grid': True,
        'axes.titlepad': 4.0,
        'axes.labelpad': 2.0,
        'axes.axisbelow': False,
        'legend.fancybox': False,
        'legend.borderpad': 0.4,
        'figure.autolayout': True,
        'axes.xmargin': .05,  # x margin.  See `axes.Axes.margins`
        'axes.ymargin': .05,  # y margin.  See `axes.Axes.margins`
        'axes.zmargin': .05,  # z margin.  See `axes.Axes.margins`
        'axes.autolimit_mode': "data",
        'errorbar.capsize': 1,
        'lines.markersize': 3,
        'boxplot.boxprops.linewidth': 0.5,
        'boxplot.whiskerprops.linewidth': 0.5,
        'boxplot.capprops.linewidth': 0.5,
        'boxplot.medianprops.linewidth': 0.5,
        'boxplot.meanprops.linewidth': 0.5,
        'axes.linewidth': 0.5,
        'axes.grid.which': "both",
        'legend.numpoints': 1,
        'figure.dpi': 144,
        'figure.facecolor': "white",
    })


# def set_size(ratio=(5 ** .5 - 1) / 2, width_pt=textwidth, fraction=1, subplots=(1, 1)):
#     """Set figure dimensions to sit nicely in our document.
#
#     Parameters
#     ----------
#     width_pt: float
#             Document width in points
#     fraction: float, optional
#             Fraction of the width which you wish the figure to occupy
#     subplots: array-like, optional
#             The number of rows and columns of subplots.
#     Returns
#     -------
#     fig_dim: tuple
#             Dimensions of figure in inches
#     """
#     # Width of figure (in pts)
#     fig_width_pt = width_pt * fraction
#     # Convert from pt to inches
#     inches_per_pt = 1 / 72.27
#
#     # Golden ratio to set aesthetic figure height
#
#     # Figure width in inches
#     fig_width_in = fig_width_pt * inches_per_pt
#     # Figure height in inches
#     fig_height_in = fig_width_in * ratio * (subplots[0] / subplots[1])
#
#     return (fig_width_in, fig_height_in)
#
#
# def set_width(width_pt, fraction=1, subplots=(1, 1)):
#     """Set figure dimensions to sit nicely in our document.
#
#     Parameters
#     ----------
#     width_pt: float
#             Document width in points
#     fraction: float, optional
#             Fraction of the width which you wish the figure to occupy
#     subplots: array-like, optional
#             The number of rows and columns of subplots.
#     Returns
#     -------
#     fig_dim: tuple
#             Dimensions of figure in inches
#     """
#     # Width of figure (in pts)
#     fig_width_pt = width_pt * fraction
#     # Convert from pt to inches
#     inches_per_pt = 1 / 72
#
#     # Golden ratio to set aesthetic figure height
#     golden_ratio = (5 ** .5 - 1) / 2
#
#     # Figure width in inches
#     fig_width_in = fig_width_pt * inches_per_pt
#     # Figure height in inches
#     fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])
#
#     return (fig_width_in)
