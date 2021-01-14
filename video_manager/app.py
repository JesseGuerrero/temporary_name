import cv2

'''
Here is a potential project, a video manager for downloaded videos to act as a replacement for Netflix when you 
download videos.
'''


def isXButtonPressed():
    return cv2.getWindowProperty('VideoManager', 0) == -1

video = cv2.VideoCapture('Oklahoma.mp4')

# Read until video is completed
while (video.isOpened()):
    # Capture frame-by-frame
    frameSuccessful, frame = video.read()
    if frameSuccessful == True:
        # Display the resulting frame
        cv2.imshow('VideoManager', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if isXButtonPressed() is True:
            break
    else: #no more frames!
        break
video.release()

# Closes all the frames
cv2.destroyAllWindows()