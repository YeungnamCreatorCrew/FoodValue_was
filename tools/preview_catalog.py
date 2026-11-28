"""Run the 20-item preview against local DB_* without changing .env's shared DATABASE_URL."""
import os

from dotenv import load_dotenv
from sqlalchemy import URL


def main():
    load_dotenv('.env')
    url = URL.create('postgresql+psycopg', username=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                     host='127.0.0.1', port=int(os.getenv('DB_PORT', '5432')), database=os.environ['DB_NAME'])
    os.environ['DATABASE_URL'] = url.render_as_string(hide_password=False)
    os.environ['CORS_ORIGINS'] = 'http://localhost:3000,http://localhost:3001,http://127.0.0.1:3001'
    import uvicorn
    uvicorn.run('app.main:app', host='127.0.0.1', port=8001)


if __name__ == '__main__':
    main()
