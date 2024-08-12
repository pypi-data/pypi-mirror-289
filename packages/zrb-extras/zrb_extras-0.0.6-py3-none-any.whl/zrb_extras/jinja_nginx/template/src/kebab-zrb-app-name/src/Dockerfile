FROM nginx:1.25.0-bullseye

# Install required packages
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx python3-pip python-is-python3 && \
    pip install jinja2

COPY ./etc/letsencrypt /etc/letsencrypt
COPY ./etc/generate_config.py /etc/generate_config.py
COPY ./etc/start.d /etc/start.d

RUN mkdir -p /etc/.well-known && \
    echo '<h1>Well known</h1>' > /etc/.well-known/index.html && \

# Expose ports for HTTP and HTTPS traffic
EXPOSE 80 443

# Start Nginx
CMD /bin/bash -c 'python /etc/generate_config.py && nginx -g "daemon off;"'

