import cv2
import numpy as np

imgfile = '1.jpg'
refPt = []
cropping = False

image = cv2.imread(imgfile)
(h, w, _) = image.shape
mask = np.zeros((h, w), np.uint8) * 255

scale = w / 1000
w2, h2 = (1000, int(h/scale))
image2 = cv2.resize(image, (w2, h2), cv2.INTER_AREA)
clone = image2.copy()

cv2.namedWindow("image")
cv2.imshow("image", image2)
bb = cv2.selectROI("image", image2, fromCenter=False, showCrosshair=True)
refPt.append((bb[0], bb[1]))
refPt.append((bb[0]+bb[2], bb[1]+bb[3]))
cv2.destroyAllWindows()

srcvideo = imgfile # './test/IMG_4027.mp4'
cap = cv2.VideoCapture(srcvideo)
if not cap.isOpened():
    print("ERROR: Cannot open VideoCapture")
    exit()

if len(refPt) == 2:
    pos = [(int(refPt[0][0]*scale), int(refPt[0][1]*scale))]
    pos.append((int(refPt[1][0]*scale), int(refPt[1][1]*scale)))
    logo_img = image[pos[0][1]:pos[1][1], pos[0][0]:pos[1][0]]
    #cv2.imwrite('logo_img.bmp', logo_img)
    logo_gray = cv2.cvtColor(logo_img, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('logo_gray.bmp', logo_gray)
    logo_binary = cv2.threshold(logo_gray, 128, 255, cv2.THRESH_BINARY)[1]
    #cv2.imwrite('logo_binary.bmp', logo_binary)
    mask[pos[0][1]:pos[1][1], pos[0][0]:pos[1][0]] = 255 #logo_binary
    #cv2.imwrite('mask.bmp', mask)
    frame_num = 0
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        dst = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)
        outfile = 'out_' + str(frame_num) + '.bmp'
        cv2.imwrite(outfile, dst)
        frame_num += 1

print('done')