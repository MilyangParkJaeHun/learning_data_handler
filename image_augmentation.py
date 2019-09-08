import os
import sys
import image_converter

from multiprocessing import Process

def augmentation(input_image_dir, origin_path, origin_csv, augmentation_list):
  origin_data = os.path.join(origin_path, origin_csv)
  data = []
  with open(origin_data, "r") as f:
    f.readline()
    while True:
      line = f.readline()
      if not line:
        break
      line = line[:-1].split(",")
      data.append(line)

  augmentation_csv_file = os.path.join(origin_path, "augmentation_"+origin_csv)
  header = "filename,width,height,class,xmin,ymin,xmax,ymax\n"
  with open(augmentation_csv_file, "w") as f:
    f.write(header)
    for bbox_info in data:
      origin_line = ",".join(bbox_info) + "\n"
      f.write(origin_line)
      for option in augmentation_list.keys():
        for value in augmentation_list[option]:
          image_name = bbox_info[0].split("/")[-1]
          image_path = bbox_info[0][:-len(image_name)-1]
          bbox_info[0] = os.path.join(image_path,option+str(value),image_name)
          converted_line = ",".join(bbox_info)+"\n"
          f.write(converted_line) 

  data_size = len(data)
  process_count = 10

  procs = []
  split_data = []
  for i in range(process_count-1):
    split_data.append(data[int(data_size/process_count)*i:int(data_size/process_count)*(i+1)])
  split_data.append(data[int(data_size/process_count)*(process_count-1):])

  progress_flag = False
  for i in range(process_count):
    if i == process_count-1:
      progress_flag = True
    proc = Process(target=image_converter.convert, args=(progress_flag, split_data[i], input_image_dir, augmentation_list))
    procs.append(proc)
    proc.start()

  for proc in procs:
    proc.join()
