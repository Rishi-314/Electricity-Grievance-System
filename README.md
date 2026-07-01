# ⚡ Electricity Grievance System

**Electricity Grievance System** is a web-based platform designed to streamline the process of registering, tracking, and resolving electricity-related complaints. It provides a transparent and efficient interface for consumers to report issues like power outages, billing errors, or voltage fluctuations, and for authorities to manage and resolve them promptly.

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Project-7c3aed?style=for-the-badge&logo=vercel&logoColor=white)](https://electricity-grievance-system.vercel.app/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

---

## 🚀 Features

- **Consumer Complaint Portal:** Easy-to-use interface for citizens to submit new grievances with relevant details.
- **Grievance Tracking:** Users can track the status of their submitted complaints.
- **Admin/Authority Dashboard:** A backend interface for officials to view, categorize, and update the status of complaints.
- **Database Integration:** Securely stores all grievance records and user data.
- **Web-Based Access:** Accessible from any device with a browser, ensuring a wide reach.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap (implied by structure)
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Deployment:** Vercel

## 📁 Project Structure

```
Electricity-Grievance-System/
├── Static/                 # Static files (CSS, JavaScript, Images)
├── templates/              # HTML templates for the web interface
│   ├── index.html          # Homepage
│   ├── register.html       # User registration
│   ├── login.html          # User login
│   └── ...                 # Other pages (dashboard, track, admin)
├── instance/               # Database instance folder
│   └── site.db             # SQLite database file (for local development)
├── app.py                  # Main Flask application entry point
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚧 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- **Python 3.8** or higher
- **pip** (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rishi-314/Electricity-Grievance-System.git
   cd Electricity-Grievance-System
   ```

2. **Set up a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present, install Flask and your chosen database driver: `pip install flask flask-sqlalchemy`)*

4. **Run the application**
   ```bash
   python app.py
   ```

   The application will start on `http://127.0.0.1:5000` by default.

## 🗄️ Database Setup

The project uses **SQLite** by default for local development. The database file (`site.db` or similar) will be created automatically in the `instance/` folder when you run the application for the first time.

To use **PostgreSQL** in production:
1. Install `psycopg2-binary`: `pip install psycopg2-binary`
2. Update your database URI in the application's configuration (e.g., `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'`).

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📧 Contact

Rishikesh Bhagat - [rishikesh2048x@gmail.com](mailto:rishikesh2048x@gmail.com)

Project Link: [https://github.com/Rishi-314/Electricity-Grievance-System](https://github.com/Rishi-314/Electricity-Grievance-System)

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)
