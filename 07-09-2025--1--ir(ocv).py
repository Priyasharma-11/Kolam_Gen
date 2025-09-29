import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_symmetry(image_path, thresh_val=128):
    # Load and preprocess image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, img_bin = cv2.threshold(img, thresh_val, 255, cv2.THRESH_BINARY_INV)

    # Resize for easier computation
    img_bin = cv2.resize(img_bin, (256, 256))

    # Horizontal Flip
    h_flip = cv2.flip(img_bin, 1)
    # Vertical Flip
    v_flip = cv2.flip(img_bin, 0)

    # Symmetry Scores (mean similarity)
    hor_score = np.mean(img_bin == h_flip)
    ver_score = np.mean(img_bin == v_flip)

    print(f"Horizontal Symmetry: {hor_score:.2f}")
    print(f"Vertical Symmetry: {ver_score:.2f}")

    # Display
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(img_bin, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.title("H-Flip")
    plt.imshow(h_flip, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title("V-Flip")
    plt.imshow(v_flip, cmap='gray')
    plt.show()

    # Classification
    if hor_score > 0.85 and ver_score > 0.85:
        pattern_type = "Highly Symmetrical (Horizontal+Vertical)"
    elif hor_score > 0.85:
        pattern_type = "Horizontal Symmetry"
    elif ver_score > 0.85:
        pattern_type = "Vertical Symmetry"
    else:
        pattern_type = "Asymmetrical or Complex"

    print(f"Predicted Pattern Type: {pattern_type}")
    return pattern_type


# Example usage
image_path = "your_kolam_image.jpg"
detect_symmetry(image_path)
