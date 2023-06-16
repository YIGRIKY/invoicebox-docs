---
layout: default
nav_order: 10
title: "PHP SDK"
parent: "SDK"
---

# Описание SDK

PHP SDK является готовой библиотекой для серверного взаимодействия с API Инвойсбокс. Библиотека поддерживает
все необходимые методы API для организации приёма платежей.

## Требования

PHP 7.4+ (или более поздняя версия)

## Установка с помощью Composer

1. Установите Composer, менеджер пакетов
2. В консоле выполните следующую команду:

```
composer require invoicebox/invoicebox-sdk-php
```

Пропишите в файле composer.json вашего проекта:

1. Добавьте строку "invoicebox/invoicebox-sdk-php": "^1.0" в список зависимостей вашего проекта в файле composer.json

```
   "require": {
        "php": ">=7.4",
        "invoicebox/invoicebox-sdk-php": "^1.0"
```

2. Обновите зависимости вашего проекта. В консоле, в папке с файлом composer.json выполните следующую команду:

```
composer update
```

3. Подготовьте код своего проекта, чтобы активировать автоматическую загрузку зависимостей:
 
```
require __DIR__ . '/vendor/autoload.php';
```

## Установка SDK вручную

1. Скачайте архив [Инвойсбокс PHP SDK](https://github.com/InvoiceBox/invoicebox-sdk-php) и распакуйте его в необходимую папку вашего проекта.

2. Подготовьте код своего проекта, чтобы активировать автоматическую загрузку зависимостей:
 
```
require __DIR__ . '/vendor/autoload.php';
```


---

[Проект на github](https://github.com/InvoiceBox/invoicebox-sdk-php)
