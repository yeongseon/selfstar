# selfstar

## 구조

```
.
├── backend/   # FastAPI 백엔드 (헬스체크, 사용자 API, MySQL, Docker Compose)
├── frontend/  # React (Vite) 프론트엔드 - 백엔드 헬스 체크 예제
└── ai/        # 최소 학습/서빙/MLflow 구조
```

### backend
- FastAPI 앱 + `/health`, `/users` (MySQL 연동)
- async SQLAlchemy + `asyncmy`
- Dockerfile 및 `docker-compose.yml` (MySQL 8 + 백엔드 동시 실행)

### frontend
- Vite + React
- 백엔드 `/health` 호출 예제 컴포넌트 포함

### ai
- `training/train.py` : MLflow 간단 로깅 예시
- `notebooks/00_mlflow_init.ipynb` : 노트북 기반 MLflow 런
- `serving/fastapi_app/` : 서빙용 FastAPI 자리
- 대용량 데이터는 저장소에 포함하지 않고 `data/samples/` 만 예시로 허용

## 빠른 시작

1) 백엔드 개발 (로컬):
```
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2) Docker (백엔드 + MySQL):
```
docker compose up --build -d
```

3) 프론트엔드 개발:
```
cd frontend
npm install
npm run dev
```

4) MLflow 테스트:
```
cd ai
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python training/train.py
```

## 로드맵 (요약)
- 백엔드: Alembic 마이그레이션, 인증, 테스트 강화
- 프론트: 사용자 API 연동 예제
- AI: 모델 서빙 확장, 실험 관리 고도화

---
최소 기능 구조가 준비되었습니다. 필요 시 추가 요구를 이어주세요.