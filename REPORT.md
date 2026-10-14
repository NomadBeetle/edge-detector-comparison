# Edge Detector Comparison and Analysis Tool

## 1. Abstract

Edge detection is an important operation in Computer Vision that identifies boundaries and significant intensity changes in digital images. Different edge detection techniques respond differently to image structures and noise.

This project implements and compares four classical edge detection methods: Sobel, Canny, Laplacian of Gaussian (LoG), and Difference of Gaussians (DoG). The application is developed in Python and executed through the command line.

A synthetic grayscale image containing geometric shapes is used as the input. Gaussian noise is added at five levels: 0, 5, 15, 25, and 40. The output of each detector is evaluated using execution time, edge density, and percentage change in edge density relative to the clean image.

The program automatically generates individual edge maps, a comparison grid, a CSV file containing experimental measurements, noisy images, and a noise-robustness plot. The experiment demonstrates that the four methods respond differently as noise increases. The findings are specific to the selected image, implementation, and parameter settings.

## 2. Introduction

Computer Vision involves processing digital images to extract useful information. One of its fundamental operations is edge detection, which identifies locations where image intensity changes significantly.

Edges represent important structural information, such as the boundaries of objects and transitions between regions. They are useful in image segmentation, shape recognition, object detection, feature extraction, and industrial inspection.

Several edge detection algorithms have been developed, each using a different approach to identify boundaries. Gradient-based methods estimate changes in intensity, while other methods use smoothing, second-order derivatives, or differences between blurred images.

This project compares four classical techniques:

1. Sobel edge detector
2. Canny edge detector
3. Laplacian of Gaussian (LoG)
4. Difference of Gaussians (DoG)

The project also investigates how Gaussian noise affects the output of these algorithms.

## 3. Problem Statement

The objective of this project is to develop a command-line application that applies multiple edge detection methods to the same input image and compares their outputs.

The project further investigates the effect of increasing Gaussian noise on edge detection results.

The comparison considers:

- Visual differences between edge maps.
- Execution time of each detector.
- Edge density of the resulting images.
- Percentage change in edge density relative to the clean image.
- Changes in detector behaviour at different noise levels.

## 4. Objectives

The main objectives are:

1. To understand the principles of classical edge detection.
2. To implement Sobel convolution manually using NumPy.
3. To apply Canny, LoG, and DoG edge detection.
4. To compare the outputs of all four algorithms.
5. To generate synthetic test images containing geometric shapes.
6. To introduce different levels of Gaussian noise.
7. To measure execution time and edge density.
8. To calculate the percentage change in edge density.
9. To generate comparison images, CSV measurements, and plots automatically.
10. To develop a reproducible command-line Computer Vision application.

## 5. Background and Theory

### 5.1 Edge Detection

An edge is a location in an image where pixel intensity changes significantly. Edge detection identifies these changes and represents them as boundaries or edge responses.

The quality of an edge map depends on factors such as image contrast, noise, algorithm parameters, and the characteristics of the input image.

### 5.2 Sobel Edge Detector

The Sobel operator estimates image gradients in the horizontal and vertical directions using two convolution kernels.

The gradient magnitude is calculated as:

\[
G=\sqrt{G_x^2+G_y^2}
\]

where \(G_x\) and \(G_y\) represent horizontal and vertical gradient responses.

In this project, the convolution is implemented manually using NumPy. The resulting gradient magnitude is normalized to an 8-bit grayscale image.

Sobel is relatively simple to understand and implement. However, noise can create additional intensity variations that may be interpreted as edges.

### 5.3 Canny Edge Detector

Canny is a multi-stage edge detection algorithm. Its main stages include:

1. Gaussian smoothing to reduce noise.
2. Gradient calculation.
3. Non-maximum suppression to thin edge responses.
4. Double thresholding.
5. Edge tracking through hysteresis.

In this project, the image is first smoothed using a Gaussian filter with a kernel size of 5 × 5 and a sigma of 1.0. Canny is then applied using thresholds of 100 and 200.

### 5.4 Laplacian of Gaussian (LoG)

LoG combines Gaussian smoothing with the Laplacian operator.

The Gaussian filter reduces small intensity variations before the second-order derivative is calculated. The absolute Laplacian response is then normalized to an 8-bit image.

This method can identify rapid intensity changes, although its output remains dependent on smoothing and threshold settings.

### 5.5 Difference of Gaussians (DoG)

DoG subtracts two differently blurred versions of the same image.

