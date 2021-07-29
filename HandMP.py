import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#defining camera numpy dimensions
success, img = cap.read()
h, w, c = img.shape

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(abs(lm.z*40)) #correct x, correcty, correct depth(to avoid enormous circles whene the hand if far and viceversa
                cv2.circle(img, (cx, cy), cz, (255, 255, 255), cv2.FILLED)
                # print(id, lm)
                #print(id, cx, cy)
                if id == 4:
                    cv2.putText(img,"Hand Raised",(10,35),cv2.QT_FONT_NORMAL,1.5,(0,0,120),2)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 113:
      break

cv2.destroyAllWindows()
cap.release()

