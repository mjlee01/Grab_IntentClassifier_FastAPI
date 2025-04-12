# Driver Intent Prediction API 🚗🧠

This is a FastAPI backend that predicts the intent of a driver (e.g. accepting or rejecting an order) based on a given input sentence. It supports multiple languages (English, Malay, Chinese).

## 🧠 Features

- Predicts 4 intents:
  - `accept_order`
  - `reject_order`
  - `start_request`
  - `stop_request`
- Uses `sentence-transformers` for multilingual sentence embeddings
- Trained with `scikit-learn` Logistic Regression
- API built with FastAPI

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mjlee01/Grab_IntentClassifier_FastAPI.git
cd Grab_IntentClassifier_FastAPI
```

### 2. Create a Virtual Environment
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Run the API
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000/`.

## How to Test the API
You can test the API using tools like `curl` or Postman. Here's an example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"sentence": "I accept the order"}'
```
Expect a response like:
```json
{
    "intent": "accept_order"
}
```

## Project Structure
```
Grab_IntentClassifier_FastAPI/
├── main.py                # FastAPI app
├── model/
│   ├── intent_classifier.pkl
├── venv/                  # Virtual environment (should be excluded via .gitignore)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md              # This file、
```