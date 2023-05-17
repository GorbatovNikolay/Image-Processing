import os

from imageai.Detection import ObjectDetection, VideoObjectDetection

EXEC_PATH = os.getcwd()


def detect_objects():
    detector = ObjectDetection()
    detector.useCPU()
    
    # загрузить модель по ссылке 
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(EXEC_PATH, 'retinanet_resnet50_fpn_coco-eeacb38b.pth'))
    detector.loadModel()

    objects_from_image = detector.detectObjectsFromImage(
        input_image=os.path.join(EXEC_PATH, 'people.jpg'),
        output_image_path=os.path.join(EXEC_PATH, 'processed_people.jpg'),
        minimum_percentage_probability=20,
        display_percentage_probability=True,
        display_object_name=True
    )


def detect_video_objects():
    detector = VideoObjectDetection()
    detector.useCPU()

    # загрузить модель по ссылке
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(EXEC_PATH, 'yolov3.pt'))
    detector.loadModel()

    frames = detector.detectObjectsFromVideo(
        input_file_path=os.path.join(EXEC_PATH, 'traffic.mp4'),
        output_file_path=os.path.join(EXEC_PATH, 'traffic_detected'),
        frames_per_second=20,
        log_progress=True
    )

    print(frames)


def main():
    # detect_objects()
    detect_video_objects()


if __name__ == '__main__':
    main()
