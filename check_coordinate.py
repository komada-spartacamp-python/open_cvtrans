import cv2

img = cv2.imread("images/man.png")

# # OpenCVをインポート
# import cv2


def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        return x, y


cv2.imshow("Face", img)
cv2.setMouseCallback("Face", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
# img = cv2.imread('images/man.png')

# # 画像を表示させる
# cv2.imshow('face', img)

# # クリックした際にonMouse関数が発火
# cv2.setMouseCallback('face', onMouse)

# # waitKey(0)で画像上で何かしらのキーを押せば閉じられるようにする
