import numpy as np
import cv2

def compute_affine(pixel_pts, ground_pts):
    pixel = np.array(pixel_pts, dtype=np.float32)
    ground = np.array(ground_pts, dtype=np.float32)
    matrix = cv2.getAffineTransform(pixel[:3], ground[:3])
    return matrix.tolist()

def compute_projective(pixel_pts, ground_pts):
    pixel = np.array(pixel_pts, dtype=np.float32)
    ground = np.array(ground_pts, dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(pixel, ground)
    return matrix.tolist()

def apply_affine(matrix, point):
    m = np.array(matrix)
    x, y = point
    res = m @ np.array([x, y, 1])
    return res[0], res[1]

def apply_projective(matrix, point):
    m = np.array(matrix)
    x, y = point
    vec = m @ np.array([x, y, 1])
    return vec[0]/vec[2], vec[1]/vec[2]
