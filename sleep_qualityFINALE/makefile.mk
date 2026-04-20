.PHONY: setup train test run clean

setup:
	pip install -r requirements.txt
	python ml/generate_dataset.py

train:
	python ml/train_professional.py

test:
	pytest tests/ -v

run:
	uvicorn backend.main:app --reload

docker-build:
	docker build -t sleep-quality-app .

docker-run:
	docker run -p 8000:8000 sleep-quality-app

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache