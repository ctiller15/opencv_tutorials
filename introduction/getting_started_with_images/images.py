import cv2 as cv
import sys

def main():
    img = cv.imread("../../sample_files/starry_night.jpg")

    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)
    k = cv.waitKey(0)

    if k == ord("s"):
        print("Saving starry night image as png")
        cv.imwrite("starry_night.png", img)
    else:
        print("Exiting program.")

if __name__ == '__main__':
    main()