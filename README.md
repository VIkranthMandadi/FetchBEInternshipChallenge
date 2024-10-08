# FetchBEInternshipChallenge

This project is a simple points spending backend that calculates how points have been spent based on timestamp and payer information. The program handles requests for adding and spending points, ensuring that points are spent according to the rules outlined in the prompt.

## Requirements

- Python 3.7 or later
- `pip` (Python package installer)

## Setup

### 1. Set up a Virtual Environment

It is recommended to run this project in a virtual environment. Follow the instructions based on your operating system (Linux, Windows, or Mac) to set up the environment.

#### Linux & macOS

1. **Create a virtual environment:**

   ```bash
   To create the virtual environment: python3 -m venv venv
   To activiate the virtual environment: source venv/bin/activate
   To deactivate the virtual environment: deactivate

   ```

2. **Install the packages Needed**

   I have created a requirements.txt file to make installation of packages simple.
   Once you activate your virtual environment run the command: `pip install -r requirements.txt`

3. **Run the Program**

   To run the program, run the command: `python3 app.py`
   If that does not work try: `python app.py`
   If that does not work please check if you have python or the correct version installed.

#### Windows

1. **Create a virtual environment:**

   ```windows
   To create the virtual environment: python -m venv venv
   To activiate the virtual environment: .\venv\Scripts\activate
   To deactivate the virtual environment: deactivate

   ```

2. **Install the packages Needed**

   I have created a requirements.txt file to make installation of packages simple.
   Once you activate your virtual environment run the command: `pip install -r requirements.txt`

3. **Run the Program**

   To run the program, run the command: `python3 app.py`
   If that does not work try: `python app.py` or try `py app.py`
   If that does not work please check if you have python or the correct version installed.

#### Testing Endpoints

1. **Using Postman**

   If you are comfortable with with a tool such as postman or insomnia, I recommend
   using one of those.

   To use postman:

   1. Make sure you have postman installed
   2. Run your program
   3. Paste your URL + endpoint into the request (e.x. http://127.0.0.1:8000/balance)
   4. Make sure the request is set to the correct type (i.e. POST, GET, etc)
   5. Select body and provide a valid json body for that request type

2. **Using Curl**

   The program can still be tested without using a tool like postman or insomnia.
   Rather a curl request such as:
   `curl -X POST http://127.0.0.1:8000/add \
    -H "Content-Type: application/json" \
    -d '{
   "payer": "DANNON",
   "points": 300,
   "timestamp": "2022-10-31T10:00:00Z"
   }'`
   can be placed directly into the terminal

   Another example for a GET request can be: `curl http://127.0.0.1:8000/balance`
