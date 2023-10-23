---
layout: default
nav_order: 5
title: "Создание отгрузки"
parent: "Работа с заказом"
grand_parent: "Приём платежей"
---

# Создание отгрузки

Для создания отгрузки, необходимо вызвать следующий метод API:

- метод: `POST`
- ресурс: `/v3/billing/api/order/shipment`
- тело запроса - объект [CreateShipmentRequest](#createshipmentrequest)
- тело ответа - объект [ShipmentResponse](#shipmentresponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса</summary>
<section markdown="1">
``` json
POST /v3/billing/api/order/shipment
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
Accept: application/json
{
    "orderId": "0187c6db-1637-c1ca-bef7-f6706799c41e",
    "basketItems": [
        {
            "sku": "01GZ3DP5HADMSBAXRKVCES5FJX",
            "name": "iPhone 5s",
            "measure": "шт",
            "measureCode": "796",
            "originCountry": "Россия",
            "originCountryCode": "643",
            "grossWeight": 1010.55,
            "netWeight": 1000.66,
            "quantity": 1,
            "amount": 123.96,
            "amountWoVat": 103.3,
            "totalAmount": 123.96,
            "totalVatAmount": 20.66,
            "vatCode": "RUS_VAT20",
            "type": "commodity",
            "paymentType": "full_prepayment"
        }
    ]
}
```
</section>
</details>

## CreateShipmentRequest

| Свойство    | Обязательное | Тип                                | Описание       | Пример значения                        |
|-------------|--------------|------------------------------------|----------------|----------------------------------------|
| orderId     | да           | string(36)                         | Id заказа      | `01771534-1a57-f184-dee3-ebeb91dded75` |
| basketItems | да           | array of [BasketItem](#basketitem) | Корзина заказа |                                        |

## ShipmentResponse

Повторяет свойства объекта [CreateShipmentRequest](#createshipmentrequest) с дополнительными свойствами:

| Свойство   | Обязательное | Тип        | Описание                                    | Пример значения                         |
|------------|--------------|------------|---------------------------------------------|-----------------------------------------|
| id         | да           | int        | Идентификатор отгрузки в системе Инвойсбокс | `2`                                     |
| merchantId | да           | string(36) | Идентификатор магазина                      | `01771534-1a57-f184-dee3-ebeb91dded76 ` |

## BasketItem

Корзина заказа. Пожалуйста, внимательно ознакомьтесь с требованиями по [заполнению наименования номенклатуры](/docs/merchant/fz54).

| Свойство          | Обязательное | Тип                | Описание                                                                                                                                          |
|-------------------|--------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| sku               | да           | string(500)        | Артикул, например: `5fe0adcfa7fb4`                                                                                                                |
| name              | да           | string(500)        | Наименование, например `Бронирование номера`                                                                                                      |
| groupName         | нет          | string(500)        | Наименование группы позиций заказа, используется для формирования отчетных документов                                                             |
| measure           | да           | string(10)         | Единица измерения (для России - по [ОКЕИ](/docs/dictionary/okei/)), например `шт.`                                                                |
| measureCode       | да           | string(4)          | Код единицы измерения (для России - по [ОКЕИ](/docs/dictionary/okei/)), например `796`                                                            |
| originCountry     | нет          | string(20)         | Страна происхождения товара, например, `Россия`                                                                                                   |
| originCountryCode | нет          | string(4)          | Код страны происхождения, например, Россия `643`                                                                                                  |
| grossWeight       | нет          | float              | Вес брутто, например `125.45`                                                                                                                     |
| netWeight         | нет          | float              | Вес нетто, например `125.45`                                                                                                                      |
| quantity          | да           | float              | Количество, например `3`                                                                                                                          |
| amount            | да           | float              | Стоимость единицы, например `100.55`                                                                                                              |
| amountWoVat       | да           | float              | Стоимость единицы без учета НДС                                                                                                                   |
| totalAmount       | да           | float              | Стоимость всех единиц с НДС, например`123.55`                                                                                                     |
| totalVatAmount    | да           | float              | Итого сумма НДС, например `23`                                                                                                                    |
| excise            | нет          | float              | Сумма акциза, например, `10.00`                                                                                                                   |
| vatCode           | да           | string(20) enum    | Код процента НДС, допустимые значения: `VATNONE` - не облагается,`VATNONE` - не облагается, `RUS_VAT0` - 0%, `RUS_VAT10` - 10%, `RUS_VAT20` - 20% |
| type              | да           | string(10) или int | Тип позиции, [в соответствии со справочником](/docs/dictionary/tag1212) или service - сервис, commodity - товар                                   |
| paymentType       | да           | string(20) enum    | Тип оплаты, допустимые значения: `full_prepayment`, `prepayment`, `advance`, `full_payment`                                                       |
| metaData          | нет          | object             | [Дополнительные данные элемента корзины](/docs/merchant/order/metadata/)                                                                                   |


---
[Читать далее &raquo;](/docs/merchant/order/shipment_get){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

{: .fs-6 .fw-300 }
