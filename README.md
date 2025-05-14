# Cat vs Dog Classifier
This project is a Flask web application that classifies images of cats and dogs using a pre-trained Convolutional Neural Network (CNN) model built with TensorFlow. The model predicts whether an uploaded image is a cat or a dog. Users can drag and drop images for prediction directly on the frontend.

# 🛠️ Technologies Used
Flask: Python web framework for creating the server-side application.

TensorFlow: Machine learning framework to load the pre-trained CNN model from saved models which are trained in training for image classification.

HTML, CSS, JavaScript: For frontend interface with drag-and-drop functionality.

Python 3.x: For backend logic and integration with TensorFlow.

# 🚀 Features
Drag and Drop Interface: Users can easily drag and drop images of cats or dogs for classification.

Real-Time Prediction: Instant feedback on whether the image is a cat or a dog.

Responsive UI: Designed to work across devices.

# 📦 Installation
Step 1: Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/cat-dog-classifier.git
cd cat-dog-classifier
Step 2: Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Step 3: Install the required dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt
txt
Copy
Edit
Flask==2.1.1
tensorflow==2.10.0
Pillow==9.1.0
numpy==1.21.0
Step 4: Download or create the pre-trained model
Ensure you have a trained model (e.g., model.h5) saved in your project directory. You can use your own model or follow a tutorial to train one. Place the model in the root directory of the project.

# 🎨 Usage
Step 1: Start the Flask app
bash
Copy
Edit
python app.py
This will start a local server at http://127.0.0.1:5000/.

Step 2: Open the app in your browser
Open http://127.0.0.1:5000/ in your web browser.

Drag and drop any cat or dog image into the drop area, and it will predict the class (Cat or Dog) and display the result.

🖼️ Images for Testing
Place your images inside the static/sample_images/ folder. The app currently uses 5 cat images and 5 dog images that can be dragged and dropped for classification.

# 🧑‍💻 Running the Project
To run the project:

Clone the repository and set up the environment.

Run the Flask server with python app.py.

Navigate to http://127.0.0.1:5000/ in your web browser.

# 📂 Project Structure
bash
Copy
Edit
cat-dog-classifier/
│
├── app.py                 # Main Flask app
├── requirements.txt       # Project dependencies
├── static/
│   └── sample_images/     # Folder containing sample cat and dog images
├── templates/
│   └── index.html         # Frontend HTML page
├── model.h5               # Pre-trained CNN model file
└── README.md              # Project documentation
# ⚙️ How It Works
Frontend:

Users drag and drop images into the designated area.

Images are sent to the backend using JavaScript Fetch API.

# Backend:

The image is received by the Flask server.

The image is processed, resized, and normalized to fit the model input.

The model makes a prediction (cat or dog) and sends the result back to the frontend.

Prediction:

The result (either "Cat" or "Dog") is displayed on the page.

# 🛠️ Troubleshooting
Issue: TensorFlow model not loading
Solution: Ensure that your model is correctly saved as model.h5 and placed in the correct directory.

Issue: Drag and drop not working
Solution: Ensure that JavaScript is enabled in your browser and there are no errors in the browser's developer console.

# 🔄 License
This project is licensed under the MIT License.

