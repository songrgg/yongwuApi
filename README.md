## 启动mysql container
docker-compose up -d mysql


## 管理mysql container
docker run -it --rm \
--link yongwuapi_mysql_1:mysql \
mysql:5.7.7 sh -c '\
exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" \
-P"$MYSQL_PORT_3306_TCP_PORT" \
-uroot \
-p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'


## 建库
docker-compose run web python yongwu-api/module.py
