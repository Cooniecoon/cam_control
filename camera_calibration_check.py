import numpy as np
import cv2


def cali(source):
    rms = 0.160635
    fx = 638.999828
    fy = 638.999828
    cx = 320.000000
    cy = 240.000000
    k1 = 0.058642
    k2 = -0.191958
    p1 = -0.000912
    p2 = 0.002935

    hfov = 53.2  # deg
    vfov = 41.2  # deg
    # copy parameters to arrays
    # A (Intrinsic Parameters) [fc, skew*fx, cx], [0, fy, cy], [0, 0, 1]
    K = np.array([[fx, 0.0, cx], [0, fy, cy], [0, 0, 1]])

    # Distortion Coefficients(kc) - 1st, 2nd
    d = np.array([k1, k2, p1, p2, 0])  # just use first two terms

    image = source
    img = cv2.resize(
        image,
        (640, 480),
    )
    h, w = img.shape[:2]

    # undistort
    newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w, h), 0)
    newimg = cv2.undistort(img, K, d, None, newcamera)
    img = cv2.resize(newimg, (640, 480))

    return img


source = cv2.imread("./image/image_29.jpg")
img = cali(source)


cv2.imshow("img", source)
cv2.imshow("new_img", img)
cv2.waitKey()
cv2.destroyAllWindows()
