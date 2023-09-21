# ubiquitous-guide

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arjun-234/ubiquitous-guide
   ```
2. Navigate to the project directory:
   ```bash
   cd your-flask-project
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment (replace `venv` with the appropriate name if you chose a different one):
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Make sure you are in the project directory and the virtual environment is activated.
2. Set the FLASK_APP environment variable to specify the path to your Flask application:
   - On Windows:
     ```bash
     set FLASK_APP=main.py
     ```
   - On macOS and Linux:
     ```bash
     export FLASK_APP=main.py
     ```
3. Start the Flask development server:
   ```bash
   flask run
   ```
4. Open a web browser and navigate to `http://localhost:5000` to access the application.

## Endpoint
To test the GET API endpoint, simply send a request to `http://localhost:5000/api/greet`, and you will receive a friendly greeting in response.
