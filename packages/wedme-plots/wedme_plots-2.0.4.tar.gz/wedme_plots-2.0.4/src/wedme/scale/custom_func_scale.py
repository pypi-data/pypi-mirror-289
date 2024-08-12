import matplotlib as mpl
from matplotlib.scale import FuncScale
from matplotlib.ticker import (
    AutoMinorLocator,
    Formatter,
    Locator,
    MaxNLocator,
    NullFormatter,
    NullLocator,
    ScalarFormatter,
)


class CustomFuncScale(FuncScale):
    # docstring inherited
    major_locator: Locator
    minor_locator: Locator
    major_formatter: Formatter
    minor_formatter: Formatter

    def __init__(
        self,
        functions,
        max_ticks=7,
        major_locator: Locator = None,
        minor_locator: Locator = None,
        major_formatter: Formatter = None,
        minor_formatter: Formatter = None,
    ):
        super().__init__(None, functions)

        if major_locator is None:
            self.major_locator = MaxNLocator(max_ticks, prune="upper")
        if minor_locator is None:
            self.minor_locator = AutoMinorLocator()
        if major_formatter is None:
            self.major_formatter = ScalarFormatter()
        if minor_formatter is None:
            self.minor_formatter = NullFormatter()

    def set_default_locators_and_formatters(self, axis):
        # docstring inherited
        axis.set_major_locator(self.major_locator)
        axis.set_major_formatter(self.major_formatter)
        axis.set_minor_formatter(self.minor_formatter)

        # update the minor locator for x and y axis based on rcParams
        if (
            axis.axis_name == "x"
            and mpl.rcParams["xtick.minor.visible"]
            or axis.axis_name == "y"
            and mpl.rcParams["ytick.minor.visible"]
        ):
            axis.set_minor_locator(self.minor_locator)
        else:
            axis.set_minor_locator(NullLocator())
