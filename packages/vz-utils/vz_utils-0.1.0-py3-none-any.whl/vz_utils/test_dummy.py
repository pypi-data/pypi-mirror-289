import numpy as np
import matplotlib.pyplot as plt

from ._utils import *


def test_draw_broken_histogram(random_state: int):
    random_gen = np.random.RandomState(seed=random_state)
    dummy_data = random_gen.randint(low=0, high=100, size=250)
    dummy_data = np.concatenate((dummy_data, random_gen.randint(low=10, high=20, size=750)))

    plt.hist(x=dummy_data, bins=20, color='#aa2244')
    plt.title('Normal histogram', fontsize=14)
    plt.xlabel('x_label', fontsize=12)
    plt.ylabel('Freq')
    plt.show()

    draw_broken_histogram(data=dummy_data,
                          bottom=0, broken_bottom=30, broken_top=200, top=600, bins=20, color='#66aa33',
                          title="Broken histogram", x_label='x_label', y_label='Freq')
