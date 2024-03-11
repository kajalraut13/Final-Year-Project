from pyexpat import model
from tkinter import Frame
import cv2
from flask import request
from matplotlib.patches import Polygon
from sklearn.preprocessing import scale
from playsound import playsound
import pyttsx3
import mysql.connector
engine = pyttsx3.init()
import numpy as np
import datetime

net =cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255)


#load class lists
classes=[]
with open("dnn_model/classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
    #print("Object list")
    #print(classes)

#initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)


while True:
    
    ret,frame= cap.read()
    
    #object Detection 
    (class_ids,scores,bboxes)=model.detect(frame)
    for class_id,score,bbox in zip(class_ids,scores,bboxes):
        x,y,w,h =bbox
        #print("class id",class_id[0])
        #id11=class_id[0]
        class_name = classes[class_id]
        cv2.putText(frame,class_name,(x,y-10),cv2.FONT_HERSHEY_PLAIN,2,(200,0,50),2)
        cv2.rectangle(frame,(x,y),(x + w,y + h),(200,0,50,),3)
    
        if class_name:
          time_date = datetime.datetime.now()
          print (time_date.strftime("Current date and time : %H:%M %d-%M-%Y"))
          my_connect = mysql.connector.connect(
                   host="localhost",
                   user="root", 
                   passwd="root",
                   database="detection"
              # )
         # my_conn = my_connect.cursor()

          #try:
        
           # my_conn.execute("insert into object values('%s','%s');"%(class_name,time_date))
           # my_connect.commit()
            
         # except:
              #print("not insreted ")
          
          

        #else:
            #print("not done")


        
        #object is detected so print the object name 
        if(class_name):
           print("Object Name:-",class_name)
           engine.say("this is a"+class_name)


           engine.runAndWait() 
        #object is hot detecetd 
        elif(class_name):
            print("object is not detected")

        else:
            print("________________")
    
    cv2.imshow("Object Detection",frame)
    cv2.waitKey(1)
