# Chappy

## Project structure

### Backend

`cd backend && python3 -m uvicorn chappy_backend.main:app --reload --port 5050`

### Frontend

`cd frontend && python3 -m uvicorn app:app --reload --port 6050`
UserModel

- name
- location
- sessions = []

UserLoginSchema - /login

- name
- password

auto-face-crop

- backend
- Dockerfile
- frontend
- Dockerfile
- ml_service
- Dockerfile
- docs
- scehams
  . architecture
  . DB

docker-compose.yaml

MongoDB - Atlas
