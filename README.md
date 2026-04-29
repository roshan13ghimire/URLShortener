# URL Shortener (Flask + SQLite + React)

A simple full-stack URL shortener built using React for the frontend and Flask with SQLite for the backend. This project allows users to shorten long URLs and redirect them using a generated short code.

---

## Features

- Shorten long URLs
- Redirect using short URL
- Prevent duplicate URL entries
- Store data using SQLite
- Simple debug endpoint to view all URLs
- React frontend with API integration

---

## Tech Stack

Frontend:
- React
- Axios

Backend:
- Flask
- SQLite
- Flask-CORS

---

## Project Structure

backend/
- app.py
- db.py
- utils.py
- database.db

frontend/
- src/
  - App.js

---

## Backend Setup

### Install dependencies
pip install flask flask-cors

### Run backend
python app.py

Backend runs at:
http://127.0.0.1:5000

---

## API Endpoints

### Shorten URL
POST /shorten

Request:
{
  "long_url": "https://google.com"
}

Response:
{
  "short_url": "http://127.0.0.1:5000/abc123"
}

---

### Redirect URL
GET /<short_code>

Redirects to the original long URL.

---

### Debug Endpoint
GET /debug

Returns all stored URLs in the database.

---

## Frontend Setup

Install dependencies:
npm install axios

Run frontend:
npm start

Frontend runs at:
http://localhost:3000

---

## How It Works

1. User enters a URL in the frontend
2. React sends request to Flask backend
3. Backend generates a short code
4. Data is stored in SQLite database
5. Short URL is returned to frontend
6. Clicking short URL redirects to original URL

---

## Example

Input:
https://google.com

Output:
http://127.0.0.1:5000/abc123

---

## Future Improvements

- Click tracking
- Custom short URLs
- Link expiration
- Dashboard for managing links
- User authentication

---

## Author

Simple URL shortener project built for learning full-stack development using React and Flask.
