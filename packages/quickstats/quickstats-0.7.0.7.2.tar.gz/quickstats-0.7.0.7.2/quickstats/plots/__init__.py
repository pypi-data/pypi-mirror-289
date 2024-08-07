import quickstats

from .core import *
from .color_schemes import *
from .abstract_plot import AbstractPlot
from .collective_data_plot import CollectiveDataPlot
from .stat_plot_config import *
from .hypotest_inverter_plot import HypoTestInverterPlot
from .variable_distribution_plot import VariableDistributionPlot
from .score_distribution_plot import score_distribution_plot, score_distribution_plot_2D, ScoreDistributionPlot
from .test_statistic_distribution_plot import TestStatisticDistributionPlot
from .general_1D_plot import General1DPlot
from .two_axis_1D_plot import TwoAxis1DPlot
from .general_2D_plot import General2DPlot
from .upper_limit_1D_plot import UpperLimit1DPlot
from .upper_limit_2D_plot import UpperLimit2DPlot
from .upper_limit_3D_plot import UpperLimit3DPlot
from .upper_limit_benchmark_plot import UpperLimitBenchmarkPlot
from .likelihood_1D_plot import Likelihood1DPlot
from .likelihood_2D_plot import Likelihood2DPlot
from .pdf_distribution_plot import PdfDistributionPlot
from .correlation_plot import CorrelationPlot
from .sample_purity_plot import SamplePurityPlot
from .bidirectional_bar_chart import BidirectionalBarChart
from .two_panel_1D_plot import TwoPanel1DPlot

# Reference from https://github.com/beojan/atlas-mpl
reload_styles()
use_style('hep')

register_colors(EXTRA_COLORS)
register_cmaps(QUICKSTATS_PALETTES)