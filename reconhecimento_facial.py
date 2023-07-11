import cv2
import imutils

arquivo_reconhecimento = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
figura = cv2.imread('river_keanu.jpg')
fugura = imutils.resize(figura, width=min(400, figura.shape[1])) # para diminuir o tamanho

dimensao = arquivo_reconhecimento.detectMultiScale(figura)

for (x, y, w, h) in dimensao:
    cv2.rectangle(figura,(x, y), (x+w, y+h), (0, 0, 255), 2) # padrão
cv2.imshow('Detected', figura)
cv2.waitKey(0)
cv2.destroyAllWindows()
