import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('C:/Users\Darre\Desktop\yolov8-main/runs/train\others\exp8\weights/best.pt') # select your model.pt path
    model.predict(source='dataset/images/test',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                #   visualize=True # visualize model features maps
                )