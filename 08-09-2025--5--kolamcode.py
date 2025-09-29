import cv2
import numpy as np


def rotational_symmetry(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    img_bin = cv2.resize(img_bin, (256, 256))

    def similarity_score(a, b):
        return np.mean(a == b)

    rot_90 = np.rot90(img_bin)
    rot_180 = np.rot90(img_bin, 2)
    rot_270 = np.rot90(img_bin, 3)

    score_90 = similarity_score(img_bin, rot_90)
    score_180 = similarity_score(img_bin, rot_180)
    score_270 = similarity_score(img_bin, rot_270)

    print(f"90° Rotation Similarity: {score_90:.2f}")
    print(f"180° Rotation Similarity: {score_180:.2f}")
    print(f"270° Rotation Similarity: {score_270:.2f}")


# Example usage
rotational_symmetry("your_kolam_image.jpg")
