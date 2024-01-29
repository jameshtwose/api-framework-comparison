### Fastapi + sqlalchemy implementation
#### Python
- `pip install -r requirements.txt`
- `uvicorn api:app --port 8080 --reload`

#### Docker
- `docker build -t fastapi-sqlalchemy .`
- `docker run -d -p 8080:8080 fastapi-sqlalchemy`