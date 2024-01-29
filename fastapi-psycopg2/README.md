### Fastapi + sqlalchemy implementation
#### Python
- `pip install -r requirements.txt`
- `uvicorn api:app --port 8081 --reload`

#### Docker
- `docker build -t fastapi-psycopg2 .`
- `docker run -d -p 8081:8081 fastapi-psycopg2`