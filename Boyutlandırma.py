import cv2

kamera=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0 pcdeki kamera usb felan kullanarak camera bağlamışsa 1 direk video dosyası alıyosakta yazdığımız gibi

##kamera.set(cv2.CAP_PROP_FRAME_WIDTH,1920) ya böyle
##kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,1080) bbu şekil

while True:
    ret, goruntu = kamera.read() #goruntu alınıp alınamadığını
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    ret=kamera.set(3,320) #yada bu şekilde
    ret=kamera.set(4,320) # bu şekil
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Goruntu', griton)
    if cv2.waitKey(25) & 0xFF == ord('q'): #qya basınca kapanıyor
        break

kamera.release()
cv2.destroyAllWindows()