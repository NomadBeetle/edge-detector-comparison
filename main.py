
import argparse
import csv
import time
from pathlib import Path

import cv2
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from edge_detectors import (
    sobel_detector,
    canny_detector,
    log_detector,
    dog_detector,
)


DETECTORS = {
    "Sobel": sobel_detector,
    "Canny": canny_detector,
    "LoG": log_detector,
    "DoG": dog_detector,
}


def add_gaussian_noise(image, sigma, rng):
    """Add Gaussian noise to a grayscale image."""

    noise = rng.normal(0, sigma, image.shape)
    noisy = image.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def make_binary(edge_image):
    """Convert an edge-strength image into a binary edge map."""

    _, binary = cv2.threshold(
        edge_image, 50, 255, cv2.THRESH_BINARY
    )
    return binary


def edge_density(edge_image):
    """Calculate the fraction of pixels classified as edges."""

    return float(np.count_nonzero(edge_image) / edge_image.size)


def save_comparison(edge_maps, output_dir):
    """Save a comparison grid of all four edge detectors."""

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    for ax, (name, edge_image) in zip(
        axes.ravel(), edge_maps.items()
    ):
        ax.imshow(edge_image, cmap="gray", vmin=0, vmax=255)
        ax.set_title(name)
        ax.axis("off")

    fig.suptitle("Edge Detector Comparison")
    fig.tight_layout()
    fig.savefig(
        output_dir / "comparison_grid.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)


def save_robustness_plot(rows, output_dir):
    """Plot percentage change in edge density against noise."""

    fig, ax = plt.subplots(figsize=(9, 5))

    for method in DETECTORS:
        method_rows = [
            row for row in rows if row["method"] == method
        ]
        method_rows.sort(key=lambda row: row["noise_sigma"])

        x = [row["noise_sigma"] for row in method_rows]
        y = [
            row["density_change_percent"]
            for row in method_rows
        ]

        ax.plot(x, y, marker="o", label=method)

    ax.set_title("Noise Robustness of Edge Detectors")
    ax.set_xlabel("Gaussian Noise Sigma")
    ax.set_ylabel("Change in Edge Density (%)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    fig.savefig(
        output_dir / "noise_robustness_plot.png",
        dpi=150,
    )
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(
        description="Compare four edge detection methods."
    )

    parser.add_argument(
        "--image",
        default="sample_images/synthetic_test.png",
        help="Path to the input image",
    )

    parser.add_argument(
        "--output",
        default="results",
        help="Directory for generated results",
    )

    parser.add_argument(
        "--noise_levels",
        default="0,5,15,25,40",
        help="Comma-separated Gaussian noise sigma values",
    )

    args = parser.parse_args()

    image_path = Path(args.image)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise SystemExit(
            f"Could not load image: {image_path}\n"
            "Check that the file exists and is a valid image."
        )

    try:
        noise_levels = [
            float(value.strip())
            for value in args.noise_levels.split(",")
        ]

        if not noise_levels:
            raise ValueError("No noise levels supplied.")

        if any(
            not np.isfinite(sigma) or sigma < 0
            for sigma in noise_levels
        ):
            raise ValueError(
                "Noise levels must be finite and non-negative."
            )

    except ValueError as error:
        raise SystemExit(f"Invalid noise levels: {error}")

    if len(set(noise_levels)) != len(noise_levels):
        raise SystemExit("Noise levels must not contain duplicates.")

    if 0 not in noise_levels:
        raise SystemExit(
            "Include noise level 0 to calculate the clean baseline."
        )

    rng = np.random.default_rng(42)
    results = []
    baseline_densities = {}
    clean_edge_maps = {}

    print(f"Input image: {image_path}")
    print(f"Image dimensions: {image.shape[1]} x {image.shape[0]}")
    print(f"Noise levels: {noise_levels}")

    for sigma in noise_levels:
        noisy_image = add_gaussian_noise(image, sigma, rng)

        if sigma != 0:
            cv2.imwrite(
                str(output_dir / f"noisy_sigma_{sigma:g}.png"),
                noisy_image,
            )

        print(f"\nProcessing noise sigma = {sigma:g}")

        for method, detector in DETECTORS.items():
            start = time.perf_counter()

            edge_image = detector(noisy_image)
            binary_edges = make_binary(edge_image)

            elapsed_ms = (time.perf_counter() - start) * 1000
            density = edge_density(binary_edges)

            if sigma == 0:
                baseline_densities[method] = density
                clean_edge_maps[method] = binary_edges.copy()

            baseline = baseline_densities[method]

            if baseline > 0:
                change = ((density - baseline) / baseline) * 100
            else:
                change = 0.0

            results.append({
                "noise_sigma": sigma,
                "method": method,
                "runtime_ms": elapsed_ms,
                "edge_density": density,
                "density_change_percent": change,
            })

            print(
                f"  {method:6s} | "
                f"Runtime: {elapsed_ms:8.2f} ms | "
                f"Density: {density:.4f} | "
                f"Change: {change:.2f}%"
            )

            if sigma == 0:
                cv2.imwrite(
                    str(output_dir / f"edges_{method.lower()}.png"),
                    binary_edges,
                )

    csv_path = output_dir / "noise_experiment.csv"

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "noise_sigma",
                "method",
                "runtime_ms",
                "edge_density",
                "density_change_percent",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    save_comparison(clean_edge_maps, output_dir)
    save_robustness_plot(results, output_dir)

    print("\nExperiment completed successfully!")
    print(f"Results saved in: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
