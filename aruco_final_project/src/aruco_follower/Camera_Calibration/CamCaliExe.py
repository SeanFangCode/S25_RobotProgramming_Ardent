#!/usr/bin/env python3

import cv2
import numpy as np
import os
import glob

# Checkerboard dimensions
CHECKERBOARD = (7, 4)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Directory to save captured images
capture_dir = "calibration_images"
os.makedirs(capture_dir, exist_ok=True)

# Capture images function
def capture_images():
    cam = cv2.VideoCapture(0)  # Adjust camera index if needed
    image_counter = 0

    print("Press 's' to save an image, or 'q' to quit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture image.")
            break

        cv2.imshow("Capture", frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            filename = os.path.join(capture_dir, f"calibration_image_{image_counter}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            image_counter += 1
        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Calibration function
def calibrate_camera():
    objpoints = []  # 3D points in real-world space
    imgpoints = []  # 2D points in image plane
    
    # Prepare object points
    objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    
    image_size = None
    images = glob.glob(os.path.join(capture_dir, "*.jpg"))
    
    # Check if images are found in the directory
    if not images:
        print(f"No images found in {capture_dir}. Make sure images are saved correctly.")
        return

    for fname in images:
        if not os.path.exists(fname):
            print(f"File not found: {fname}")
            continue

        print(f"Processing {fname}...")  # Print the file path for verification
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if image_size is None:
            image_size = gray.shape[::-1]  # (width, height)

        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
            cv2.imshow("Corners", img)
            cv2.waitKey(500)
        else:
            print(f"Checkerboard not detected in {fname}")
    
    cv2.destroyAllWindows()

    # Perform calibration if valid points were found
    if objpoints and imgpoints:
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, image_size, None, None)
        print("Camera matrix (K):\n", mtx)
        print("Distortion coefficients:\n", dist)
    else:
        print("No valid checkerboard images were detected. Please capture images with a clearer view of the checkerboard.")

# Run the capture function first
if __name__ == "__main__":
    capture_images()

    # Then run the calibration function
    calibrate_camera()

