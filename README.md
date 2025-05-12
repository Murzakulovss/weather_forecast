# 🌤️ Weather Forecast API

A simple REST API service for fetching weather forecasts and allowing users to save their favorite cities.

---

## 🚀 Tech Stack

- **Python 3.11**
- **Django 5.2**
- **Django REST Framework**
- **SimpleJWT (Authentication)**
- **PostgreSQL**
- **Docker & Docker Compose**
- **drf-spectacular (Swagger docs)**

---

## ⚙️ Installation & Run

```bash
# 1. Clone the project
git clone https://github.com/yourname/weather_forecast.git
cd weather_forecast

# 2. Create a .env file in the project root with the following content
echo "
SECRET_KEY=your_secret_key
WEATHER_API_KEY=your_openweathermap_api_key
DB_NAME=weather_db
DB_USER=weather_user
DB_PASSWORD=secure_password
DB_HOST=db
DB_PORT=5432
" > .env

# 3. Run the project using Docker
docker compose up --build
