"""
Computer Science Education - Visualization of Distributions

This module provides functions for visualizing two distributions that can typically
be used in computer science education. It uses Matplotlib to display two distributions
side by side as line or bar charts.

Functions:
- show_distributions(distribution1, distribution2, title1="", title2="", mode="Lines"):
    Visualizes two distributions as line or bar charts.

Parameters:
- distribution1: A list or array representing the first distribution.
- distribution2: A list or array representing the second distribution.
- title1: Title for the first chart (default: empty).
- title2: Title for the second chart (default: empty).
- mode: Display mode, either "Lines" (default) or "Bars".

Example Usage:
    distribution1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    distribution2 = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    show_distributions(distribution1, distribution2, "Distribution 1", "Distribution 2", "Bars")

Note:
This module was specifically developed for use in computer science education and offers
an easy way to perform basic data visualizations. It can be reused in other projects
that have similar visualization requirements.

Author:
- Henning Mattes

License:
- MIT License with addition: See LICENSE.txt file in the repository

Dependencies:
- matplotlib

"""

import matplotlib.pyplot as plt

def show_distributions(distribution1, distribution2, title1="", title2="", mode="Lines"):
    
    def letter(code26number):
        return chr(code26number + ord("A"))
    
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    ticks = range(1, 27)
    labels = [letter(i-1) for i in ticks]
    for ax, distribution, title, color in zip(axs, [distribution1, distribution2], [title1, title2], ["red", "blue"]):
        if mode.upper() == "BARS":
            ax.bar(ticks, distribution, align='center', color=color)
        else:
            ax.plot(ticks, distribution, marker="x", color=color)
        ax.grid()
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
        ax.set_title(title)
    plt.show()
