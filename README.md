🖐 Gesture Volume & Brightness Controller
A real-time gesture-based system controller that adjusts Windows volume and screen brightness using hand gestures powered by Computer Vision.
Built using MediaPipe for hand tracking and Windows system APIs for hardware-level control.

🚀 Features

🫴 Right Hand → Controls System Volume

🫳 Left Hand → Controls Screen Brightness

🤏 Thumb–Index distance mapping

⚡ Real-Time Processing

🎯 Smooth signal interpolation

🖥 Direct Windows System API integration


🧠 How It Works

The system detects both hands using MediaPipe:

✋ Right Hand → Volume Control



Distance between Thumb tip (Landmark 4) and Index tip (Landmark 8)

Distance is mapped from [30px – 200px]

Converted to volume scalar range [0.0 – 1.0]

Applied using Windows Audio Endpoint API via Pycaw



✋ Left Hand → Brightness Control



Same thumb–index distance detection

Mapped to brightness range [0% – 100%]

Applied using screen_brightness_control



🎥 Usage Instructions

Ensure webcam is connected.

Keep hand clearly visible in front of camera.

Use:

Right hand → Volume

Left hand → Brightness

Increase distance → Increase level

Decrease distance → Decrease level

Press Ctrl + C in terminal to stop.


🛠 Tech Stack

Python,OpenCV,MediaPipe,NumPy,Pycaw (Windows Audio API),screen-brightness-control,Windows COM Interfaces.
