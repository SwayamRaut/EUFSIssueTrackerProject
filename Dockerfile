FROM python:3.13

WORKDIR /app

#install backend dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

EXPOSE 5000

#The IP 127.0.0.1 is interpreted in the container as only accepting traffic within the container
#so we need to run it on IP 0.0.0.0 which listens on every network interface available
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "5000"]