# TruthGuard-AI Backend

## Overview

# TruthGuard-AI Backend

## Overview

TruthGuard-AI is an advanced AI-driven fake news detection system that leverages natural language processing and machine learning to accurately identify and flag potential instances of fake news. Our cutting-edge technology examines content, source, and spread patterns to provide reliable, real-time information verification.

## The Problem

Fake news is a widespread issue with serious consequences:
1. Rapid dissemination through social media platforms
2. Erosion of trust in legitimate news sources
3. Negative impact on public opinion and decision-making
4. Potential harm to individuals (financial losses, reputational damage, emotional distress)

## Our Approach

We've developed a robust AI-powered system that provides real-time analysis of news content with high accuracy detection. The system offers transparency and explainability in its assessments, empowering users to make informed decisions.

## Key Features

- Real-time classification of news articles
- High accuracy detection using the fine-tuned Llama 3 model
- Transparent explanations for the system's assessments
- User-friendly API for easy integration
- Support for both system and user messages for context
- Basic error handling and logging

## Technologies Used

- **Llama-3 Model**: The backbone of our fake news detection engine, providing advanced text analysis capabilities
- **LlamaIndex**: An innovative knowledge graph system for seamless integration and querying of diverse data sources
- **Together AI**: Platform for model hosting and collaborative verification
- **Milvus Vector Database**: High-performance vector database for efficient storage and querying of vast amounts of data
- **Flask**: Web framework for the API

## Prerequisites

- Python 3.7 or later
- Flask
- Together AI account and API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/djpapzin/TruthGuard-AI.git
   cd TruthGuard-AI
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Together AI API key:
   ```
   export TOGETHER_API_KEY='your_api_key_here'
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

3. To classify a news article, send a POST request to `/classify` with the following JSON payload:
   ```json
   {
     "article": "Your news article text here"
   }
   ```

4. The API will respond with a classification result:
   ```json
   {
     "classification": "real" or "fake",
     "confidence": 0.95
   }
   ```

## API Endpoints

- `POST /classify`: Classifies a news article as real or fake
- `GET /`: Returns a simple message (can be used as a health check)

## How It Works

1. **User Input**: Users submit a URL or content for analysis through the API.
2. **Processing & Analysis**: 
   - The submitted data is preprocessed and converted into numerical embeddings using the Llama-3 model.
   - The system performs a context-based semantic search to compare the new article with known fake and real news.
3. **Response**: The user receives a response indicating whether the news is likely fake or real, along with a confidence score.

## Model Information

The backend uses a fine-tuned Llama 3 model hosted on Together AI. The model was trained on the WELFake Dataset, which contains a collection of real and fake news articles.

## Future Enhancements

- Implement user authentication and rate limiting
- Add support for batch classification
- Integrate with a frontend application for a complete user interface
- Implement caching to improve performance
- Add more comprehensive error handling and input validation
- Continuous improvement through machine learning algorithms
- Multilingual support for detecting fake news in multiple languages
- Automated monitoring to proactively scan online content
- Seamless integration with popular social media platforms and news aggregators

## Team

- Reema Memon - NLP Engineer (Team Lead)
- Sami Raza - AI Developer
- Letlhogonolo Fanampe - AI Specialist
- Wajahat Ali Hassan - Backend Developer
- Muhammad Qasim - Frontend Developer
- Muhammad Hassan - Full Stack Developer

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.TruthGuard-AI is an AI-driven fake news detection system that uses a fine-tuned Llama 3 model to classify news articles as real or fake in real-time. This backend service provides an API endpoint for news article classification.

## Features

- Real-time classification of news articles
- Uses Together AI's fine-tuned Llama 3 model
- Flask-based API for easy integration
- Supports both system and user messages for context
- Basic error handling and logging

## Prerequisites

- Python 3.7 or later
- Flask
- Together AI account and API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/djpapzin/TruthGuard-AI.git
   cd TruthGuard-AI
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Together AI API key in:
   ```
   export TOGETHER_API_KEY='your_api_key_here'
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

3. To classify a news article, send a POST request to `/classify` with the following JSON payload:
   ```json
   {
     "article": "Your news article text here"
   }
   ```

4. The API will respond with a classification result:
   ```json
   {
     "classification": "real" or "fake"
   }
   ```

## API Endpoints

- `POST /classify`: Classifies a news article as real or fake
- `GET /`: Returns a simple message (can be used as a health check)

## Model Information

The backend uses a fine-tuned Llama 3 model hosted on Together AI. The model was trained on the WELFake Dataset, which contains a collection of real and fake news articles.

## Future Improvements

- Implement user authentication and rate limiting
- Add support for batch classification
- Integrate with a frontend application for a complete user interface
- Implement caching to improve performance
- Add more comprehensive error handling and input validation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.