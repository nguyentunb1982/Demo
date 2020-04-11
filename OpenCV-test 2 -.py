import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#tạo ra đối tượng face_cascade để xử lý quán trình nhận diện khuôn mặt bên dưới
 
image = cv2.imread('hung.jpg')#nhập vào hình ảnh và biến nó thành mảng số
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#chuyển thành ảnh xám
#image[150:255,150:255]=[255,255,255]
#pn = image[450:455,150:255]
#cv2.imshow('hinh anh tu chon', pn)
faces = face_cascade.detectMultiScale(grayImage)#phương thức detectMultiScale sẽ trả về các khuôn mặt phát hiện được dưới dạng các hình chữ nhật để phía dưới sẽ đánh dấu bằng cách vẽ đường bao quanh

print (faces.shape)#in ra (N hàng, 4 cột) với N là số khuôn mặt còn 4 cột là 4 kích thước của hình chữ nhật
print (faces) #in ra ma trận số ảnh = số hàng và kích thước và vị trí của ảnh cạnh ứng với 1 ảnh gồm tọa độ (x,y) và kích thước ảnh (w,h)
print (image.shape[1])#in ra chiều rộng của bức ảnh
print (image.shape[0])#in ra chiều cao của bức ảnh
if len(faces) == 0:
    print ('khong co mat nao')
else:

    for (x,y,w,h) in faces:
       cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)#vẽ hình chữ nhật trên đối tượng có vị trí (x,y) với các kích thước (w,h)
       
    cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    #in ra dòng chú thích là số khuôn mặt dò ra là: faces.shape[0]
    cv2.imshow('Image with faces',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
