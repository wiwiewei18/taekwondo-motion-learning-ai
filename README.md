# Taekwondo Motion Learning

The Taekwondo Motion Learning is a WSGI (Web Server Gateway Interface) server designed for classifying Taekwondo Motion images using machine learning. It is built using the Flask Python framework and leverages the Ultralytics YOLOv8 model for image classification.

## Description

The Taekwondo Motion Learning serves as an AI-powered tool capable of classifying Taekwondo Motion images. It utilizes state-of-the-art machine learning techniques, specifically the Ultralytics YOLOv8 model, to achieve accurate image classification.

## Getting Started

### Dependencies

- Flask
- Ultralytics YOLOv8

### Installation

To get started, follow these steps:

- Clone the repository:

```
> git clone https://github.com/wiwiewei18/taekwondo-motion-learning-ai.git
```

- Set up a virtual environment and install Flask:

```
> py -3 -m venv .venv
> .venv\Scripts\activate
> pip install Flask
> pip install flask_cors
```

- Train the machine learning model:

```
> cd ./taekwondo_motion_learning/machine_learning/image_classification
> py train.py
```

### Running the Application

- Make sure you are in the root directory of the project with the virtual environment activated, then execute the program using Flask:

```
flask --app taekwondo_motion_learning run
```

## Authors

Contributor:

- Wiwie Sanjaya [@wiwiewei18](https://github.com/wiwiewei18)

## Version History

- 0.1
  - Initial Release

## Acknowledgments

This project drew inspiration and knowledge from the following sources:

- [flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Ultralytics YOLOv8 Tutorial - Computer vision engineer](https://www.youtube.com/playlist?list=PLb49csYFtO2FXGMZxqmPrw_0GPJnPR0Up)