In this project, the image is blurred using two Gaussian filters with kernel sizes of 5 × 5 and 9 × 9. The absolute difference between the two results is calculated and thresholded.

The method emphasizes structures that respond differently at the two smoothing scales. Its output depends on the selected Gaussian parameters and threshold.

### 5.6 Gaussian Noise

Gaussian noise is random variation added to image pixel intensities. It can introduce unwanted intensity changes and affect edge detection.

The noisy image is generated using:

\[
I_{\text{noisy}}=\operatorname{clip}(I+N,0,255)
\]

where \(I\) is the original grayscale image and \(N\) is Gaussian noise with mean zero and a specified standard deviation.

The clipping operation ensures that pixel values remain within the valid 8-bit range of 0 to 255.

## 6. Technologies Used

### Python

Python is used as the primary programming language because of its support for numerical computing and image processing.

### NumPy

NumPy is used for array operations, Gaussian noise generation, gradient calculations, and manual Sobel convolution.

### OpenCV

OpenCV is used for image loading, image saving, Gaussian filtering, Canny detection, Laplacian operations, and image thresholding.

### Matplotlib

Matplotlib is used to create the comparison grid and noise-robustness plot.

### CSV

CSV is used to store the experimental measurements in a structured format.

### Visual Studio Code

Visual Studio Code is used as the development environment for writing and executing the Python programs.

## 7. Project Structure

The project contains the following files and folders:

```text
EdgeDetectorProject/
├── sample_images/
│   └── synthetic_test.png
├── results/
│   ├── edges_sobel.png
│   ├── edges_canny.png
│   ├── edges_log.png
│   ├── edges_dog.png
│   ├── comparison_grid.png
│   ├── noise_experiment.csv
│   ├── noise_robustness_plot.png
│   ├── noisy_sigma_5.png
│   ├── noisy_sigma_15.png
│   ├── noisy_sigma_25.png
│   └── noisy_sigma_40.png
├── create_sample.py
├── edge_detectors.py
├── main.py
├── requirements.txt
├── README.md
└── REPORT.md
```

## 8. Implementation

The implementation is divided into three main Python files.

### 8.1 create_sample.py

This file generates a synthetic grayscale image of size 512 × 512 pixels. It contains geometric shapes, including rectangles, a circle, a triangle, and lines.

The synthetic image provides clear boundaries for testing the edge detection algorithms.

The generated image is saved as `sample_images/synthetic_test.png`.

### 8.2 edge_detectors.py

This file contains the four edge detection functions.

- `sobel_detector()` calculates horizontal and vertical gradients using manual NumPy convolution.
- `canny_detector()` applies Gaussian smoothing followed by Canny edge detection.
- `log_detector()` smooths the image and calculates the absolute Laplacian response.
- `dog_detector()` subtracts two Gaussian-blurred images and applies thresholding.

The functions return grayscale edge-response images that are subsequently processed by the main program.

### 8.3 main.py

This file controls the complete experiment.

Its main responsibilities include:

- Reading the input image.
- Parsing command-line arguments.
- Generating noisy images.
- Applying all four edge detectors.
- Measuring execution time.
- Calculating edge density.
- Calculating percentage changes relative to the clean image.
- Saving individual edge maps.
- Generating the comparison grid.
- Exporting measurements to CSV.
- Generating the noise-robustness plot.

The program uses a fixed random seed of 42 for reproducible noise generation under the same software and execution conditions.

## 9. Methodology

The experiment follows these steps.

### Step 1: Input Image

The synthetic grayscale image is loaded from the `sample_images` directory.

### Step 2: Noise Generation

Gaussian noise is added at five levels.

| Noise sigma | Description |
|---:|---|
| 0 | Clean image |
| 5 | Low noise |
| 15 | Moderate noise |
| 25 | Higher noise |
| 40 | High noise |

### Step 3: Edge Detection

Each clean or noisy image is processed using Sobel, Canny, LoG, and DoG.

### Step 4: Binary Edge Map

For measuring edge density, the returned edge-response image is thresholded at 50 to produce a binary map.

A pixel is counted as an edge when its resulting intensity is nonzero.

### Step 5: Runtime Measurement

Execution time is measured using Python's `time.perf_counter()` function. The measurement covers the detector call and subsequent binary-map conversion.

### Step 6: Edge Density Calculation

Edge density is calculated as:

\[
D=\frac{N_e}{N}
\]

where:

