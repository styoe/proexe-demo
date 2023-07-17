#!/bin/bash

if [[ -z "${ENV}" ]]; then
  export ENV=development
fi

case $1 in
    build)
      docker-compose up --build
      ;;
    manage)
      docker exec -t proexe-demo_web_1 sh -c "/usr/local/bin/python manage.py $2 $3"
      ;;
    *)
      docker-compose up
      ;;
esac