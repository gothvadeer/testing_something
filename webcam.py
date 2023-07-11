import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    conexao, frame = video.read()
    cv2.imshow('imagem', frame)
    if cv2.waitKey(1) == ord('f'):
        break

video.release()
cv2.destroyAllWindows()
