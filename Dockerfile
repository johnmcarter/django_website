FROM python:3.9

# Install dependencies
# Apt dependencies installed first since they change less frequently
RUN apt update && \
    apt install -y rustc
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

# Copy the app
COPY jjp-website /app/

WORKDIR /app

EXPOSE 80

CMD ["daphne", "jjpsite.asgi:application", "-b", "0.0.0.0", "-p", "80"]
