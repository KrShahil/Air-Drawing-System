# ✋ Air Drawing – Touchless Gesture-Based Drawing System

## 📌 Overview
Air Drawing is a computer vision–based application that allows users to draw on a virtual canvas using hand gestures, without using any physical input device such as a mouse, stylus, or touchscreen.  
The system tracks hand landmarks in real time using a webcam and maps finger movements to drawing actions on the screen.

This project was developed as a **Final-Year B.Tech (CSE) project** to demonstrate practical application of computer vision and human–computer interaction concepts.

---

## 🎯 Objectives
- To design a touchless drawing system using hand gestures  
- To understand and implement real-time hand landmark tracking  
- To apply gesture recognition for controlling drawing operations  
- To build an intuitive and low-cost human–computer interaction system  

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **OpenCV** – Video capture and drawing operations  
- **MediaPipe Tasks API** – Real-time hand landmark detection  
- **NumPy** – Array and canvas manipulation  

---

## ✨ Features
- Draw in the air using only the **index finger**
- Gesture-based **color selection**
- **Brush size control** using hand gestures
- **Clear canvas** using open palm gesture
- Fully **touchless interaction**
- Real-time performance using a standard webcam

---

## 🧠 Gesture Controls
| Gesture | Action |
|------|------|
| Index finger only | Draw on canvas |
| Index + Middle finger | Change drawing color |
| Index + Middle + Ring | Change drawing color (alternate) |
| Index + Pinky | Increase brush size |
| Index + Ring | Decrease brush size |
| Open palm (wide hand) | Clear the canvas |

---

## ⚙️ System Requirements
- Python 3.9 or above  
- Webcam  
- Windows OS (tested on Windows 10/11)  

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Air-Drawing-System.git
