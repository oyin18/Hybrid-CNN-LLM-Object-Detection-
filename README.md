# Smart City Object Detection using YOLOv5 + Gemini LLM

This project is a hybrid deep learning system that combines a **Convolutional Neural Network (YOLOv5)** with a **Large Language Model (LLM)** (e.g., Gemini) to perform **object detection** and **natural language interpretation** of scenes in smart cities.

##  Overview

- Detects objects like **cars, traffic lights, pedestrians, bikes, etc.**
- Uses **YOLOv5** for fast object detection
- Uses **LLM (Gemini)** to generate descriptive analysis of the scene
- Exposes a **Flask API** you can test with **Postman**


##  Project Structure

yolo5-main/
│
├── server.py # Main Flask server file
├── yolo.py # Runs YOLOv5 on the uploaded image
├── yolov5n.pt # Pre-trained YOLOv5 model
├── requirements.txt # Python dependencies
├── README.md # This file
├── project pic.PNG # Screenshot of Postman API output
│
├── routes/
│ ├── analyse.py # Handles Gemini-based language analysis
│ └── report.py # Combines detection + description
│
├── .env # Environment variables (optional)
├── check_env.py # Environment checker



## How to Set Up

### 1️⃣ Install Python Requirements
Make sure you have Python 3.8+ and then run:

```bash
pip install -r requirements.txt

2️⃣ Start the Flask Server
bash 
python server.py
You should see something like:

 * Running on http://127.0.0.1:5000/
3️⃣ Test with Postman
Endpoint 1: /report — Object detection + description

Endpoint 2: /analyse — Only language model interpretation

Method: POST

Body: Form-data → Key: file, Value: (upload your image)

##  Sample Output
Below is a screenshot showing the output of the API in Postman:
(postman.project.PNG)

##  Technologies Used
YOLOv5 (object detection)

Gemini LLM API or any alternative (image captioning/analysis)

Flask (API framework)

Postman (for testing)

##  Use Cases
Intelligent traffic systems

Smart surveillance

Infrastructure monitoring

Autonomous vehicles

##  Status
Project is functional and tested locally via Postman.
Can be extended with real-time video or frontend integration.

