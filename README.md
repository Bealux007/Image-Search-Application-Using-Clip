# Image-Search-Application-Using-Clip

**📖 Overview**
The Image Search Application is a Streamlit-based web app that allows users to search for images using text descriptions or by uploading an image. The system utilizes OpenAI's CLIP model to compute text and image embeddings, enabling a powerful semantic search mechanism.

**🚀 Features**
✅ Search by Text - Enter a description and find matching images.
✅ Search by Image - Upload an image and find visually similar images.
✅ CLIP Model-Based Embeddings - Uses OpenAI's CLIP model for semantic matching.
✅ Interactive Web UI - Built using Streamlit for an easy-to-use interface.

**📂 Project Structure**
**📦 Image-Search-App**
├── app.py                 # Streamlit web application
├── clip_model.py          # CLIP model wrapper for generating embeddings
├── search.py              # Image search logic (loads images, computes embeddings, searches)
├── requirements.txt       # Required dependencies
├── README.md              # Documentation
└── data/
    ├── images/            # Folder containing searchable images
    
**🛠 Technologies Used**

Technology	        Purpose**
Streamlit 🎨	Web UI for search functionality
OpenAI CLIP 🤖	Text and image embedding model
Torch (PyTorch) 🔥	Handles deep learning computations
Pillow (PIL) 🖼️	Image processing
Transformers	Loads the CLIP model
Gradio	(Optional) Alternative UI


**📜 File Descriptions**
**1️⃣ clip_model.py (CLIP Model Wrapper)**
Loads OpenAI’s CLIP model to generate text and image embeddings.
Provides two key functions:
get_image_embedding(image): Converts an image into a feature vector.
get_text_embedding(text): Converts a text query into a feature vector.

**2️⃣ search.py (Image Search Implementation)**
Loads all images from the data/images/ folder.
Computes and stores embeddings for all images in memory.
Provides two main search functions:
search_by_text(text): Finds the top-k images that match a text query.
search_by_image(image): Finds visually similar images based on an uploaded image.
Uses cosine similarity between embeddings for ranking.

**3️⃣ app.py (Streamlit Web Application)**
Provides an interactive UI for searching images via:
Text-based search: Users input a text description.
Image-based search: Users upload an image.
Displays top-matching images from the dataset.
Uses the ImageSearch class from search.py to retrieve results.

**4️⃣ requirements.txt (Dependencies)**
Lists all required Python libraries:
streamlit
gradio
torch
transformers
Pillow
requests
python-dotenv

**🛠 Installation & Setup**
1️⃣ Clone the Repository
git clone https://github.com/Bealux007/Image-Search-App.git
cd Image-Search-App

**2️⃣ Create a Virtual Environment**
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
**3️⃣ Install Dependencies**
pip install -r requirements.txt
4️⃣ Set Up Image Data
mkdir -p data/images
Place images inside data/images/.

**🚀 Running the Application**
**Run the Streamlit Web App**
streamlit run app.py

Open the generated local link.
Choose a search method (Text or Image).
View the top-matching images.

**📜 License**
This project is MIT Licensed.

**🔗 Contribute**
Pull requests are welcome! If you find a bug, open an issue.
