import time
import os
import bar.progressbar as pb
import image_convert_functions
import cv2

def chk_dir(path):
  try:
    if not(os.path.isdir(path)):
      os.makedirs(os.path.join(path))
  except OSError as e:
    if e.errno != errno.EEXIST:
      print('failed to create directory')
      raise

def convert(progress_flag, data, input_image_dir, augmentation_list):
  progressbar = pb.Progressbar(len(data), 'augmentation Progress:', 'Complete', 2, 50, 0.1)
  
  for i in range(len(data)):
    if progress_flag:
      progressbar.progress()
    image_name = data[i][0].split("/")[-1]
    image_path = data[i][0][:-len(image_name)-1]
    image_file = os.path.join(input_image_dir,data[i][0])
    image = cv2.imread(image_file)
    converter = image_convert_functions.functions()
    for option in augmentation_list.keys():
      for value in augmentation_list[option]:
        output_path = os.path.join(input_image_dir, image_path, option+str(value))

        chk_dir(output_path)
        output_image = os.path.join(output_path, image_name)
        if os.path.isfile(output_image):
          continue

        converted_image = converter[option](image, float(value) if option!="flip" else value)
        cv2.imwrite(output_image, converted_image)
