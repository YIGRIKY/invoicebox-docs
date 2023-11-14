---
layout: default
nav_order: 10
title: "PHP SDK"
parent: "SDK"
grand_parent: "Приём платежей"
date: 2023-10-25 00:00:00 +0300
---

# Описание SDK

![PHP](/assets/images/sdk/php.svg){: .img-right}

PHP SDK является готовой библиотекой для серверного взаимодействия с Инвойсбокс API. Библиотека поддерживает
все необходимые методы API для организации приёма платежей.

## Требования

PHP 7.4+ (или более поздняя версия)

## Установка с помощью Composer

1. Установите Composer, менеджер пакетов
2. В консоле выполните следующую команду:

```
composer require invoicebox/sdk-php
```

Пропишите в файле composer.json вашего проекта:

1. Добавьте строку "invoicebox/sdk-php": "^1.0" в список зависимостей вашего проекта в файле composer.json

```
   "require": {
        "php": ">=7.4",
        "invoicebox/sdk-php": "^1.0"
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

1. Скачайте архив [Инвойсбокс PHP SDK](https://github.com/invoicebox/sdk-php) и распакуйте его в необходимую папку вашего проекта.

2. Подготовьте код своего проекта, чтобы активировать автоматическую загрузку зависимостей:
 
```
require __DIR__ . '/vendor/autoload.php';
```

## Пример создания заказа

```
$client = new InvoiceboxClient(
    '*auth токен*',
    'v3',
    null,
    HttpClient::create(),
);

/**
 * Проверка авторизации (необязательный шаг, для тестирования наличия доступа)
 */
$result = $client->checkAuth();

if ($result->getUserId()) {
    echo "Успешная авторизация \n";
}


// Покупатель юр.лицо
//$customer = new LegalCustomer(
//    'OOO TEST',
//    '78121111111',
//    'test@test.test',
//    '7804445210',
//    '123321, Улица, 1, 1'
//);

// Покупатель физ.лицо
$customer = new PrivateCustomer(
    'name',
    '78121111111',
    'test@test.test',
);


$basketItems[] = new BasketItem(
    "12312", /* Идентификатор заказа (необходим для создания возврата) */
    'Тест',
    'шт.',
    '796',
    1.0,
    1000.00,
    1000,
    1000.00,
    0,
    VatCode::VATNONE,
    BasketItemType::COMMODITY,
    PaymentType::FULL_PREPAYMENT
);

$request = new CreateOrderRequest(
    'Описание заказа',
    'ffffffff-ffff-ffff-ffff-ffffffffffff', // id магазина
    strval(random_int(1,2000)),
    1000.00,
    0,
    'RUB',
    new \DateTime('tomorrow'),
    $basketItems,

);

$result = $client->createOrder($request);

if ($result->getPaymentUrl()) {
    echo sprintf('Заказ успешно создан - ссылка на оплату - %s', $result->getPaymentUrl());
}

/* Redirect to: $result->getPaymentUrl() */

```


---

[Проект на github](https://github.com/invoicebox/sdk-php){: .btn .mb-4 .mb-md-0 } [Проект на packagist](https://packagist.org/packages/invoicebox/sdk-php){: .btn .mb-4 .mb-md-0 }
