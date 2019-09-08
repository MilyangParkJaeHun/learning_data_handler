input_image_dir="/home/park/Desktop/image_data"
input_image_path="labeled"
labeled_txt_path="/home/park/Desktop/image_data/txt"
make_origin=1
origin_path="/home/park/Desktop/image_data"
origin_csv="origin.csv"
overwrite=1
augmentation=1
augmentation_list_file="/home/park/dev/learning_data_handler/augmentation_list.txt"

python3 learning_data_generator.py \
  --input_image_dir ${input_image_dir} \
  --input_image_path ${input_image_path} \
  --labeled_txt_path ${labeled_txt_path} \
  --make_origin ${make_origin} \
  --origin_path ${origin_path} \
  --origin_csv ${origin_csv} \
  --overwrite ${overwrite} \
  --augmentation ${augmentation} \
  --augmentation_list_file ${augmentation_list_file}
