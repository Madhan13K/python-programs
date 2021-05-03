# import player
# tim=player.Player("tim")
import cv2
cap=cv2.VideoCapture(0)
while True:
    first,set=cap.read()
    cv2.imshow("image",set)


