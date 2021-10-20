import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

# from autopy.mouse import LEFT_BUTTON

wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7

pTime = 0
cTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    # Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # Working Area
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (0, 0, 255), 2)
    # Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    # Check which fingers are up
    fingers = detector.fingersUp()
    # print(fingers)
    # Only Index Finger : Moving Mode
    if len(fingers) != 0 and len(lmList) != 0:
        if frameR <= x1 <= wScr - frameR and frameR <= y1 <= hScr - frameR:
            if fingers[1] == 1 and fingers[2] == 0:
                # Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                # Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                plocX, plocY = clocX, clocY
            # Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
                # Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)
                print(length)
                # Click mouse if distance<=40
                if length <= 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (34, 139, 34), cv2.FILLED)
                    autopy.mouse.click()
            # LEFT_BUTTON_CLICK
            # if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            #     length1, img, lineInfo2 = detector.findDistance(8, 12, img)
            #     length2, img, lineInfo3 = detector.findDistance(12, 16, img)
            #     if length1 <= 40 and length2 <= 40:
            #         cv2.circle(img, (lineInfo2[2], lineInfo2[3]), 15, (0, 0, 0), cv2.FILLED)
            #         autopy.mouse.click(LEFT_BUTTON)

    # Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
