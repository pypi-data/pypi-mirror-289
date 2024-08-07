from typing import Any

import matplotlib.pyplot as plt


def draw_broken_histogram(data: Any, *,
                          bottom: float, broken_bottom: float, broken_top: float, top: float, bins: int,
                          color: Any, title: str, x_label: str, y_label: str,
                          title_font_size: int = 14, x_label_font_size: int = 12):
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax1.set_ylim(broken_top, top)
    ax2.set_ylim(bottom, broken_bottom)
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    d = .01
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((-d, +d), (-d, +d), **kwargs)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    kwargs.update(transform=ax2.transAxes)
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax1.hist(data, bins=bins, color=color)
    ax2.hist(data, bins=bins, color=color)

    fig.text(0.5, 0.94, title, ha='center', fontdict={'fontsize': title_font_size})
    fig.text(0.02, 0.5, y_label, va='center', rotation='vertical')
    plt.xlabel(x_label, fontsize=x_label_font_size)

    plt.show()
