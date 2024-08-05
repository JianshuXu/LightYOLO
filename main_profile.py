from ultralytics import YOLO

if __name__ == '__main__':
    # choose your yaml file
    model = YOLO('ultralytics/cfg/models/v8/yolov8-C2f-AKConv.yaml')
    model.info(detailed=True)
    model.profile(imgsz=[640, 640])
    model.fuse()