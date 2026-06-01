# Stateless Lego Server (REST API Fundamentals)

A modern, high-performance, and lightweight stateless backend application built using Python and FastAPI. This project implements the core communication layer of the web by creating a local server, defining standard `GET` and `POST` routes, and handling structured JSON payloads.

---

## 🚀 Features

- High-performance local server built on ASGI architecture.
- RESTful API design using clean, noun-based endpoints (e.g., `/toys`).
- Supports core HTTP methods: `GET` and `POST`.
- Automatic data validation using Pydantic `BaseModel`.
- Built-in interactive API documentation (Swagger UI / OpenAPI).

---

## 📊 HTTP Method Diagnostic Matrix

| Method | Action | Data Location | Safe | Idempotent | Description |
|--------|--------|--------------|------|------------|-------------|
| GET    | Read   | URL/Query    | Yes  | Yes        | Retrieves data without modifying server state |
| POST   | Create | JSON Body    | No   | No         | Creates new resource and modifies server state |

---

## 🛠️ Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn (ASGI Server)
- Pydantic (Data Validation)
- Swagger UI (Auto Documentation)

---

## 💻 Getting Started

### Prerequisites

Make sure you have Python installed:

```bash
python --version
````

---

### Installation

Install required dependencies:

```bash
pip install fastapi uvicorn
```

---

### Project Setup

Create a file named:

```text
main.py
```

Paste your FastAPI application code inside it.

---

### Running the Server

Start the development server:

```bash
uvicorn main:app --reload
```

Your server will run at:

```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

---

### 1. Get All Toys

* Route: `GET /toys`
* Description: Fetches all toys from in-memory storage.
* Status: `200 OK`

#### Response Example

```json
{
  "status": "success",
  "toys": [
    {
      "id": 1,
      "name": "Lego Castle",
      "color": "Gray"
    },
    {
      "id": 2,
      "name": "Race Car",
      "color": "Red"
    }
  ]
}
```

---

### 2. Create a New Toy

* Route: `POST /toys`
* Description: Adds a new toy after validating input data.
* Status: `201 Created`

#### Request Body Example

```json
{
  "id": 3,
  "name": "Spaceship",
  "color": "Blue"
}
```

---

## 🗺️ Interactive API Docs

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

You can:

* Test APIs directly in browser
* View request/response structure
* Debug endpoints in real-time

---

## 📌 Notes

* This project is for learning REST API fundamentals.
* Data is stored in-memory (not persistent database).
* Ideal for beginners in FastAPI backend development.


