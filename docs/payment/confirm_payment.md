---
layout: default
nav_order: 30
title: "Подтверждение оплаты счёта"
parent: "Платёжные инструменты"
date: 2023-10-25 00:00:00 +0300
---

# Подтверждение оплаты заказа

Для подтверждения оплаты счёта, необходимо вызвать следующий метод API:

- метод: `POST`
- ресурс: `/v3/payment/api/invoice/confirm`
- тело запроса - объект [CreateInvoicePaymentRequest](#createinvoicepaymentrequest)
- тело ответа - объект [InvoicePaymentResponse](#invoicepaymentresponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса</summary>
<section markdown="1">
``` json
POST /v3/payment/api/invoice/confirm
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
User-Agent: MyApp 1.0
Accept: application/json
{
    "paymentOperationId" : "117a58b0-7dc9-424c-8f07-b8a865e8bcc7",
    "paymentOrderNumber" : "1342",
    "paymentOrderDate" : "2023-04-01",
    "amount" : 19658.45,
    "currencyId" : "RUB",
    "customer" : {
      "type" : "legal",
      "name" : "ООО Ромашка",
      "vatNumber" : "7710044140",
      "taxRegistrationReasonCode" : "770001001",
      "settlementAccount" : "40702810800190000253",
      "correspondentAccount" : "30101810700000000187",
      "bankName" : "ПАО ВТБ",
      "bic" : "044039142"
    }
}
```
</section>
</details>

## CreateInvoicePaymentRequest

| Свойство           | Обязательное | Тип             | Описание                   | Пример значения                        |
|--------------------|--------------|-----------------|----------------------------|----------------------------------------|
| invoiceId          | да           | string(36)      | Id счёта                   | `01771534-1a57-f184-dee3-ebeb91dded75` |
| paymentOperationId | да           | string(36)      | Id операции                | `117a58b0-7dc9-424c-8f07-b8a865e8bcc7` |
| amount             | да           | float           | Сумма платежа              | `19658.45`                             |
| currencyId         | да           | string(3) enum  | Код валюты счёта в соответствии с [ISO 4217](/docs/dictionary/iso4217/) | `RUB`, `USD`,`EUR`, `GBP` |
| paymentOrder       | нет          | [PaymentOrder](#paymentorder) | Детали платежа)    |                                        |
| status                    | нет          | string(50) enum | Статус платежа (paid, pending) | `paid`                                 |

## PaymentOrder

| Свойство                  | Обязательное | Тип             | Описание                   | Пример значения                                                |
|---------------------------|--------------|-----------------|----------------------------|----------------------------------------------------------------|
| type                      | да           | string(10) enum | Тип плательщика            | `legal` - юр. лицо, `private` - физ лицо                       |
| number                    | нет          | string(36)      | Номер платёжного поручения | `1342`                                 |
| date                      | нет          | string(36)      | Дата платёжного поручения  | `2023-04-01`                           |
| amount                    | да           | float           | Сумма платежа              | `19658.45`                                                 |
| currencyId                | да           | string(3) enum  | Код валюты счёта в соответствии с [ISO 4217](/docs/dictionary/iso4217/) | `RUB`, `USD`,`EUR`, `GBP`              |
| name                      | нет          | string(500)     | Наименование плательщика       | `ООО Ромашка`                                                  |
| phone                     | нет          | string(100)     | Номер телефона                 | `79001112233`                                                  |
| vatNumber                 | нет          | string(20)      | ИНН                            | `7710044140`                                                   |
| taxRegistrationReasonCode | нет          | string(9)       | КПП                            | `770001001`                                                    |
| settlementAccount         | нет          | string(20)      | Номер расчт. счёта             | `40702810800190000253`                                         |
| correspondentAccount      | нет          | string(20)      | Номер корр. счёта              | `30101810700000000187`                                         |
| bankName                  | нет          | string(100)     | Наименование банка             | `ПАО ВТБ`                                                      |
| bic                       | нет          | string(9)       | БИК                            | `044039142`                                                    |
| kbk                       | нет          | string(20)      | Код бюджетной классификации (КБК) | `18210501011011000110`                                      |
| paymentPurpose            | нет          | string(210)     | Назначение платежа             | `Оплата по счёту №10-2946153 за авиабилеты, НДС не выделяется` |


## InvoicePaymentResponse

Повторяет свойства объекта [CreateInvoicePaymentRequest](#createinvoicepaymentrequest) с дополнительными свойствами:

| Свойство   | Обязательное | Тип        | Описание                                      | Пример значения                         |
|------------|--------------|------------|-----------------------------------------------|-----------------------------------------|
| id         | да           | string(36) | Идентификатор транзакции в системе Инвойсбокс | `8c0e116d-31a5-4210-b62e-6b6917851f69`  |


## NotificationErrorCode

| Код ошибки             | Описание                                                                                                                                                  |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `out_of_service`       | Техническая ошибка обработки запроса, при получении этого кода ошибки необходимо пытаться повторить запрос еще несколько раз в течение последующих суток. |
| `invoice_already_paid` | Счёт уже оплачен другим инструментом оплаты :warning:                                                                                                     |
| `invoice_not_found`    | Счёт не найден в учётной системе                                                                                                                          |
| `signature_error`      | Ошибка проверки подписи запроса                                                                                                                           |

{: .warning }
> Обратите внимание, в случае, если аналогичный запрос на оплату уже был обработан ранее успешно и заказ был отмечен как оплаченный, то в этом случае будет возвращён статус успешной обработки `success`. В случае, если заказ был оплачен ранее под другим идентификатором или иным платёжным инструментом, вернётся ошибка `invoice_already_paid`.


## Подпись запроса

При отправке запросе необходимо сформировать и передать подпись тела запроса в заголовке `X-Signature`. При ошибке проверки подписи будет сформирован ответ [NotificationError](#notificationerror) с [NotificationErrorCode](#notificationerrorcode) `signature_error`.
Электронная подпись формируется путем криптографического преобразования содержимого тела запроса с использованием ключа и согласованного алгоритма.
По умолчанию используется алгоритм sha1 и метод hmac.



---
[Читать далее &raquo;](/docs/dictionary){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

{: .fs-6 .fw-300 }
