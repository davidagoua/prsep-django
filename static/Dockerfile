FROM bitnami/php-fpm:8.2

RUN apt-get update && apt-get install -y \
    git \
    curl \

RUN docker-php-ext-install pdo pdo_pgsql 



WORKDIR /app
COPY . .

EXPOSE 9000

CMD ["php-fpm"]
