up:
	docker-compose up -d

stop:
	docker-compose stop

build:
	docker-compose up --build -d

install:
	docker-compose run grunt sh -c 'npm install'

grunt-shell:
	docker-compose exec grunt bash

compile:
	docker-compose exec grunt grunt build

compileJS:
	docker-compose exec grunt grunt buildJS

log:
	docker-compose logs -f grunt

shell:
	docker-compose exec webserver bash

down:
	docker-compose down

deploy:
	docker-compose exec webserver rsync -avhz --exclude loginattempts.txt --exclude api/user --exclude visitenkarten  --exclude quiz --exclude logo --exclude log/*.log --exclude log/*.txt --exclude persistent --exclude youtubedownloader --exclude tmp /var/www/html/dist/ tom@sharepicgenerator.de:/var/www/html --delete

get-config:
    docker-compose exec webserver rsync rsync tom@sharepicgenerator.de:/var/www/html/ini/* ini/

get-log:
	docker-compose exec webserver rsync tom@sharepicgenerator.de:/var/www/html/log/log.log dist/log.log

get-passwords:
	docker-compose exec webserver rsync tom@sharepicgenerator.de:/var/www/html/passwords.php dist/passwords.php

tests:
	docker-compose exec webserver python tests/test-federal.py
	docker-compose exec webserver python tests/test-bayern.py
	docker-compose exec webserver python tests/test-vintage.py

test-federal:
	docker-compose exec webserver python tests/test-federal.py

test-vintage:
	docker-compose exec webserver python tests/test-vintage.py

test-bayern:
	docker-compose exec webserver python tests/test-bayern.py

test-live:
	docker-compose exec webserver python tests/test-live.py

