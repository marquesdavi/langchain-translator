# LangChain Translator Project

## Overview
LangChain Translator is a web application that allows users to translate sentences from English to Portuguese using OpenAI's GPT-4 model. The project is built using Vue.js for the frontend and FastAPI for the backend, and it uses Docker for containerization.

## Prerequisites
Before you start, ensure you have the following installed on your system:
- Docker
- Docker Compose

## Project Structure
```
LangChainTranslator/
│
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── HeaderComponent.vue
│   │   │   ├── ...
│   │   ├── App.vue
│   │   ├── main.js
│   ├── nginx.conf (optional)
│   ├── Dockerfile
│   ├── vue.config.js
│   ├── package.json
│   └── ...
│
├── docker-compose.yml
└── README.md (this file)
```

## Setup Instructions

### Running with Docker Compose (Simplest Way)
The easiest way to run the LangChain Translator project is by using Docker Compose. Follow these steps:

#### Clone the Repository
Clone the project repository to your local machine:
```sh
git clone https://github.com/marquesdavi/langchain-translator.git
cd langchain-translator
```

#### Setup Environment Variables
Create a `.env` file in the backend directory with your OpenAI API key:
```sh
echo "OPENAI_API_KEY=your_openai_api_key" > backend/.env
```

#### Build and Run with Docker Compose
Use Docker Compose to build and run the services:
```sh
docker-compose up --build
```
This command will build the Docker images for both the frontend and backend and start the containers. The frontend will be accessible at [http://localhost:3000](http://localhost:3000) and the backend at [http://localhost:8000](http://localhost:8000).

#### Verify the Setup
- **Frontend**: Open your browser and navigate to [http://localhost:3000](http://localhost:3000). You should see the LangChain Translator interface.
- **Backend**: You can test the backend API directly by using tools like curl or Postman.
```sh
curl -X POST "http://localhost:8000/translate" -H "Content-Type: application/json" -d '{"sentence": "Hello"}'
```

### Local Development

#### Frontend
For local development of the frontend, you can use the Vue.js development server:

Navigate to the frontend directory:
```sh
cd frontend
```

Install the dependencies:
```sh
npm install
```

Start the development server:
```sh
npm run serve
```
The frontend development server will start on [http://localhost:3000](http://localhost:3000).

#### Backend
For local development of the backend, you can use the FastAPI development server:

Navigate to the backend directory:
```sh
cd backend
```

Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the dependencies:
```sh
pip install -r requirements.txt
```

Start the development server:
```sh
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```
The backend development server will start on [http://localhost:8000](http://localhost:8000).

## Project Details

### Backend
- **Framework**: FastAPI
- **File**: `api/main.py`
- **Dependencies**: Listed in `requirements.txt`
- **Dockerfile**: Builds the backend application
- **Main Endpoints**
  - `POST /translate`: Translates a given sentence from English to Portuguese.

### Frontend
- **Framework**: Vue.js
- **Entry Point**: `src/main.js`
- **Components**: Located in `src/components`
- **Dockerfile**: Builds the frontend application and serves it using Nginx
- **Custom Nginx Configuration (Optional)**: If you need to customize the Nginx configuration, you can do so by editing the `nginx.conf` file in the frontend directory and updating the Dockerfile to use this custom configuration.

## Troubleshooting

### Common Issues

#### CORS Errors
- Ensure that the CORS middleware in the FastAPI application is correctly configured with the allowed origins.

#### Docker Network Issues
- Make sure the Docker network is properly set up and both services are connected to it.

#### API Key Issues
- Ensure your OpenAI API key is correctly set in the `.env` file in the backend directory.
