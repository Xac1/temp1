FROM alpine

# Install dependencies
RUN apk update && \
    apk add python3 py3-pip mariadb-connector-c-dev && \
    pip3 install  --break-system-packages pymysql cryptography==3.4.8 python-dotenv && \
    apk add --no-cache mariadb-client && \
    apk add python3 -m pip install mysql-connector-python

# Copy source code to image
COPY ./src /app
# Set working directory
WORKDIR /app

# Run the application
CMD ["python3", "main.py"]