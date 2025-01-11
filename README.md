# CSE Logical Bug Detection System - Server

## Description

This is the server-side application for the **CSE Logical Bug Detection System**

## System eequirements

- Python 3.10 or above
- Docker
- Docker Compose

## Run locally

1. **Create and activate a virtual environment**:

```bash
python3 -m venv venv
source ./venv/bin/activate  # (Windows: .\venv\Scripts\activate)
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the application with Docker**:

- Build the Docker image:

  ```bash
  docker-compose build
  ```

- Start the container:

  ```bash
  docker-compose up -d
  ```

- Stop the container:

  ```bash
  docker-compose down
  ```

Or run manually: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Contributors: `tannat-team`

- Le Duy Anh
- Vo Nguyen Doan Thao
- Nguyen Tran Bao Ngoc
