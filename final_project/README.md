# Image Blurring and Histogram Analysis in Python

This project demonstrates how to load an image, convert it to grayscale, apply a Gaussian blur, visualize grayscale histograms, and statistically compare the distributions before and after blurring using Python.

## What the Code Does

- Loads a 500x500 pixel PNG image (`final_project.png`)
- Applies a Gaussian blur using `scipy.ndimage.gaussian_filter`
- Converts the RGB image to grayscale
- Plots grayscale histograms of both the original and blurred images
- Performs a Chi-squared statistical test on the histograms
- Writes two output images:
  - `blurred_final_project.png` (blurred image)
  - `blurred_final_project_downscaled.png` (blurred + downscaled to 250x250 pixels)

## Requirements

To run this code, you’ll need the following Python packages:

- `matplotlib`
- `numpy`
- `scipy`
- `Pillow`

Install them using pip:

```bash
pip install matplotlib numpy scipy Pillow