- \(D\) is edge density.
- \(N_e\) is the number of pixels classified as edges.
- \(N\) is the total number of pixels.

### Step 7: Percentage Change

The change in edge density is calculated relative to the clean image:

\[
\Delta D(\%)=\frac{D_\sigma-D_0}{D_0}\times100
\]

where \(D_\sigma\) is the edge density at a particular noise level and \(D_0\) is the corresponding clean-image edge density.

A positive value indicates an increase in edge density, while a negative value indicates a decrease.

### Step 8: Result Generation

The program saves the individual edge maps, noisy images, comparison grid, CSV measurements, and noise-robustness plot in the `results` directory.

## 10. Experimental Results

The experiment was executed successfully using a 512 × 512 synthetic grayscale image.

All four detectors were evaluated at each of the five noise levels, producing 20 experimental observations.

### 10.1 Edge Density of the Clean Image

| Method | Edge density |
|---|---:|
| Sobel | 0.0256 |
| Canny | 0.0126 |
| LoG | 0.0373 |
| DoG | 0.0478 |

For the clean image, DoG produced the highest measured edge density, while Canny produced the lowest.

These differences reflect the algorithms' distinct processing methods and the thresholding procedure used in the experiment. A higher edge density does not necessarily indicate better detection accuracy.

### 10.2 Edge Density at Different Noise Levels

| Noise sigma | Sobel | Canny | LoG | DoG |
|---:|---:|---:|---:|---:|
| 0 | 0.0256 | 0.0126 | 0.0373 | 0.0478 |
| 5 | 0.0256 | 0.0132 | 0.0328 | 0.0469 |
| 15 | 0.0255 | 0.0132 | 0.0351 | 0.0447 |
| 25 | 0.0295 | 0.0132 | 0.0446 | 0.0431 |
| 40 | 0.0810 | 0.0166 | 0.0956 | 0.0471 |

The results indicate that the effect of noise differs between the algorithms.

Sobel and LoG show substantial increases in edge density at the highest noise level. Canny changes relatively little at lower noise levels, while DoG remains comparatively stable in terms of edge density across the tested range.

### 10.3 Percentage Change in Edge Density

| Noise sigma | Sobel | Canny | LoG | DoG |
|---:|---:|---:|---:|---:|
| 0 | 0.00% | 0.00% | 0.00% | 0.00% |
| 5 | 0.15% | 5.04% | -12.09% | -1.82% |
| 15 | -0.24% | 5.07% | -6.05% | -6.45% |
| 25 | 15.22% | 5.37% | 19.47% | -9.80% |
| 40 | 216.49% | 31.72% | 155.84% | -1.34% |

The results show that:

- **Sobel:** Edge density increases by 216.49% at noise sigma 40.
- **Canny:** Edge density increases by 31.72% at noise sigma 40, with comparatively small changes at lower noise levels.
- **LoG:** Edge density increases by 155.84% at noise sigma 40.
- **DoG:** Edge density remains close to its clean-image value, with a net change of -1.34% at noise sigma 40.

Negative changes indicate that fewer pixels passed the selected edge threshold than in the clean-image result. They do not necessarily indicate improved or degraded accuracy.

### 10.4 Runtime Analysis

The measured execution times for the clean image were:

| Method | Runtime (ms) |
|---|---:|
| Sobel | 10.50 |
| Canny | 2.09 |
| LoG | 1.99 |
| DoG | 1.27 |

In this particular run, DoG had the lowest measured runtime, followed by LoG and Canny. Sobel had the highest runtime because its gradient calculation uses explicit loops over the convolution kernel and full image arrays.

These measurements are not fixed benchmarks. Runtime can vary according to hardware, software environment, image dimensions, and system load.

## 11. Visual Results

The program generates the following visual outputs.

### 11.1 Comparison Grid

![File: `results/comparison_grid.png`](results/comparison_grid.png)

The comparison grid displays the binary edge maps produced by Sobel, Canny, LoG, and DoG for the clean image. It provides a direct visual comparison of the boundaries detected by each method.

### 11.2 Noise-Robustness Plot

![File: `results/noise_robustness_plot.png`](results/noise_robustness_plot.png)

The plot shows the percentage change in edge density against Gaussian noise sigma for all four methods. It helps visualize how the measured edge density changes as noise increases.

### 11.3 Individual Edge Maps

The program saves four separate files:

- `edges_sobel.png`
- `edges_canny.png`
- `edges_log.png`
- `edges_dog.png`

