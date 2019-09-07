import fiji_to_csv
import image_augmentation
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--input_image_dir", help="input image dir used in tensorflow api")
parser.add_argument("--input_image_path", help="input image path from input_image_dir")
parser.add_argument("--labeled_txt_path", help="labeled text file path")
parser.add_argument("--make_origin", help="make origin data or not", type=int)
parser.add_argument("--origin_path", help="output origin data csv path")
parser.add_argument("--origin_csv", help="origin data csv file name")
parser.add_argument("--overwrite", help="overwrite or not", type=int)
parser.add_argument("--augmentation", help="do data augmentation or not", type=int)
args = parser.parse_args()

def main(input_image_dir, input_image_path, labeled_txt_path, make_origin, origin_path, origin_csv, overwrite, augmentation):
  file_open_format = "a" if overwrite==0 else "w"

  if make_origin == 1:
    fiji_to_csv.convert(input_image_dir, input_image_path, labeled_txt_path, origin_path, origin_csv, file_open_format)
  if augmentation == 1:
    image_augmentation.augmentation(input_image_dir, origin_path, origin_csv)

if __name__ == '__main__':
  main(args.input_image_dir, args.input_image_path, args.labeled_txt_path, args.make_origin, args.origin_path, args.origin_csv, args.overwrite, args.augmentation)
