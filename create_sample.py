
import cv2
import numpy as np
from pathlib import Path

output_dir = Path("sample_images")
output_dir.mkdir(parents=True, exist_ok=True)

image = np.zeros((512, 512), dtype=np.uint8)

# Rectangle
cv2.rectangle(image, (40, 40), (210, 200), 220, -1)

# Circle
cv2.circle(image, (350, 130), 75, 150, -1)

# Triangle
triangle = np.array([
    [80, 420],
    [220, 260],
    [300, 420]
], dtype=np.int32)

cv2.fillPoly(image, [triangle], 255)

# Additional geometric details
cv2.line(image, (330, 280), (470, 430), 180, 8)
cv2.rectangle(image, (340, 330), (460, 450), 100, 4)

output_path = output_dir / "synthetic_test.png"

if cv2.imwrite(str(output_path), image):
    print(f"Sample image created: {output_path}")
else:
    raise SystemExit("Failed to save sample image.")