### 11.4 Noisy Images

The program also saves noisy versions of the input image for sigma values 5, 15, 25, and 40.

Together, these outputs provide both visual and numerical evidence of the differences between the methods.

## 12. Discussion

The experiment demonstrates that different edge detection algorithms respond differently to increasing Gaussian noise.

Sobel calculates gradient magnitude and is affected by intensity variations introduced by noise. In this experiment, its edge density increased sharply at sigma 40.

Canny remained comparatively stable at lower noise levels. Its Gaussian smoothing and thresholding stages help suppress some unwanted responses, although its edge density also increased at the highest tested noise level.

LoG exhibited a relatively small change at lower noise levels, followed by a substantial increase at sigma 40. This indicates that smoothing does not eliminate the effects of strong noise completely.

DoG produced relatively stable edge-density measurements throughout the experiment. However, this stability should not be interpreted as proof that every detected edge was correct or that all genuine edges were preserved.

The experiment also illustrates an important limitation of edge density: it measures the proportion of pixels classified as edges, not the correctness of those detections. Different thresholds and output characteristics can influence the measured values.

Therefore, the findings should be interpreted as a comparison of the behaviour of these implementations under the selected experimental conditions rather than a universal ranking of edge detection algorithms.

## 13. Limitations

The project has the following limitations:

1. The experiment uses one synthetic image rather than a large collection of real-world images.
2. Edge density does not directly measure detection accuracy.
3. The results depend on the selected parameters and thresholding procedure.
4. The detectors produce different types of edge responses, which can affect comparison.
5. Runtime measurements depend on the system and software environment.
6. Only Gaussian noise is investigated.
7. The project does not compare classical methods with deep-learning-based edge detectors.
8. The Sobel implementation prioritizes clarity over computational optimization.

## 14. Applications

Edge detection is useful in several Computer Vision applications, including:

- Image segmentation.
- Object boundary detection.
- Shape recognition.
- Industrial inspection.
- Medical image processing.
- Document analysis.
- Road and lane detection.
- Feature extraction.
- Object detection systems.

For example, edge detection can help identify boundaries and defects in manufactured components or separate objects from their backgrounds.

## 15. Future Scope

The project can be extended in several ways.

### 15.1 Real-World Image Dataset

Multiple photographs and images with different textures, lighting conditions, and contrasts can be used to improve the breadth of the experiment.

### 15.2 Ground-Truth Evaluation

Labelled edge maps can be used to calculate precision, recall, and F1-score. These metrics would provide a more meaningful assessment of edge detection accuracy.

### 15.3 Parameter Optimization

The program can be extended to accept configurable Gaussian kernel sizes, thresholds, and smoothing parameters.

### 15.4 Additional Edge Detectors

Other methods, including Prewitt, Roberts, and Scharr, can be added to the comparison.

### 15.5 Additional Noise Models

Salt-and-pepper noise and other noise types can be tested to study how different noise characteristics affect the algorithms.

### 15.6 Performance Optimization

The manual Sobel implementation can be optimized to improve execution speed while retaining its educational value.

### 15.7 Learning-Based Edge Detection

Classical methods can be compared with modern learning-based approaches using suitable datasets and evaluation metrics.

## 16. Conclusion

This project successfully implements and compares four classical edge detection methods: Sobel, Canny, Laplacian of Gaussian, and Difference of Gaussians.

The Python application generates a synthetic input image, introduces Gaussian noise at different levels, applies all four detectors, measures runtime and edge density, and produces visual and numerical outputs.

In the experiment, Sobel and LoG showed substantial increases in edge density at the highest noise level. Canny exhibited comparatively small changes at lower noise levels, while DoG maintained relatively stable edge-density measurements.

The findings demonstrate that the behaviour of an edge detector depends on the algorithm, image characteristics, noise level, and parameter settings. They also show that edge density alone is insufficient to determine detection accuracy.

Overall, the project connects theoretical Computer Vision concepts with a practical, executable experiment and provides a foundation for further study of edge detection and image-noise robustness.

## 17. References

1. Gonzalez, R. C., and Woods, R. E., *Digital Image Processing*, Pearson.
2. Canny, J., "A Computational Approach to Edge Detection," *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
3. OpenCV Documentation, Image Processing and Edge Detection.
4. NumPy Documentation, Numerical Computing with Python.
5. Matplotlib Documentation, Data Visualization and Plotting.
