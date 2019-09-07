import os
import cv2
import numpy as np

output = "/media/park/ParkJH/learning_data/csv/origin.csv"

def bound(width, height, xmin, ymin, xmax, ymax):
  return int(xmin)>=0 and int(ymin)>=0 and int(xmax)<=int(width) and int(ymax)<=int(height)

def left_cal(width, height, xmin, ymin, xmax, ymax, ratio):
  ymin = int((1+ratio)*ymin-height*ratio)
  ymax = int((1+ratio)*ymax-height*ratio)
  xmin = int((1+ratio)*xmin)
  xmax = int((1+ratio)*xmax)
  return (str(int(width)), str(int(height)), str(xmin), str(ymin), str(xmax), str(ymax))

def right_cal(width, height, xmin, ymin, xmax, ymax, ratio): 
  ymin = int((1+ratio)*ymin-height*ratio)
  ymax = int((1+ratio)*ymax-height*ratio)
  xmin = int((1+ratio)*xmin-width*ratio)
  xmax = int((1+ratio)*xmax-width*ratio)
  return (str(int(width)), str(int(height)), str(xmin), str(ymin), str(xmax), str(ymax))


filename="/media/park/ParkJH/learning_data/csv/parsing_result.csv"
with open(filename,"r") as f:
	data = []
	f.readline()
	while True:
		line = f.readline()
		if not line:
			break
		data.append(line[:-1].split(","))
with open(output,"a") as f:
	#f.write('filename,width,height,class,xmin,ymin,xmax,ymax\n')
	#for i in range(len(data)):
#		(filename, width, height, class_name, xmin, ymin, xmax, ymax) = [content for content in data[i]]
#		f.write('origin/'+filename+','+width+','+height+','+class_name+','+xmin+','+ymin+','+xmax+','+ymax+'\n')
		#left
#		(w,h,xn,yn,xx,yx) = left_cal(float(width), float(height), float(xmin), float(ymin), float(xmax), float(ymax), 0.3)
#		if(bound(w,h,xn,yn,xx,yx)):
#			f.write('left_image/'+filename+','+w+','+h+','+class_name+','+xn+','+yn+','+xx+','+yx+'\n')
		#right
#		(w,h,xn,yn,xx,yx) = right_cal(float(width), float(height), float(xmin), float(ymin), float(xmax), float(ymax), 0.3)
#		if(bound(w,h,xn,yn,xx,yx)):
#			f.write('right_image/'+filename+','+w+','+h+','+class_name+','+xn+','+yn+','+xx+','+yx+'\n')

	name_list = ['busan0']
	input_path = "/media/park/ParkJH/learning_data/txt/"
	img_path = "/media/park/ParkJH/learning_data/images/"
	for name in name_list:
		file_list = os.listdir(input_path+name)
		img_name = file_list[0].split('.')[0]+'.jpg'
		img = cv2.imread(img_path+name+"/"+img_name)
		width = img.shape[1]
		height = img.shape[0]
		print(name , ' : ',width, ',', height)
		for filename in file_list:
			with open(input_path+name+"/"+filename,"r") as textfile:
				text_data = []
				while True:
					line = textfile.readline()
					if not line:
						break
					text_data.append(line[:-1].split(" "))
				for text in text_data:
					f.write(name+'/'+filename.split('.')[0]+'.jpg,'+str(width)+','+str(height)+',b'+text[0]+','+text[4]+','+text[5]+','+text[6]+','+text[7]+'\n')
	
