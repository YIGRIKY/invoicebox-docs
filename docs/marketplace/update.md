---
layout: default
nav_order: 1
title: Обновление точки продаж
parent: "Маркетплейс"
---

# Обновление точки продаж

Для обновления точки продаж, необходимо вызвать следующий метод API:

- метод: `POST`
- ресурс: `/v3/marketplace/api/shop/:id` - где `:id` это идентификатор точки продаж
- тело запроса - объект [UpdateShopRequest](#updateshoprequest)
- тело ответа - объект [ShopResponse](#shopresponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса</summary>
<section markdown="1">
``` json
POST /v3/marketplace/api/shop
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
Accept: application/json
{
  "description": "Это наш тестовый магазин",
  "notificationEmail": "test@test.me",
  "jivositeId": "321314123123",
  "yandexMetrikaId": 432141251234,
  "deliveryInfo": "Когда хотим, тогда и доставляем",
  "registrationAddress": "Санкт-Петербург, улица Рубинштейна, дом 12",
  "lat": 59.931228,
  "lon": 30.345557,
  "brandId": 123,
  "merchantId": "01771534-1a57-f184-dee3-ebeb91dded76",
  "externalUpdate": true
}
```
</section>
</details>

## UpdateShopRequest

| Свойство            | Обязательное | Тип              | Описание                                                                                                  | Пример значения                                                                       |
|---------------------|--------------|------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| description         | нет          | string(2000)     | Описание магазина                                                                                         | `Это наш первый тестовый магазин`                                                     |
| seoTitle            | нет          | string(500)      | Название магазина под SEO                                                                                 | `Магазин`                                                                             |
| seoDescription      | нет          | string(500)      | Описание магазина под SEO                                                                                 | `Это наш первый тестовый магазин`                                                     |
| categoryId          | нет          | int              |                                                                                                           | 12                                                                                    |
| shopDeliveryId      | нет          | int              |                                                                                                           | 12                                                                                    |
| shopUrl             | нет          | string(64)       | Ссылка на магазин                                                                                         | `https://1694158899.expressclient.ru`                                                 |
| minOrderSum         | нет          | float            | Минимальная сумма заказа                                                                                  | 99.99                                                                                 |
| notificationEmail   | нет          | string(500)      | Email для отправки уведомлений                                                                            | `test@test.me`                                                                        |
| defaultPriceId      | нет          | int              |                                                                                                           | 12                                                                                    |
| imageId             | нет          | int              |                                                                                                           | 12                                                                                    |
| ogImageId           | нет          | int              |                                                                                                           | 12                                                                                    |
| jivositeId          | нет          | string(256)      |                                                                                                           | `4234123123`                                                                          |
| orderFlow           | нет          | string(256) enum |                                                                                                           | `manual`                                                                              |
| yandexMetrikaId     | нет          | int              |                                                                                                           | 12332134222                                                                           |
| deliveryInfo        | нет          | string(1000)     | Описание доставки                                                                                         | `Не доставляем по выходным и праздникам`                                              |
| type                | нет          | string(50) enum  | Тип магазина                                                                                              | `shop`                                                                                |
| registrationAddress | нет          | string(200)      | Адрес магазина                                                                                            | `Санкт-Петербург, улица Рубинштейна, дом 12`                                          |
| lat                 | нет          | float            | Широта нахождения магазина                                                                                | 59.931228                                                                             |
| lon                 | нет          | float            | Долгота нахождения магазина                                                                               | 30.345557                                                                             |
| brandId             | нет          | int              | Идентификатор магазина с типом brand                                                                      | 123                                                                                   |
| merchantId          | нет          | string(36)       | Идентификатор магазина Invoicebox, работает только в связвке с полем externalUpdate                       | `01771534-1a57-f184-dee3-ebeb91dded76`                                                |
| externalUpdate      | нет          | bool             | Флаг, необходимо ли запросить данные из магазина Invoicebox, работает только в связвке с полем merchantId | true - получить данные из магазина по идентификатору merchantId, по-умолчанию - false |


## ShopResponse

Повторяет свойства объекта [CreateShopRequest](#createshoprequest):

