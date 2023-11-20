# 1) Создаем сеть в сервисе vpc

![image](Pictures/vpc.png)


## Заходим в сабнетс и создаем три подсети.

1-ю приватную

![image](Pictures/vpc2.png)

2-ю публичную в первой зоне

![image](Pictures/subnet1.png)

3-ю публичную в второй зоне

![image](Pictures/subnet3.png)

## Ограничиваем доступ приватной сети через ACL

![image](Pictures/acl_for_privetvpc.png)

# 2) Создаем security group web-sg

![image](Pictures/security_web-sg.png)
![image](Pictures/security_web-sg2.png)

# 3) Имеем уже сгенерерованный ключ.

# 4) Coздание 2-х публичных инстансов в разных сетях и учтановка nginx.

1-ый
![image](Pictures/pub_instance1.png)

2-ой
![image](Pictures/pub_instance2.png)

## Теперь создаем для публичных сетей internet gateways & route tables

Создание internet gateways

![image](Pictures/internet_gateaway.png)

Создание route tables

![image](Pictures/route_tables.png)
![image](Pictures/route_tables2.png)
![image](Pictures/route_tables3.png)

## Подключаемся к публичным инстансам, устанавливаем nginx и заходим через браузер по ip адресу.

![image](Pictures/connect_public_inst.png)
![image](connect_pPictures/ub_browser.png)

# 5) ЕLB

## Создание таргет группы

![image](Pictures/creating_targetgroup.png)
![image](Pictures/creating_targetgroup2.png)

### Настраеваем Healthcheck с минимальным интервалом

![image](Pictures/healthcheck.png)

### Добавляем инстансы

![image](Pictures/creating_TG3.png)

## Создание ELB

Выбираем Application load balancer

![image](Pictures/creatingLB.png)

Выбираем нашу сеть и публичные инстансы

![image](Pictures/creatingLB2.png)

Создаем security group для ELB

![image](Pictures/creatingLB3.png)

Добавляем security group в ELB

![image](Pictures/creatingLB4.png)

Добавляем security group ELB в security group web-sg для получения поступа ELB  к инстансам.

![image](Pictures/add_securLB_to_web-sg.png)

Подключаемся по DNS ELB через браузер

![image](Pictures/connect_toDNS_LB.png)

Останавливаем один из инстансов и проверяем работоспособность

![image](Pictures/stop1instance.png)
![image](Pictures/connect_toDNS_LB.png)

## Все работает!

# 6) RDS

## Создание RDS

![image](Pictures/creating_RDS.png)
![image](Pictures/creatingRDS2.png)
![image](Pictures/creatingRDS3.png)
![image](Pictures/creatingRDS4.png)
![image](Pictures/creatingRDS5.png)
![image](Pictures/creatingRDS6.png)

## И Security group для RDS.

Прописываем порт RDS и добавляем группу web-sg

![image](Pictures/securG_forRDS.png)

Добавляем Security group в RDS

![image](Pictures/add_sedyrityG_for_RDS.png)

Подключаемся к публичному инстансу с помошью команды "ssh -i "keypair.pem" ubuntu@51.20.134.229"
Ставим клиента postgres с помошью команды "sudo apt-get install postgressql-client"

Подключаемся к postgres

![image](Pictures/connect_to_postgres.png)

Проверяем возможность подключения с локальной машины
Ставим клиента postgres и подключаемся.

![image](Pictures/connect_to_postgres_LM.png)

Подключение не удалось.

# 7) ElastiCache

## Создаем ElastiCache Redis

![image](Pictures/EC_Redis.png)
![image](Pictures/EC_Redis2.png)

Ставим Редис клиент на инстанс с помошью команды "sudo apt install redis-tools"

Делаем Security group для Redis

![image](Pictures/RedisSG.png)

Добавляем Новую группу в редис

Подключаемся

![image](Pictures/connect_redis.png)

Попытка аналогичного подключения с локальной машины не увенчалась успехом.

## Создаем ElastiCache memcache

![image](Pictures/create_memC.png)

Создаем Security group для memcache

![image](Pictures/SGmemcache.png)

Добавляем нашу группу в memcache

Подключаемся

![image](Pictures/connectmem.png)

С локальной машины подключится не удалось.

# 8) CloudFront Distribution & s3

Находим сервис CloudFront в амазоне, создаем его по умолчанию с домменым именем нашего с3 баскета

![image](Pictures/CFcreate.png)

## S3

При создания баскета делаем его не публичным

![image](Pictures/s3perm.png)

Cоздаем 100 файлов на локальной машине с помошью скрипта
``` 
for ((i = 1; i <= 100; i++)); do
  FILE_SIZE=$((RANDOM % 512 + 1))

  FILE_NAME="file_${i}.txt"

 
  dd if=/dev/urandom of="${FILE_NAME}" bs=1024 count="${FILE_SIZE}"

done
```
Загружаем их на нашь баскет.

Создаем правила хранения файлов

1 правило

никому не рассказывать о .....
по истечению 30 дней отправлять в ледник

![image](Pictures/rule1.png)

2 правило

по истечению 180 дней удалять файлы из глейсера

![image](Pictures/rule2.png)