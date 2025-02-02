# [Doctor Chat](https://doctor-chat-mty8.onrender.com) – AI Assistant for Medical Consultations
Doctor Chat is an AI chatbot for medical advice, powered by GPT-2 and deployed with Streamlit and Docker.

## Description 
Doctor Chat is an AI-powered chatbot designed to provide medical advice and recommendations. It uses a fine-tuned GPT-2 model to generate responses in a structured dialogue format between the patient and a virtual doctor. The project includes a Streamlit web application deployed on a server for easy access.

Unfortunately, this is a learning project without funding, so it is hosted on a free web service with limited resources, which may affect its performance. However, you can run the application locally on your PC for full functionality.  

## Features
-  **Medical AI Consultant** – analyzes symptoms, suggests possible diagnoses, and recommends medical tests.  
-  **Fine-tuned GPT-2 model** – trained on structured medical conversations to enhance response accuracy.  
-  **Uses special tokens** `[|Human|]` and `[|AI|]` – to maintain structured dialogue.  
-  **Streamlit Web App** – provides a user-friendly interface for real-time interaction.  
-  **Docker Deployment** – ensures stable performance on a server.  

## Technologies
- **Text Modeling**: GPT-2, Hugging Face Transformers  
- **Data Processing**: Pandas
- **UI Framework**: Streamlit  
- **Containerization**: Docker  
- **Evaluation Metrics**: Perplexity (12.9094), Loss (2.6079)

## Installation & Setup  

### Clone the Repository  
```bash
git clone https://github.com/data-tamer2410/ds-doctor-chat
cd ds-doctor-chat
```

### Run with Docker  
```bash
docker build -t image_name .
docker run -it -p 8501:8501 image_name
```

### Run with Poetry  
```bash
pip install poetry
poetry install --without dev
poetry run streamlit run doctor_chat/app.py
```

Enjoy using **Doctor Chat**!  

## Important ⚠️  
Doctor Chat **is not a substitute for professional medical advice**. Always consult a healthcare professional for an accurate diagnosis.
