# Person Detector

## Highly performant, and accurate, real-time person tracking with YOLOv10 and ByteTrack

### Command-Line Interface

#### Clone repo and navigate to project directory

```bash
git clone git@github.com:k3y5tr0k3/person-detector.git && cd person-detector
```

#### Install requirements

```bash
pip install -r requirements.txt
```

#### Example usage

##### Detections from Image

```bash
python -m src.main --image 'path/to/image.jpg' --detection --show
```

##### Detections from Video

```bash
python -m src.main --video 'path/to/video.mp4' --detection --show
```

##### Trajectory Tracking from Video
```bash
python -m src.main -video 'path/to/video.mp4' --tracking --show
```

##### For more info, use the help flag

```bash
python -m src.main --help
```

### Utility Functions

#### Convert video to images

```bash
python -m src.main --video2images 'path/to/video.mp4
```

### Generate Developer Documentation (Optional)

```bash
pdoc ./src
```

### Performance

