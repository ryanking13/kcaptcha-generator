import pathlib
import random
import json
import cv2

def main():
    _dataset_dir = ".data/train"
    dataset_dir = pathlib.Path(_dataset_dir)
    
    images = list(dataset_dir.glob("*.png"))

    img_file = random.choice(images)
    annotation_file = pathlib.Path(img_file.as_posix().replace(".png", ".json"))
    
    img = cv2.imread(str(img_file))
    annotation = json.loads(annotation_file.read_text())
    
    bboxs = annotation["bbox"]

    img_bbox = img
    for b in bboxs:
        img_bbox = cv2.rectangle(img_bbox, (b["xmin"], b["ymin"]), (b["xmax"], b["ymax"]), (255, 0, 0), 2)

    cv2.imshow("bbox", img_bbox)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

if __name__ == "__main__":
    main()