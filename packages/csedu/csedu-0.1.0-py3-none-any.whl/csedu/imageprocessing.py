"""
Computer Science Education - Image Processing Module

This module provides functions for very simple processing and analysis of images.
It allows loading, saving, and displaying images, as well as calculating color depths
and transforming palette-based images into RGB.

Author:
- Henning Mattes

License:
- MIT License with addition: See LICENSE.txt file in the repository

Dependencies:
- numpy
- matplotlib
- pillow

Example Usage:

    # Load image and calculate color depth
    image, color_mode, color_depth, palette = load_image('path/to/image.png')
    print(f"Color depth: {color_depth} Bit")

    # Display image
    show(image)

    # Save image
    save_image('path/to/output_image.png', image, palette)

"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.cm as cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

def numpy_array(image):
    original_color_mode = image.mode
    return (np.array(image), original_color_mode)

# Function to calculate the color depth
def calculate_color_depth(image):
    color_mode = image.mode
    if color_mode == '1':  # Binary mode
        return 1
    elif color_mode == 'L':  # 8-bit grayscale
        return 8
    elif color_mode == 'RGB':  # 24-bit color
        return 24
    elif color_mode == 'RGBA':  # 32-bit color with alpha
        return 32
    elif color_mode == 'P':  # Palette
        palette = image.getpalette()
        number_of_colors = len({tuple(palette[i:i+3]) for i in range(0, len(palette), 3)})
        if number_of_colors <= 16:
            return 4  # 4 bits for 16 colors
        else:
            return 8  # 8 bits for more than 16 colors
    else:
        return 'Unknown'

def transform_palette_image_to_rgb(np_image_array, palette):
    # Create an empty image with the same size as the input image
    image = np.zeros((np_image_array.shape[0], np_image_array.shape[1], 3), dtype=np.uint8)
    
    # Replace color values with the values from the palette
    for i in range(np_image_array.shape[0]):
        for j in range(np_image_array.shape[1]):
            image[i, j] = palette[np_image_array[i, j]]
    
    return image

def load_image(path_and_filename):
    pil_image = Image.open(path_and_filename)
    image, color_mode = numpy_array(pil_image)
    if color_mode == 'P':  # Palette
        palette = pil_image.getpalette()
        # Convert the flat palette into a 2D NumPy array (N x 3), where N is the number of colors
        palette_array = np.array(palette).reshape((-1, 3))
    else:
        palette_array = None
    return image, color_mode, calculate_color_depth(pil_image), palette_array

def pillow_image(numpy_array, palette=None):
    # Determine the color mode based on the shape and palette
    if palette is not None:
        color_mode = 'P'
        image = Image.fromarray(numpy_array.astype('uint8'), 'P')
        flat_palette = palette.flatten().tolist()
        image.putpalette(flat_palette)
    elif numpy_array.ndim == 2:
        color_mode = 'L'
        image = Image.fromarray(numpy_array, 'L')
    elif numpy_array.shape[2] == 3:
        color_mode = 'RGB'
        image = Image.fromarray(numpy_array, 'RGB')
    elif numpy_array.shape[2] == 4:
        color_mode = 'RGBA'
        image = Image.fromarray(numpy_array, 'RGBA')
    else:
        raise ValueError("Unknown format or color mode cannot be determined")

    return image

def save_image(path, np_image_array, palette=None):
    # Create the Pillow image, now with a possible palette
    pillow_image = pillow_image(np_image_array, palette)
    # Save the image
    pillow_image.save(path)

def transform_palette_image_to_rgb(np_image_array, palette):
    # Create an empty image with the same size as the input image
    image = np.zeros((np_image_array.shape[0], np_image_array.shape[1], 3), dtype=np.uint8)
    
    # Replace color values with the values from the palette
    for i in range(np_image_array.shape[0]):
        for j in range(np_image_array.shape[1]):
            image[i, j] = palette[np_image_array[i, j]]
    
    return image

def show(image_data, show_axes=True, label_data=None, palette_data=None, show_grid=False, grid_color='black', number_of_ticks=None, number_of_columns=1, figsize=None):
    if not isinstance(image_data, list):
        image_data = [image_data]  # Convert single image into a list for consistent processing

    def prepare_parameter_list(param, name, length):
        if isinstance(param, list):
            if len(param) != length:
                raise ValueError(f"When a list is passed for image_data, a list may (but does not have to) also be passed for '{name}'. "
                                 + f"In this case, the length of the list '{name}' must match the length of the "
                                 + f"image_data list.")
        else:
            param = [param] * length
        return param

    palette_data = prepare_parameter_list(palette_data, 'palette_data', len(image_data))
    label_data = prepare_parameter_list(label_data, 'label_data', len(image_data))
    show_grid = prepare_parameter_list(show_grid, 'show_grid', len(image_data))
    grid_color = prepare_parameter_list(grid_color, 'grid_color', len(image_data))
    number_of_ticks = prepare_parameter_list(number_of_ticks, 'number_of_ticks', len(image_data))

    number_of_images = len(image_data)
    number_of_rows = np.ceil(number_of_images / number_of_columns).astype(int)

    # Create subplots
    if figsize is None:
        figsize = (number_of_columns * 5, number_of_rows * 5)
    fig, axs = plt.subplots(number_of_rows, number_of_columns, figsize=figsize)
    axs = np.ravel([axs])

    for idx, image in enumerate(image_data):
        ax = axs[idx]
        if label_data[idx] is not None:
            ax.set_title(label_data[idx])

        current_palette = palette_data[idx]
        if isinstance(current_palette, np.ndarray):
            image = transform_palette_image_to_rgb(image, current_palette)
            ax.imshow(image)
        else:
            cmap = current_palette if current_palette is not None else 'gray'
            ax.imshow(image, cmap=cmap)

        if show_axes:
            ax.axis('on')
            if number_of_ticks[idx] is not None:
                ticks_x = np.linspace(0, image.shape[1] - 1, num=number_of_ticks[idx], dtype=int)
                ticks_y = np.linspace(0, image.shape[0] - 1, num=number_of_ticks[idx], dtype=int)
                ax.set_xticks(ticks_x)
                ax.set_yticks(ticks_y)
                ax.set_xticklabels(ticks_x)
                ax.set_yticklabels(ticks_y)
        else:
            ax.axis('off')

        if show_grid[idx]:
            ax.set_xticks(np.arange(-.5, image.shape[1], 1), minor=True)
            ax.set_yticks(np.arange(-.5, image.shape[0], 1), minor=True)
            ax.grid(which="minor", color=grid_color[idx], linestyle='-', linewidth=1)
            ax.tick_params(which="minor", size=0)
        else:
            ax.grid(False)

    plt.tight_layout()
    plt.show()

def plot_histogram(histogram, palette='inferno'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    # Find min and max for normalization
    # Ignore 0 values for min determination
    non_zero_values = histogram[np.nonzero(histogram)]
    if non_zero_values.size == 0:  # Case when the histogram contains only zeros
        min_val = 0
    else:
        min_val = non_zero_values.min()
    max_val = histogram.max()

    # Create normalization object
    norm = Normalize(vmin=min_val, vmax=max_val)
    cmap = plt.get_cmap(palette)
    
    # ScalarMappable for the colorbar
    mappable = ScalarMappable(norm=norm, cmap=cmap)

    # Draw bars with colors based on the height of the bar
    # Draw all bars, including those with a value of 0, to use color 0
    for i in range(256):
        color = cmap(0) if histogram[i] == 0 else cmap(norm(histogram[i]))
        ax.bar(i, histogram[i], color=color, width=1)

    ax.set_title('Histogram')
    ax.set_xlabel('Brightness/Luminance Values (0-255)')
    ax.set_ylabel('Number of Pixels')

    ax.set_xlim(0, 255)
    ax.set_ylim(0, max(histogram) + max(histogram) * 0.05)

    ax.set_xticks(range(0, 256, 50))
    y_ticks_max = max(histogram) + 1
    ax.set_yticks(np.linspace(0, y_ticks_max, num=5, endpoint=True))
    ax.tick_params(axis='both', which='major', labelsize=8)

    # Add colorbar
    fig = ax.figure
    cbar = fig.colorbar(mappable, ax=ax)
    cbar.set_label('Number of Pixels')
    plt.show()
