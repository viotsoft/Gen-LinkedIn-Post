# AI Social Media Post Generator

A powerful web application that leverages OpenAI's GPT-4 to generate engaging social media posts for LinkedIn and X (Twitter). This tool helps content creators, marketers, and professionals create high-quality, platform-specific content with customizable tone and style.

## Features

- **Multi-Platform Support**: Generate posts for LinkedIn and X (Twitter)
- **Customizable Content**: Adjust tone, type, and target audience
- **Smart Generation**: AI-powered content creation using GPT-4
- **Feedback System**: Collect and store user feedback for continuous improvement
- **Modern UI**: Clean and intuitive Streamlit interface
- **RESTful API**: FastAPI backend with comprehensive error handling
- **Data Storage**: CSV-based feedback storage with UTF-8 encoding

## Tech Stack

- **Backend**: FastAPI, Python 3.12
- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4
- **Data Storage**: CSV
- **Environment Management**: Python-dotenv

## Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Git

## Security Best Practices

1. **API Key Protection**:
   - Never commit your `.env` file to version control
   - Use `.env.example` as a template for required environment variables
   - Keep your API keys secure and rotate them periodically
   - Use environment variables in production deployments

2. **Environment Setup**:
   - Copy `.env.example` to `.env` in the backend directory
   - Replace placeholder values with your actual API keys
   - Never share your `.env` file or API keys publicly

3. **Production Deployment**:
   - Use secure environment variable management in your hosting platform
   - Consider using a secrets management service
   - Implement rate limiting and API key rotation
   - Monitor API usage and set up alerts for unusual activity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-social-post-generator.git
cd ai-social-post-generator
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Install frontend dependencies:
```bash
cd ../frontend
pip install streamlit requests
```

5. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual API key
# OPENAI_API_KEY=your-api-key-here
```

## Running the Application

1. Start the backend server:
```bash
cd backend
python -m uvicorn main:app --reload
```

2. In a new terminal, start the frontend:
```bash
cd frontend
streamlit run app.py
```

3. Access the application:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Usage

1. Select your target platform (LinkedIn or X)
2. Choose the desired tone (Professional, Conversational, or Witty)
3. Select the post type (Thought Leadership, Promo, or Thread)
4. Specify your target audience
5. Enter your content goal
6. Provide your topic or post idea
7. Click "Generate Post"
8. Review the generated content
9. Optionally provide feedback

## API Endpoints

### POST /generate
Generates a social media post based on provided parameters.

Request body:
```json
{
    "platform": "LinkedIn" | "X",
    "tone": "Professional" | "Conversational" | "Witty",
    "type": "Thought Leadership" | "Promo" | "Thread",
    "audience": "string",
    "goal": "string",
    "topic": "string"
}
```

### POST /feedback
Submits feedback for a generated post.

Request body:
```json
{
    "post": "string",
    "feedback": "string"
}
```

## Project Structure

```
ai-social-post-generator/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── feedback.csv
├── frontend/
│   └── app.py
├── .gitignore
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-4 API
- FastAPI for the robust backend framework
- Streamlit for the intuitive frontend framework

## Contact

For questions or support, please open an issue in the GitHub repository. 