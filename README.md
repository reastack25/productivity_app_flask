# productivity_app_flask
# 📝 Flask Notes API (Session-Based Auth)

## 📌 Project Description

This project is a secure RESTful API built using Flask. It implements full user authentication using **session-based authentication** and allows users to manage a personal notes resource.

Each user can:

* Sign up and log in securely
* Create, view, update, and delete their own notes
* Access only their own data (strict access control)
* View notes with pagination support

This API is designed to integrate with a frontend client that handles authentication flows.

---

## ⚙️ Tech Stack

* Python 3.8+
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-Bcrypt
* SQLite (default DB)
* Postman (for testing)

---

## 📁 Project Structure

```
server/
│
├── app.py
├── config.py
├── extensions.py
│
├── models/
│   ├── user.py
│   └── note.py
│
├── routes/
│   ├── auth_routes.py
│   └── note_routes.py
│
├── seed.py
├── migrations/
└── Pipfile
```

---

## 🚀 Installation Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install dependencies

```
pipenv install
pipenv shell
```

### 3. Set environment variables

Mac/Linux:

```
export FLASK_APP=app.py
```

Windows:

```
set FLASK_APP=app.py
```

---

## 🗄️ Database Setup

### Initialize migrations

```
flask db init
```

### Generate migration

```
flask db migrate -m "initial migration"
```

### Apply migration

```
flask db upgrade
```

---

## 🌱 Seed the Database

```
python seed.py
```

Creates:

* Sample user
* Sample notes

---

## ▶️ Run the Application

```
flask run
```

Server will run on:

```
http://127.0.0.1:5000
```

---

## 🔐 Authentication

This API uses **session-based authentication**:

* Login stores `user_id` in session
* Session persists via cookies
* Logout clears session

---

## 📡 API Endpoints

### 🔑 Auth Routes

#### Signup

```
POST /signup
```

Creates a new user.

#### Login

```
POST /login
```

Logs in a user and starts a session.

#### Logout

```
DELETE /logout
```

Clears session.

#### Check Session

```
GET /me
```
Returns current logged-in user.

---

### 📝 Notes Routes (Protected)

⚠️ All routes require authentication

#### Get Notes (Paginated)

```
GET /notes?page=1
```

#### Create Note

```
POST /notes
```

#### Update Note

```
PATCH /notes/<id>
```

#### Delete Note

```
DELETE /notes/<id>
```

---

## 🔒 Security Features

* Passwords hashed using Bcrypt
* Session-based authentication
* Route protection with login checks
* Users can only access their own data
* Unauthorized access returns proper HTTP status codes

---

## 🧪 Testing

Use Postman to test endpoints:

Recommended flow:

1. Signup
2. Login
3. Access `/me`
4. Create notes
5. Fetch notes
6. Update/Delete notes
7. Logout

Ensure cookies are enabled in Postman for session persistence.

---

## ⚠️ Common Issues

* Not logged in → Check cookies in Postman
* No data returned → Ensure database is seeded
* Migration errors → Re-run migrate and upgrade

---

## 📌 Future Improvements

* Add JWT authentication
* Add search and filtering
* Add categories/tags for notes
* Deploy to cloud (Render/Heroku)

---

## 👨‍💻 Author

Backend developed as part of a Flask API lab project.
