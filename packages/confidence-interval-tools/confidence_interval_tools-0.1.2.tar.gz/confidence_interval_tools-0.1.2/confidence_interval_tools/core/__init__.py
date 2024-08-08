"""
    My numpydoc description of a kind
    of very exhautive numpydoc format docstring.

    Parameters
    ----------
    first : array_like
        the 1st param name `first`
    second :
        the 2nd param
    third : {'value', 'other'}, optional
        the 3rd param, by default 'value'

    Returns
    -------
    string
        a value in a string

    Raises
    ------
    KeyError
        when a key error
    OtherError
        when an other error
"""

### TODO: write docstring, ensure it is accessible

import pandas
import numpy
import matplotlib
from matplotlib import pyplot as plt
import seaborn
from scipy import stats as sps
from typing import Literal


### A collection of types that can be used to make a plot
type datatypes = pandas.DataFrame | pandas.Series | numpy.ndarray | list | tuple | int | float
### A collection of all named matplotlib colors
exec(
    f"type matplotlib_colors_type = Literal{list(matplotlib.colors.CSS4_COLORS.keys())}"
)
### A collection of all linestyles in matplotlib
type matplotlib_linestyles_types = Literal[
    "solid", "dotted", "dashed", "dashdot", "-", ":", "--", "-.", "None", "", ","
] | tuple | None
### A collection of all marker styles in matplotlib
exec(
    f"type matplotlib_markers_type = Literal{list(matplotlib.lines.Line2D.markers.keys())}"
)


### sub-functions for calculating different types of confidence intervals
def extrapolate_quantile_value_linear(v: pandas.Series, q) -> int | float:
    """Linear extrapolation for quantiles greater than 1 or lower than 0"""
    if (q >= 0) and (q <= 1):
        return v.quantile(q)
    elif q > 1:  ## references are the last two points
        return (v.quantile(1) - v.quantile((len(v) - 2) / (len(v) - 1))) / (
            1 - (len(v) - 2) / (len(v) - 1)
        ) * (q - 1) + v.quantile(1)
    ## case q < 0 , references are the first two points
    return (v.quantile(0) - v.quantile((1) / (len(v) - 1))) / (
        0 - (1) / (len(v) - 1)
    ) * (q - 0) + v.quantile(0)


def std_ci(v: pandas.Series, std_multiplier) -> tuple:
    """Upper and lower bounds of the CI based on standard deviation (normal approximation around mean)"""
    return (
        v.mean() - std_multiplier * v.std(),
        v.mean() - std_multiplier * v.std(),
    )


def wald_ci(v: pandas.Series) -> tuple:
    """Upper and lower bounds of the CI based on Wald's binomial approximation"""
    q_lower = pandas.Series(
        [
            0.05 - 1.96 / numpy.sqrt(len(v)) * numpy.sqrt(0.05 * (1 - 0.05)),
            0.05 + 1.96 / numpy.sqrt(len(v)) * numpy.sqrt(0.05 * (1 - 0.05)),
        ]
    ).quantile(q=0.25)
    return ()


