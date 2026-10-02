# EduGenie AI 🎓🤖

### AI-Powered Personalized Learning Assistant

EduGenie AI is an AI-powered educational platform designed to make
learning easier, smarter, and more interactive. It helps students
understand complex topics, ask academic questions, generate quizzes,
summarize study materials, and create personalized learning paths using
Artificial Intelligence.

The project uses **FastAPI, Python, Google Gemini, Hugging Face
Transformers, HTML, CSS, and JavaScript** to provide an interactive
web-based learning experience.

## 🚀 Features

-   💬 **AI Question & Answer:** Get clear and easy-to-understand
    answers to academic questions.
-   🧠 **Concept Explanation:** Learn complex concepts through simple
    explanations using AI.
-   📝 **AI Quiz Generation:** Generate multiple-choice quizzes to test
    your understanding.
-   📚 **Text Summarization:** Convert lengthy educational content into
    concise study notes.
-   🎯 **Personalized Learning Path:** Generate structured learning
    plans based on topics and skill levels.
-   🤖 **Dual AI Support:** Uses Google Gemini and a local Hugging Face
    model for concept explanations.
-   🌐 **Interactive Web Interface:** Simple and responsive frontend for
    students.
-   ⚡ **REST API:** FastAPI backend for handling learning requests.

## 🛠️ Technologies Used

  Technology                  Purpose
  --------------------------- ----------------------------
  Python                      Backend development
  FastAPI                     REST API framework
  Google Gemini               AI-powered responses
  Hugging Face Transformers   Local AI explanation model
  PyTorch                     Local model execution
  HTML5                       Webpage structure
  CSS3                        User interface styling
  JavaScript                  Frontend interactions
  Pydantic                    Data validation
  Jinja2                      HTML template rendering
  Pytest                      Automated testing

## 🏗️ Project Architecture

``` text
EduGenie-AI/
│
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
│
├── static/
│   ├── app.js
│   └── style.css
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_app.py
```

### Architecture Overview

1.  **Frontend:** HTML, CSS and JavaScript handle user input and display
    AI-generated responses.
2.  **Backend:** FastAPI receives and validates requests and routes them
    to the appropriate learning module.
3.  **AI Processing:** The relevant module generates a prompt and calls
    the configured AI model.
4.  **Response:** The generated result is returned through the API and
    displayed on the web interface.

## ⚙️ Installation and Setup

### 1. Clone the Repository

``` bash
git clone https://github.com/YOUR-USERNAME/EduGenie-AI.git
```

### 2. Navigate to the Project Directory

``` bash
cd EduGenie-AI/EduGenie.AI
```

### 3. Create a Virtual Environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

On Linux or macOS:

``` bash
source venv/bin/activate
```

### 4. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the backend directory and add your Gemini API
key:

``` env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
USE_LOCAL_EXPLAINER=false
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**Important:** Keep your API key private. Never commit your `.env` file
or expose your API key in frontend JavaScript.

### 6. Run the Application

``` bash
uvicorn main:app --reload
```

Open the following URL in your browser:

``` text
http://127.0.0.1:8000
```

## 📡 API Endpoints

  --------------------------------------------------------------------------
  Method                  Endpoint                   Description
  ----------------------- -------------------------- -----------------------
  GET                     `/`                        Load the web
                                                     application

  GET                     `/health`                  Check application
                                                     health

  POST                    `/qa`                      Answer academic
                                                     questions

  POST                    `/explain`                 Explain educational
                                                     concepts

  POST                    `/quiz`                    Generate
                                                     multiple-choice quizzes

  POST                    `/summarize`               Summarize educational
                                                     content

  POST                    `/learn/recommendations`   Generate personalized
                                                     learning paths
  --------------------------------------------------------------------------

### API Documentation

FastAPI automatically provides interactive API documentation.

Once the server is running, visit:

``` text
http://127.0.0.1:8000/docs
```

## 🧪 Running Tests

Run the included tests using Pytest:

``` bash
pytest -v
```

The test suite includes basic API, health-check, and input-validation
tests.

## 🎯 Use Cases

-   Students learning new academic subjects.
-   Learners preparing for examinations.
-   Students who need simplified explanations of difficult topics.
-   Learners who want to evaluate their understanding through quizzes.
-   Students who need structured learning plans.

## 🔮 Future Enhancements

-   👤 Student registration and authentication.
-   📊 Student performance tracking and analytics.
-   🏆 Gamified learning with badges and achievements.
-   📄 PDF and document-based learning.
-   📈 Adaptive learning recommendations based on previous performance.
-   👨‍🏫 Teacher dashboard and classroom management.
-   📚 Learning history and progress tracking.
-   🌍 Support for multiple languages.

## 🔐 Security

-   Store API keys in environment variables.
-   Do not expose secret credentials in frontend code.
-   Configure appropriate request validation and error handling.
-   Add authentication and rate limiting before public deployment.

## 🤝 Contributing

Contributions are welcome!

1.  Fork this repository.

2.  Create a new branch:

    ``` bash
    git checkout -b feature/YourFeature
    ```

3.  Commit your changes:

    ``` bash
    git commit -m "Add YourFeature"
    ```

4.  Push your branch:

    ``` bash
    git push origin feature/YourFeature
    ```

5.  Open a Pull Request.

## 👨‍💻 Project

**EduGenie AI -- AI-Powered Personalized Learning Assistant**

Developed as an educational AI project to make learning more accessible,
interactive, and personalized.

## 📄 License

No license has been specified yet. Add a license file if you intend to
distribute or allow reuse of this project.

------------------------------------------------------------------------

⭐ If you find EduGenie AI useful, consider starring the repository!
