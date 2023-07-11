import cv2
import imutils

arquivo_reconhecimento = cv2.HOGDescriptor()
arquivo_reconhecimento.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

figura = cv2.imread('people.jpg')
fugura = imutils.resize(figura, width=min(400, figura.shape[1])) # para diminuir o tamanho

(dimensao, _) = arquivo_reconhecimento.detectMultiScale(figura, winStride=(4,4), padding=(4,4),
                                                        scale=1.05)

for (x, y, w, h) in dimensao:
    cv2.rectangle(figura,(x, y), (x+w, y+h), (0, 0, 255), 2) # padrão
cv2.imshow('Detected', figura)
cv2.waitKey(0)
cv2.destroyAllWindows()