### A class for drawing a confidence interval in whatever way you prefer, from pre-defined values
### note: this requires matplotlib, matplotlib.pyplot as plt, numpy, pandas, and scipy.stats as sps
class CI_Drawer(object):
    """A class for drawing a confidence interval in whatever way you prefer, from pre-defined values."""

    def __init__(
        self,
        data: pandas.DataFrame | None = None,  # ok
        x: str | datatypes | None = None,  # ok
        y: str | datatypes | None = None,  # ok
        lower: str | datatypes | None = None,  # partial?
        upper: str | datatypes | None = None,  # partial?
        kind: (
            Literal["lines", "bars", "area", "scatterplot", "none"]
            | list[str]
            | tuple[str]
            | None
        ) = None,  # ok
        ci_type: Literal[
            "std", "Wald", "Wilson", "Clopper–Pearson", "Agresti–Coull", "Rule of three"
        ] = "std",  # ongoing
        extrapolation_type: Literal[
            "linear"
        ] = "linear",  ### TODO: add more options, such as Scholz, Hutson, etc.
        std: str | datatypes | None = None,  # ongoing
        std_multiplier: int | float = 1.96,  # ok (nothing to do?)
        orientation: Literal["horizontal", "vertical"] = "vertical",  # ok
        draw_lines: bool = False,  # ok
        draw_lower_line: bool | None = None,  # ok
        draw_upper_line: bool | None = None,  # ok
        lines_style: matplotlib_linestyles_types = "solid",  # ok
        lower_line_style: matplotlib_linestyles_types | None = None,  # ok
        upper_line_style: matplotlib_linestyles_types | None = None,  # ok
        lines_color: matplotlib_colors_type = "black",  # ok
        lower_line_color: matplotlib_colors_type | None = None,  # ok
        upper_line_color: matplotlib_colors_type | None = None,  # ok
        lines_linewidth: int | float = 1,  # ok
        lower_line_linewidth: int | float | None = None,  # ok
        upper_line_linewidth: int | float | None = None,  # ok
        lines_alpha: int | float = 0.8,  # ok
        lower_line_alpha: int | float | None = None,  # ok
        upper_line_alpha: int | float | None = None,  # ok
        draw_bars: bool = False,  # ok
        draw_bar_ends: bool | None = None,  # ok
        draw_lower_bar_end: bool | None = None,  # ok
        draw_upper_bar_end: bool | None = None,  # ok
        bars_style: matplotlib_linestyles_types = "solid",  # ok
        bars_color: matplotlib_colors_type = "black",  # ok
        bars_linewidth: int | float = 1,  # ok
        bars_alpha: int | float = 1,  # ok
        bar_ends_style: matplotlib_linestyles_types = "solid",  # ok
        bar_ends_color: matplotlib_colors_type | None = None,  # ok
        lower_bar_end_color: matplotlib_colors_type | None = None,  # ok
        upper_bar_end_color: matplotlib_colors_type | None = None,  # ok
        bar_ends_width: int | float | None = None,  # ok
        bar_ends_ratio: int | float = 0.3,  # ok
        hide_bars_center_portion: bool = False,  # ok
        bars_center_portion_length: int | float | None = None,  # ok
        bars_center_portion_ratio: int | float = 0.5,  # ok
        fill_area: bool = False,  # ok
        fill_color: matplotlib_colors_type = "lavender",  # ok
        fill_alpha: int | float = 0.4,  # ok
        plot_limits: bool = False,  # ok
        plot_lower_limit: bool | None = None,  # ok
        plot_upper_limit: bool | None = None,  # ok
        plot_marker: matplotlib_markers_type | None = None,  # ok
        lower_plot_marker: matplotlib_markers_type | None = None,  # ok
        upper_plot_marker: matplotlib_markers_type | None = None,  # ok
        plot_color: matplotlib_colors_type = "black",  # ok
        lower_plot_color: matplotlib_colors_type | None = None,  # ok
        upper_plot_color: matplotlib_colors_type | None = None,  # ok
        plot_alpha: int | float = 0.8,  # ok
        lower_plot_alpha: int | float | None = None,  # ok
        upper_plot_alpha: int | float | None = None,  # ok
        plot_size: int | float | None = None,  # ok
        lower_plot_size: int | float | None = None,  # ok
        upper_plot_size: int | float | None = None,  # ok
        binomial_ci_policy: (
            Literal[
                "conservative",
                "conservative quartile",
                "median",
                "optimistic quartile",
                "optimistic",
            ]
            | int
            | float
        ) = "conservative",  # ok
        ax: matplotlib.axes.Axes | None = None,  # ok
    ):
        ###
        #############################################################################
        ### Argument handling: type check and guessed values
        #############################################################################
        ###
        ### convert binomial_ci_policy to a numeral if it is given as a string
        if isinstance(binomial_ci_policy, str):
            if binomial_ci_policy in self.binomial_ci_policy_dict:
                binomial_ci_policy = self.binomial_ci_policy_dict[binomial_ci_policy]
            else:
                raise ValueError(
                    "'binomial_ci_policy' preset should be one of 'conservative', 'conservative quartile', 'median', optimistic quartile', 'optimistic'."
                )
        elif isinstance(binomial_ci_policy, type(int)) or isinstance(
            binomial_ci_policy, type(float)
        ):
            ### check that the numerical value is between 0 and 1
            if (binomial_ci_policy < 0) or (binomial_ci_policy > 1):
                raise ValueError(
                    "'binomial_ci_policy' should be between 0 (conservative) and 1 (optimistic) if given as a numerical value."
                )
        else:
            raise TypeError(
                "'binomial_ci_policy' should be a numerical value between 0 and 1, or one of 'conservative', 'conservative quartile', 'median', optimistic quartile', 'optimistic'."
            )
        ### check matplotlib axes on which to draw
        if isinstance(ax, type(None)):
            ax = plt.gca()
        ### check all optional arguments with None as default value
        ### case where data is provided as a pandas DataFrame
        if isinstance(data, pandas.DataFrame):
            ### check variables that could have been declared as a column name from data
            ### replace them with the numerical series they refer to
            if isinstance(x, str):
                x = data[x].copy()
            ### if x and/or y have not been declared, look for the names 'x' and 'y' in data,
            ### or assume they are the first and second columns, respectively
            elif isinstance(x, type(None)):
                if "x" in data.columns:
                    x = data["x"].copy()
                elif len(data.columns) == 1:
                    ### special case: if data only contains one column, use the index for x
                    x = data.index.copy()
                elif len(data.columns) >= 2:
                    x = data[data.columns[0]].copy()
                else:
                    raise ValueError(
                        "x can only be implicit if 'data' has at least 1 column."
                    )
            if isinstance(y, str):
                y = data[y].copy()
            elif isinstance(y, type(None)):
                if "y" in data.columns:
                    y = data["y"].copy()
                elif len(data.columns) == 1:
                    ### special case: if data only contains one column, assume that column is y
                    y = data[data.columns[0]].copy()
                elif len(data.columns) >= 2:
                    y = data[data.columns[1]].copy()
                else:
                    raise ValueError(
                        "y can only be implicit if 'data' has at least 1 column."
                    )
            if isinstance(std, str):
                std = data[std].copy()
            if isinstance(lower, str):
                lower = data[lower].copy()
            if isinstance(upper, str):
                upper = data[upper].copy()
        else:
            ### if numerical values as first argument instead of data, take them as y
            if isinstance(
                data,
                (
                    pandas.Series,
                    numpy.ndarray,
                    type(list),
                    type(tuple),
                    type(int),
                    type(float),
                ),
            ):
                y = data
            ### check variables that could have WRONGLY been declared as a column name from data without any data...
            if isinstance(x, str):
                raise TypeError(
                    "'x' can only be of type 'str' if 'data' is provided as a pandas DataFrame."
                )
            if isinstance(y, str):
                raise TypeError(
                    "'y' can only be of type 'str' if 'data' is provided as a pandas DataFrame."
                )
            elif isinstance(y, type(None)):
                raise ValueError("If 'data' is not provided, 'y' must be provided.")
            if isinstance(std, str):
                raise TypeError(
                    "'std' can only be of type 'str' if 'data' is provided as a pandas DataFrame."
                )
            if isinstance(lower, str):
                raise TypeError(
                    "'lower' can only be of type 'str' if 'data' is provided as a pandas DataFrame."
                )
            if isinstance(upper, str):
                raise TypeError(
                    "'upper' can only be of type 'str' if 'data' is provided as a pandas DataFrame."
                )
            ### TODO: add a condition to catch any numerical value passed as first argument, and save it as y unless y was specified
        ### "kind" activates one or more toggles
        if isinstance(kind, list) or isinstance(kind, tuple):
            kind = list(kind)  ## make sure kind is a list of strings
        elif isinstance(kind, str) or isinstance(kind, type(None)):
            kind = list([kind])
        else:
            raise TypeError(
                "'kind' can only be of type 'str', 'tuple[str]', 'list[str]', or set to None."
            )
        for kind_i in kind:
            if kind_i == "lines":
                draw_lines = True
            elif kind_i == "bars":
                draw_bars = True
            elif kind_i == "area":
                fill_area = True
            elif kind_i == "scatterplot":
                plot_limits = True
            elif (kind_i == "none") or (isinstance(kind_i, type(None))):
                pass
            else:
                raise ValueError(
                    "Available kinds of confidence intervals: 'lines', 'bars', 'area', 'scatterplot', 'none'."
                )

        ###
        #############################################################################
        ### Argument handling: type checking for x, y, data, and calculations
        #############################################################################
        ###
        ### Ensure the compatible formating of x and y numerical series
        y = pandas.Series(y)
        if isinstance(x, type(None)):
            x = y.index
        x = pandas.Series(x)
        ### TODO: add a check for te equal length of x and y if they were not provided as part of a dataframe
        ### check if at least one of std, lower, or upper was provided
        if (
            isinstance(std, type(None))
            and isinstance(lower, type(None))
            and isinstance(upper, type(None))
        ):
            # raise ValueError("At least one of 'std', 'lower', or 'upper' must be provided.")
            ### estimate the value of std based on the variability of y for each value of x
            ### TODO: solve the error raised when data is not provided... Reconstitute from y?
            s = pandas.Series([y.loc[x == val_x].std() for val_x in x.unique()]).fillna(
                0
            )
        ### TODO; if std was provided, use it to calculate lower and upper
        lower = pandas.Series(lower)
        upper = pandas.Series(upper)
        ###
        #############################################################################
        ### Argument handling: boolean checks and defaults for optional arguments
        #############################################################################
        ###
        ### if "sub" variables are None, they take the value of the "master" variable
        ### draw_lines
        if isinstance(draw_lower_line, type(None)):
            draw_lower_line = draw_lines
        if isinstance(draw_upper_line, type(None)):
            draw_upper_line = draw_lines
        ### lines_style
        if isinstance(lower_line_style, type(None)):
            lower_line_style = lines_style
        if isinstance(upper_line_alpha, type(None)):
            upper_line_style = lines_style
        ### lines_color
        if isinstance(lower_line_color, type(None)):
            lower_line_color = lines_color
        if isinstance(upper_line_color, type(None)):
            upper_line_color = lines_color
        ### lines_linewidth
        if isinstance(lower_line_linewidth, type(None)):
            lower_line_linewidth = lines_linewidth
        if isinstance(upper_line_linewidth, type(None)):
            upper_line_linewidth = lines_linewidth
        ### lines_alpha
        if isinstance(lower_line_alpha, type(None)):
            lower_line_alpha = lines_alpha
        if isinstance(upper_line_alpha, type(None)):
            upper_line_alpha = lines_alpha
        ### draw_bar_ends
        if isinstance(draw_bar_ends, type(None)):
            draw_bar_ends = draw_bars
        if isinstance(draw_lower_bar_end, type(None)):
            draw_lower_bar_end = draw_bar_ends
        if isinstance(draw_upper_bar_end, type(None)):
            draw_upper_bar_end = draw_bar_ends
        ### bar_ends_color
        if isinstance(bar_ends_color, type(None)):
            bar_ends_color = bars_color
        if isinstance(lower_bar_end_color, type(None)):
            lower_bar_end_color = bar_ends_color
        if isinstance(upper_bar_end_color, type(None)):
            upper_bar_end_color = bar_ends_color
        ### bar_ends_width has priority over bar_ends_ratio
        if isinstance(bar_ends_width, type(None)):
            bar_ends_width = (numpy.max(x) - numpy.min(x) + 1) / len(x) * bar_ends_ratio
        ### plot_limits
        if isinstance(plot_lower_limit, type(None)):
            plot_lower_limit = plot_limits
        if isinstance(plot_upper_limit, type(None)):
            plot_upper_limit = plot_limits
        ### plot_marker
        if isinstance(lower_plot_marker, type(None)):
            lower_plot_marker = (
                "2" if isinstance(plot_marker, type(None)) else plot_marker
            )
        if isinstance(upper_plot_marker, type(None)):
            upper_plot_marker = (
                "1" if isinstance(plot_marker, type(None)) else plot_marker
            )
        ### plot_color
        if isinstance(lower_plot_color, type(None)):
            lower_plot_color = plot_color
        if isinstance(upper_plot_color, type(None)):
            upper_plot_color = plot_color
        ### plot_size
        if isinstance(lower_plot_size, type(None)):
            lower_plot_size = plot_size
        if isinstance(upper_plot_size, type(None)):
            upper_plot_size = plot_size
        ### plot_alpha
        if isinstance(lower_plot_alpha, type(None)):
            lower_plot_alpha = plot_alpha
        if isinstance(upper_plot_alpha, type(None)):
            upper_plot_alpha = plot_alpha
        ###
        #############################################################################
        ### Instance preparation: saving variables and parameters
        #############################################################################
        ###
        self.data = data
        self.x = x
        self.y = y
        self.lower = lower
        self.upper = upper
        self.std = std
        ### Save all toggles in a dictionary
        self.params = {
            "kind": kind,
            "ci_type": ci_type,
            "extrapolation_type": extrapolation_type,
            "std_multiplier": std_multiplier,
            "orientation": orientation,
            "draw_lines": draw_lines,  ## currently not needed, but kept for now in case it would be needed later
            "draw_lower_line": draw_lower_line,
            "draw_upper_line": draw_upper_line,
            "lines_style": lines_style,
            "lower_line_style": lower_line_style,
            "upper_line_style": upper_line_style,
            "lines_color": lines_color,
            "lower_line_color": lower_line_color,
            "upper_line_color": upper_line_color,
            "lines_linewidth": lines_linewidth,
            "lower_line_linewidth": lower_line_linewidth,
            "upper_line_linewidth": upper_line_linewidth,
            "lines_alpha": lines_alpha,
            "lower_line_alpha": lower_line_alpha,
            "upper_line_alpha": upper_line_alpha,
            "draw_bars": draw_bars,
            "draw_bar_ends": draw_bar_ends,
            "draw_lower_bar_end": draw_lower_bar_end,
            "draw_upper_bar_end": draw_upper_bar_end,
            "bars_style": bars_style,
            "bars_color": bars_color,
            "bars_linewidth": bars_linewidth,
            "bars_alpha": bars_alpha,
            "bar_ends_style": bar_ends_style,
            "bar_ends_color": bar_ends_color,
            "lower_bar_end_color": lower_bar_end_color,
            "upper_bar_end_color": upper_bar_end_color,
            "bar_ends_width": bar_ends_width,
            "bar_ends_ratio": bar_ends_ratio,
            "hide_bars_center_portion": hide_bars_center_portion,
            "bars_center_portion_length": bars_center_portion_length,
            "bars_center_portion_ratio": bars_center_portion_ratio,
            "fill_area": fill_area,
            "fill_color": fill_color,
            "fill_alpha": fill_alpha,
            "plot_limits": plot_limits,
            "plot_lower_limit": plot_lower_limit,
            "plot_upper_limit": plot_upper_limit,
            "plot_marker": plot_marker,
            "lower_plot_marker": lower_plot_marker,
            "upper_plot_marker": upper_plot_marker,
            "plot_color": plot_color,
            "lower_plot_color": lower_plot_color,
            "upper_plot_color": upper_plot_color,
            "plot_alpha": plot_alpha,
            "lower_plot_alpha": lower_plot_alpha,
            "upper_plot_alpha": upper_plot_alpha,
            "plot_size": plot_size,
            "lower_plot_size": lower_plot_size,
            "upper_plot_size": upper_plot_size,
            "binomial_ci_policy": binomial_ci_policy,
        }
        self.ax = ax  # ok
        ### TODO: finish registering the variables, including calculated ones
        ###
        #############################################################################
        ### Instance preparation: method call(s) upon initialization
        #############################################################################
        ###
        self.draw()

    def __call__(self):
        pass

    ### dictionary for binomial_ci_policy
    binomial_ci_policy_dict = {
        "conservative": 0,
        "conservative quartile": 0.25,
        "median": 0.5,
        "optimistic quartile": 0.75,
        "optimistic": 1,
    }

    def help():
        print("A help message")

    def draw(self) -> None:  ## return ax instead? Or None?
        if self.params["orientation"] == "vertical":
            ### draw CI lines
            if self.params["draw_lower_line"] == True:
                seaborn.lineplot(
                    x=self.x,
                    y=self.lower,
                    color=self.params["lower_line_color"],
                    linestyle=self.params["lower_line_style"],
                    linewidth=self.params["lower_line_linewidth"],
                    alpha=self.params["lower_line_alpha"],
                )
            if self.params["draw_upper_line"] == True:
                seaborn.lineplot(
                    x=self.x,
                    y=self.upper,
                    color=self.params["upper_line_color"],
                    linestyle=self.params["upper_line_style"],
                    linewidth=self.params["upper_line_linewidth"],
                    alpha=self.params["upper_line_alpha"],
                )
            ### draw ci bars
            if self.params["draw_bars"] == True:
                if self.params["hide_bars_center_portion"] == True:
                    if isinstance(
                        self.params["bars_center_portion_length"], type(None)
                    ):  ## the length has priority over the ratio
                        bars_half_length = (
                            (self.upper - self.lower)
                            * (1 - self.params["bars_center_portion_ratio"])
                            / 2
                        )  ## with ratio
                    else:
                        bars_half_length = (
                            self.upper
                            - self.lower
                            - self.params["bars_center_portion_length"]
                        ) / 2  ## with length
                    ### lower half
                    plt.vlines(
                        x=self.x,
                        ymin=self.lower,
                        ymax=self.lower + bars_half_length,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                    ### upper half
                    plt.vlines(
                        x=self.x,
                        ymin=self.upper - bars_half_length,
                        ymax=self.upper,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                else:
                    plt.vlines(
                        x=self.x,
                        ymin=self.lower,
                        ymax=self.upper,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                ### draw bar ends
                if self.params["draw_bar_ends"] == True:
                    if self.params["draw_lower_bar_end"] == True:
                        plt.hlines(
                            y=self.lower,
                            xmin=self.x - self.params["bar_ends_width"] / 2,
                            xmax=self.x + self.params["bar_ends_width"] / 2,
                            color=self.params["lower_bar_end_color"],
                            linestyles=self.params["bar_ends_style"],
                            linewidth=self.params["bars_linewidth"],
                            alpha=self.params["bars_alpha"],
                        )
                    if self.params["draw_upper_bar_end"] == True:
                        plt.hlines(
                            y=self.upper,
                            xmin=self.x - self.params["bar_ends_width"] / 2,
                            xmax=self.x + self.params["bar_ends_width"] / 2,
                            color=self.params["upper_bar_end_color"],
                            linestyles=self.params["bar_ends_style"],
                            linewidth=self.params["bars_linewidth"],
                            alpha=self.params["bars_alpha"],
                        )
            ### fill CI area
            if self.params["fill_area"] == True:
                plt.fill_between(
                    x=self.x,
                    y1=self.lower,
                    y2=self.upper,
                    color=self.params["fill_color"],
                    alpha=self.params["fill_alpha"],
                )

            ### scatterplot of CI limits
            if self.params["plot_lower_limit"] == True:
                seaborn.scatterplot(
                    x=self.x,
                    y=self.lower,
                    color=self.params["lower_plot_color"],
                    s=self.params["lower_plot_size"],
                    marker=self.params["lower_plot_marker"],
                    alpha=self.params["lower_plot_alpha"],
                )
            if self.params["plot_upper_limit"] == True:
                seaborn.scatterplot(
                    x=self.x,
                    y=self.upper,
                    color=self.params["upper_plot_color"],
                    s=self.params["upper_plot_size"],
                    marker=self.params["upper_plot_marker"],
                    alpha=self.params["upper_plot_alpha"],
                )
        elif self.params["orientation"] == "horizontal":
            ### draw CI lines
            if self.params["draw_lower_line"] == True:
                seaborn.lineplot(
                    x=self.lower,
                    y=self.y,
                    color=self.params["lower_line_color"],
                    linestyle=self.params["lower_line_style"],
                    linewidth=self.params["lower_line_linewidth"],
                    alpha=self.params["lower_line_alpha"],
                    orient="y",
                )
            if self.params["draw_upper_line"] == True:
                seaborn.lineplot(
                    x=self.upper,
                    y=self.y,
                    color=self.params["upper_line_color"],
                    linestyle=self.params["upper_line_style"],
                    linewidth=self.params["upper_line_linewidth"],
                    alpha=self.params["upper_line_alpha"],
                    orient="y",
                )
            ### draw ci bars
            if self.params["draw_bars"] == True:
                if self.params["hide_bars_center_portion"] == True:
                    if isinstance(
                        self.params["bars_center_portion_length"], type(None)
                    ):  ## the length has priority over the ratio
                        bars_half_length = (
                            (self.upper - self.lower)
                            * (1 - self.params["bars_center_portion_ratio"])
                            / 2
                        )  ## with ratio
                    else:
                        bars_half_length = (
                            self.upper
                            - self.lower
                            - self.params["bars_center_portion_length"]
                        ) / 2  ## with length
                    ### lower half
                    plt.hlines(
                        y=self.y,
                        xmin=self.lower,
                        xmax=self.lower + bars_half_length,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                    ### upper half
                    plt.hlines(
                        y=self.y,
                        xmin=self.upper - bars_half_length,
                        xmax=self.upper,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                else:
                    plt.hlines(
                        y=self.y,
                        xmin=self.lower,
                        xmax=self.upper,
                        color=self.params["bars_color"],
                        linestyles=self.params["bars_style"],
                        linewidth=self.params["bars_linewidth"],
                        alpha=self.params["bars_alpha"],
                    )
                ### draw bar ends
                if self.params["draw_bar_ends"] == True:
                    if self.params["draw_lower_bar_end"] == True:
                        plt.vlines(
                            x=self.lower,
                            ymin=self.y - self.params["bar_ends_width"] / 2,
                            ymax=self.y + self.params["bar_ends_width"] / 2,
                            color=self.params["lower_bar_end_color"],
                            linestyles=self.params["bar_ends_style"],
                            linewidth=self.params["bars_linewidth"],
                            alpha=self.params["bars_alpha"],
                        )
                    if self.params["draw_upper_bar_end"] == True:
                        plt.vlines(
                            x=self.upper,
                            ymin=self.y - self.params["bar_ends_width"] / 2,
                            ymax=self.y + self.params["bar_ends_width"] / 2,
                            color=self.params["upper_bar_end_color"],
                            linestyles=self.params["bar_ends_style"],
                            linewidth=self.params["bars_linewidth"],
                            alpha=self.params["bars_alpha"],
                        )
            ### fill CI area
            if self.params["fill_area"] == True:
                plt.fill_betweenx(
                    y=self.y,
                    x1=self.lower,
                    x2=self.upper,
                    color=self.params["fill_color"],
                    alpha=self.params["fill_alpha"],
                )

            ### scatterplot of CI limits
            if self.params["plot_lower_limit"] == True:
                seaborn.scatterplot(
                    x=self.lower,
                    y=self.y,
                    color=self.params["lower_plot_color"],
                    s=self.params["lower_plot_size"],
                    marker=self.params["lower_plot_marker"],
                    alpha=self.params["lower_plot_alpha"],
                )
            if self.params["plot_upper_limit"] == True:
                seaborn.scatterplot(
                    x=self.upper,
                    y=self.y,
                    color=self.params["upper_plot_color"],
                    s=self.params["upper_plot_size"],
                    marker=self.params["upper_plot_marker"],
                    alpha=self.params["upper_plot_alpha"],
                )
        else:
            pass  ## if orientation is neiher horizontal nor vertical
