from typing import Union
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pathlib import Path
from datetime import datetime


def savefig(
    pathstub,
    fig: Union[Figure, None] = None,
    format=[".png", ".pdf"],
    dpi=1000,
    history=False,
):
    # If multiple formats are given, recursively call this function for each
    if type(format) == list:
        for f in format:
            savefig(pathstub, fig, f, dpi, history)
        return

    # If a figure handle is given, make sure it is displayed
    if fig is not None:
        fig.show()

    path = Path(pathstub).with_suffix(format)
    path.parent.mkdir(exist_ok=True)

    # If history is enabled, save a copy of the figure in the history directory
    if history:
        dir_history = path.parent / "history"

        savefig(
            dir_history / f"{path.stem}_{datetime.now().strftime(r'%Y%m%d-%H%M%S')}",
            fig,
            format,
            dpi,
            history=False,
        )

    # Save the figure
    plt.savefig(path, dpi=dpi, facecolor="#00f0", pad_inches=0)
