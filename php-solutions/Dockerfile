FROM php:5.5.31-cli
RUN apt-get update && \
    apt-get install -y zlibc zlib1g zlib1g-dev git && \
    docker-php-ext-install zip && \
    docker-php-ext-install bcmath && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer && \
    composer global require "phpunit/phpunit=4.8.*" && \
    ln -s ~/.composer/vendor/bin/phpunit /usr/bin/


