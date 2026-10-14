
# Edge Detector Comparison and Analysis Tool

## Overview

This project compares four classical edge detection methods:
Sobel, Canny, Laplacian of Gaussian (LoG), and Difference
of Gaussians (DoG).

It also investigates how Gaussian noise affects their
outputs by measuring edge density and execution time.

## Technologies

- Python
- NumPy
- OpenCV
- Matplotlib

## Project Structure

```text
EdgeDetectorProject/
├── sample_images/
├── results/
├── main.py
├── edge_detectors.py
├── create_sample.py
├── requirements.txt
├── README.md
└── REPORT.md
```

## Setup

Create and activate a virtual environment, then install
the dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Generate the sample image:

```bash
python create_sample.py
```

Run the experiment:

```bash
python main.py --image sample_images/synthetic_test.png --output results
```

## Experimental Setup

The experiment uses Gaussian noise sigma values of
0, 5, 15, 25 and 40.

The program records runtime, edge density and percentage
change in edge density relative to the clean image.

## Outputs

- Individual edge maps for all four methods
- Comparison grid
- CSV experimental measurements
- Noise robustness plot
- Generated noisy images

## Limitations

Edge density does not directly measure detection accuracy.
The experiment uses a synthetic image and a limited range
of noise levels. Results depend on the image and the
implementation parameters.

## Future Improvements

- Test multiple real-world images.
- Evaluate results using ground-truth edge maps.
- Add more edge detection algorithms.
- Compare additional types of image noise.
- Improve parameter selection and runtime efficiency.
