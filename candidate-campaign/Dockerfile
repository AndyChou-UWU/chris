FROM node:22-bookworm-slim AS frontend-build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY vite.config.js ./
COPY webllm ./webllm
RUN npm run build

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLET_SERVER_IP=0.0.0.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY assets/campaign.mp4 assets/candidate.jpg assets/carousel-1.png assets/carousel-2.png assets/carousel-3.png ./assets/
COPY --from=frontend-build /app/assets/webllm ./assets/webllm

EXPOSE 7860

CMD ["python", "main.py"]
