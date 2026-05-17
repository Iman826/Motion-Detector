import cv2

# ---- Yahan se change karo: file ya camera ----
SOURCE = "cross.mp4"       # file ke liye
# SOURCE = 0               # camera ke liye — bas yeh uncomment karo
# ----------------------------------------------

cap = cv2.VideoCapture(SOURCE)

if not cap.isOpened():
    print("Error: source open nahi hua — path check karo")
    exit()

# history kam karo taake jaldi seekhe background
mog = cv2.createBackgroundSubtractorMOG2(
    history=100,          # pehle 500 tha — ab jaldi warm up hoga
    varThreshold=40,
    detectShadows=True
)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# ---- Warmup: pehle 30 frames background seekhne do ----
print("Background seekh raha hai...")
for _ in range(30):
    ret, frame = cap.read()
    if not ret:
        # video chhoti hai toh wapas shuru se
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    mog.apply(gray)

# wapas shuru se play karo
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
print("Ready! Motion detection shuru...")
# -------------------------------------------------------

while True:
    ret, frame = cap.read()

    if not ret:
        # video file loop karo
        if isinstance(SOURCE, str):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    fgmask = mog.apply(gray)

    # shadow (127) hatao
    _, fgmask = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    contours, _ = cv2.findContours(
        fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < 500:   # 1000 se kam kiya — sensitive
            continue

        motion_detected = True
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Motion!", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    status = "MOTION DETECTED" if motion_detected else "No Motion"
    color  = (0, 0, 255) if motion_detected else (0, 255, 0)
    cv2.putText(frame, status, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Mask", fgmask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()