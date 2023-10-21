---
layout: default
nav_order: 40
title: "Подтверждение оплаты"
parent: "Подтверждение оплаты"
grand_parent: "Приём платежей"
---

# Подтверждение оплаты заказа

Для подтверждения оплаты заказа необходимо вызвать метод:

- метод: `POST`
- ресурс: `/v3/billing/api/order/{uuid}/payment-method-action/pay`
- тело запроса - объект [PayRequest](#payrequest)
- тело ответа - объект [PayResponse](#payresponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /v3/billing/api/order/{uuid}/payment-method-action/pay
{
  "paymentMethodId": "39363265",
  "languageId": "ru",
  "customer": {
    "name": "ООО Компания",
    "email": "email@gmail.com",
    "type": "legal",
    "phone": "79611234567",
    "vatNumber": "1233123",
    "registrationAddress": "123123123"
  },
  "customerPaymentData" : {
    "publicCode" : "string",
    "code" : "string"
  }
}
```
</section>
<section markdown="1">
``` json
{
  "data": {
    "type": "none",
    "result": "success",
    "resultData": {}
  }
}
```
</section>
</details>


## PayRequest

| Свойство               | Обязательное | Тип                                      | Описание                                        | Пример     |
|------------------------|--------------|------------------------------------------|-------------------------------------------------|------------|
| paymentMethodId        | да           | string(36)                               | Идентификатор инструмента подтверждения оплаты  |            |
| languageId             | нет          | string(2) enum                           | Язык плательщика                                | `ru`, `en` |
| customer               | да           | [Customer](/docs/merchant/order/create/#customer) | Информация о плательщике               |            |
| customerPaymentData    | да           | [customerPaymentData](/docs/merchant/guarantee/validate/#customerpaymentdata) | Данные ддя подтверждения оплаты заказа  |            |

#CustomerPaymentData

| Свойство    | Обязательное | Тип        | Описание                                           |
|-------------|--------------|------------|----------------------------------------------------|
| publicCode  | да           | string     | Публичный идентификатор кода                       |
| code        | да           | string     | Полученный плательщиком от системы Инвойсбокс код  |


## PayResponse

| Свойство | Обязательное | Тип        | Описание                             |
|----------|--------------|------------|--------------------------------------|
| data     | да           | [PaymentResponse](/docs/merchant/guarantee/pay/#paymentresponse) | Информация об оплате  |

## PaymentResponse

| Свойство    | Обязательное | Тип        | Описание                                 |
|-------------|--------------|------------|------------------------------------------|
| type        | да           | enum       | Тип действия к выполнению: none, message |
| result      | да           | enum       | Статус проверки (см. ниже)               |
| resultData  | да           | object     | Объект, в зависимости от типа действия (type) и результата (result), см. ниже  |

## Message

| Свойство    | Обязательное | Тип        | Описание            |
|-------------|--------------|------------|---------------------|
| title       | да           | string     | Заголовок сообщения |
| message     | да           | string     | Сообщние            |


Если type = message, требуется отобразить пользователю информацию от системы Инвойсбокс. Информация будет передана
в объекте resultData и будет содеражать вложенный объект message, пример:

``` json
{
  "message": {
    "title": "Недостаточно средств",
    "message": "Для подтверждения выбранного заказа недостаточно средств. Пожалуйста, восстановите баланс гарантийного фонда."
  }
}
```

Возможные статусы:
  - limitReached - Превышено кол-во попыток оплаты
  - notEnoughMoney - Недостаточно средств на счету
  - error - Непредвиденная ошибка
  - success - Оплата прошла


---

[Читать далее &raquo;](/docs/merchant/sdk/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
