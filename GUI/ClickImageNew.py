from cv2 import *

def capture_image():
    cam_port = 0
    cam = VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image is detected without any error, show result
    if result:
        imshow("DemoPic", image)

        # saving image in local storage
        imwrite("DemoPic.png", image)

        # Wait for keyboard interrupt, then destroy image window
        waitKey(0)
        destroyWindow("DemoPic")

    # If captured image is corrupted, print error message
    else:
        print("No image detected. Please try again.")

