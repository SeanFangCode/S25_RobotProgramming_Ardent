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

def capture_images():
    cam = cv2.VideoCapture(0)
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

def calibrate_camera():
    objpoints = []
    imgpoints = []
    
    objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    
    image_size = None
    images = glob.glob(os.path.join(capture_dir, "*.jpg"))
    
    if not images:
        print(f"No images found in {capture_dir}")
        return None, None

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if image_size is None:
            image_size = gray.shape[::-1]

        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)
        if ret:
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            objpoints.append(objp)
            imgpoints.append(corners2)
            img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
            cv2.imshow("Corners", img)
            cv2.waitKey(500)
    
    cv2.destroyAllWindows()

    if objpoints and imgpoints:
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, image_size, None, None)
        return mtx, dist
    return None, None

def main():
    capture_images()
    mtx, dist = calibrate_camera()
    
    print("\n\n=== Calibration Results ===")
    if mtx is not None:
        print("\nCamera Matrix (K):")
        print(np.array2string(mtx, separator=', ', formatter={'float_kind': lambda x: "%.6f" % x}))
        
        print("\nDistortion Coefficients (k1, k2, p1, p2, k3):")
        print(np.array2string(dist.ravel(), separator=', ', formatter={'float_kind': lambda x: "%.6f" % x}))
    else:
        print("\nCalibration failed - could not calculate camera parameters")

if __name__ == "__main__":
    main()