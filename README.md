# Neurolysis

Neurolysis is a platform designed to analyze the learning styles of neurodiverse children, helping parents and teachers understand and support their unique ways of learning to foster an unrestricted educational experience.

Link to the application: https://neurolysis-cneckkduroywadmgxobzko.streamlit.app/ 
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Learning Style Analysis**: Provides detailed reports on the learning styles of neurodiverse children.
- **Support Recommendations**: Offers personalized strategies and tools to support each child's unique learning needs.
- **Interactive Visualization**: Uses Streamlit for an engaging and easy-to-use interface.
- **API Integration**: Utilizes the Gemini API to analyze and process learning data.

## Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Gemini API access

### Step-by-Step Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/Shaik-mohd-huzaifa/neurolysis.git
    cd neurolysis
    ```

2. **Create and Activate a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**
    Create a `.env` file in the project root directory and add your Gemini API key:
    ```sh
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

### Running the Application
1. **Start the Streamlit Server**
    ```sh
    streamlit run app.py
    ```

2. **Access the Application**
    Open your web browser and navigate to `http://localhost:8501`.

### Application Flow
1. **Analyze**: The application will use the Gemini API to analyze the data.
2. **View Results**: View the detailed report on the child's learning style and get recommendations.

## Configuration

### Streamlit Configuration
You can configure Streamlit settings by editing the `config.toml` file located in the `.streamlit` directory.

### Gemini API Configuration
Make sure your `.env` file contains the correct API key:
```sh
GEMINI_API_KEY=your_gemini_api_key_here
