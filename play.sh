input_image_dir="/media/park/ParkJH/learning_data/images"
input_image_path="dmc"
labeled_txt_path="/media/park/ParkJH/learning_data/txt/dmc"
make_origin=0
origin_path="/media/park/ParkJH/learning_data/csv"
origin_csv="origin.csv"
overwrite=0
augmentation=1
augmentation_list_file="/home/park/tensorflow/my_train/learning_data_handler/augmentation_list.txt"
output_file="blur_augmentation.csv"

python3 learning_data_generator.py \
  --input_image_dir ${input_image_dir} \
  --input_image_path ${input_image_path} \
  --labeled_txt_path ${labeled_txt_path} \
  --make_origin ${make_origin} \
  --origin_path ${origin_path} \
  --origin_csv ${origin_csv} \
  --overwrite ${overwrite} \
  --augmentation ${augmentation} \
  --augmentation_list_file ${augmentation_list_file} \
  --output_file ${output_file}
