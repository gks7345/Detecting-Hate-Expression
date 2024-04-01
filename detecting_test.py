import cv2
from ultralytics import YOLO

model = YOLO("models\Hate_Expression.pt")

# # # test = model.predict("data_sets\\train\images\\11_4.jpg") #0.92
# test = model.predict("data_sets\\test\images\\143.jpg", conf = 0.75) #weight >=0.75
test = model.predict("data_sets\\test\images\\143.jpg")
img = cv2.imread("data_sets\\test\images\\143.jpg")
# print(test[0])
# print('boxes')
print(test[0].boxes)
print()
# print(test[0].boxes.conf)
res_plotted = test[0].plot()
cv2.imshow('0',res_plotted)
cv2.imshow('1',img)
cv2.waitKey(0)
# print(model.names)

#=========video==================================================================
'''cap = cv2.VideoCapture("video.mp4")
#재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output1.avi', fourcc, 30.0, (int(width), int(height)))
while True:
    ret, frame = cap.read()

    if ret == False:
        break
    
    result = model.predict(frame)
    res_plotted = result[0].plot()
    out.write(res_plotted)
    cv2.imshow('0',res_plotted)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()'''