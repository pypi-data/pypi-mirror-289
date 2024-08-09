# Computer Science Education - Image Processing Module and Visualization of Distributions
![Image Description](https://raw.githubusercontent.com/henningmattes/diverse/main/csedu_package_img_small.png)

## Description

This project consists of two modules for computer science education:

- **Image Processing**: A module for simple editing and analysis of images. It allows loading, saving, and displaying images, calculating color depths, and converting palette-based images to RGB.

- **Visualization of Distributions**: A module for visualizing two distributions side by side as line or bar charts. Ideal for presenting statistical data in educational settings.

## Modules

### imageprocessing

This module provides functions for simple processing and analysis of images. The main functions are:

- `load_image(path_and_filename)`: Loads an image and calculates its color depth.
- `transform_palette_image_to_rgb(np_image_array, palette)`: Transforms a palette-based image into an RGB image.
- `pillow_image(numpy_array, palette=None)`: Converts a NumPy array into a Pillow image.
- `save_image(path, np_image_array, palette=None)`: Saves an image to a file.
- `show(image_data, show_axes=True, label_data=None, palette_data=None, show_grid=False, grid_color='black', number_of_ticks=None, number_of_columns=1, figsize=None)`: Displays images in a plot.
- `plot_histogram(histogram, palette='inferno')`: Plots a histogram of the brightness values of an image.

### diagrams

This module provides a simple way to visualize two distributions. The main function is:

- `show_distributions(distribution1, distribution2, title1="", title2="", mode="Lines")`: Visualizes two distributions as line or bar charts.

## Example Usage

### Image Processing

```python
from imageprocessing import load_image, show, save_image

# Load image and calculate color depth
image, color_mode, color_depth, palette = load_image('path/to/image.png')
print(f"Color depth: {color_depth} Bit")

# Display image
show(image)

# Save image
save_image('path/to/output_image.png', image, palette)

```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) with additional terms for attribution. See the [LICENSE](https://raw.githubusercontent.com/henningmattes/diverse/main/LICENSE.txt) file for details.
