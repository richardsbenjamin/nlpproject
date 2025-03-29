# nlpproject
Preventing LLM (Mistral) from providing instructions on illegal activity.

## Requirements
- Python 3.8 or higher
- Virtualenv

## Installation and Usage

```bash
# 1. Clone the Repository
git clone <repository_url>
cd <repository_name>

# 2. Set Up a Virtual Environment
# MacOS/Linux (Ubuntu)
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Create a .env File
# In the root directory of the project, create a .env file to store your API key:
# Add the following line and replace 'your_mistral_api_key_here' with your actual API key:
echo "API_KEY=your_mistral_api_key_here" > .env

# 5. Run the Application
# MacOS/Linux (Ubuntu)
python ui/app.py

# Windows
python ui/app.py

Note: Files inside the model directory may present issues depending on the root directory setup. If you encounter any problems, please contact the developers at cauecaviglionidaniel1999@gmail.com.
