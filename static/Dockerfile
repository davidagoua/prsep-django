FROM php:8.1-apache

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && docker-php-ext-install pdo pdo_pgsql

RUN chmod -R 755 /var/www/html

COPY . /var/www/html

EXPOSE 80

