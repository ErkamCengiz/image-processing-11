import cv2

kamera=cv2.VideoCapture('smile.mp4')#0 pcdeki kamera usb felan kullanarak camera bağlamışsa 1 direk video dosyası alıyosakta yazdığımız gibi



while True:
    ret, goruntu=kamera.read() # ret return oluyor kameradan görüntü alındı mı alınmadı mı
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Goruntu',goruntu)
    cv2.imshow('Gri Ton', griton)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()