import os
import cv2
import numpy as np
import bar.progressbar as pb

def convert(input_image_dir, input_image_path, labeled_txt_path, origin_path, origin_csv, file_open_format):
  origin_csv_file_path = os.path.join(origin_path, origin_csv)
  exist = os.path.exists(origin_csv_file_path)

  with open(origin_csv_file_path, file_open_format) as f:
    if exist == False or file_open_format=="w":
      header = "filename,width,height,class,xmin,ymin,xmax,ymax\n"
      f.write(header)

    txt_list = os.listdir(labeled_txt_path)
    txt_list.sort()
    progressbar = pb.Progressbar(len(txt_list), 'fiji to csv Progress:', 'Complete', 2, 50, 0.1)

    for txt_file in txt_list:
      progressbar.progress()
      jpg_image_name = txt_file.split('.')[0]+'.jpg'
      jpg_image_file = os.path.join(input_image_dir, input_image_path, image_name)
      
      png_image_name = txt_file.split('.')[0]+'.png'
      png_image_file = os.path.join(input_image_dir, input_image_path, image_name)
      
      if os.path.isfile(jpg_image_file):
        image_file = jpg_image_file
      elif os.path.isfile(png_image_file):
        image_file = png_image_file
      else:
        print("Can not find image file")
        return
      
      image = cv2.imread(image_file)
      width = image.shape[1]
      height = image.shape[0]

      with open(os.path.join(labeled_txt_path, txt_file), "r") as bboxs:
        bbox_info = []
        while True:
          bbox = bboxs.readline()
          if not bbox:
            break
          bbox_info.append(bbox[:-1].split(" "))
      for bbox in bbox_info:
        f.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % \
          (os.path.join(input_image_path, image_name), str(width), str(height), \
          'b'+bbox[0], bbox[4], bbox[5], bbox[6], bbox[7]))
