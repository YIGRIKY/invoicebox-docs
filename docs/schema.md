---
layout: default
nav_order: 4
title: "Схема взаимодействия"
---

![Схема взаимодействия](/assets/images/api-invoicebox.png)

1. Клиент создает заказ на сайте Магазина
1. Магазин создает в системе заказ через API
1. Система возвращает ссылку на оплату заказа
1. Магазин перенаправляет клиента по этой ссылке
1. Клиент заполняет форму своими данными на странице оплаты
1. Клиент оплачивает заказ
1. Система перенаправляет клиента обратно на сайт Магазина   
1. Система оповещает Магазина об успешной оплате заказа на специальный URL

[](https://sequencediagram.org/index.html?presentationMode=readOnly#initialData=C4S2BsFMAJEIQRREEKwggeEEAwg1BMIIdhBWA4QZgfCCAsIIoJwgggiCBCIBroPIg050AggAoCS0bAdgG4D2IAMaQAQnwAeAKACGAV2B8usgLYAjSACdJMwQo3RA+CAFAXCCBhEED8IKkqJA3CCAZEEkAHaRtCCQzrsGiAcEFSBmEFQsXEBeECcXNw9pL05eAWExcWhtIzNLa3sAWgA+P0DgkIAuOAIsIlRESmgcYyDJPKDQnO5+IVEJYsAkEEBpECwCDGhkSuJ0clLykLpq1FqcSRb49vEchoLiwAwQEhDKXEAREFxaygJAARBp2fRcBnJum1roEPQCcxsrU3qAxpCc1IsrWztigZEMdEA9zMdUBgbKDcIh7uhnn9AGwgIVMgDkQBiUCGTQBiIG8ful-gAeImZHLZBZtRJdHD4YhkKg0OGMRHWFEEUjQXYnQikSQEv5ZClxKkdaCAPBBWah5iKEhJviZfhkAYZgaDUODIdDJnDzIrCTZ6A8GKhSFU0PlQtLKXLlrkPmtoIBiEAwiCIBGQ2th0AIgEYQaCmcjmRCACRAQhyfay4TUgtKgA)


Возможные статусы заказов:
 - `created` - Создан, но еще не оплачен
 - `completed` - Оплачен
 - `expired` - Просрочен (expirationDate больше чем текущее время)
 - `canceled` - Отменен магазином до оплаты

[Читать далее](/docs/order){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
