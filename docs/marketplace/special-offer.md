---
layout: default
nav_order: 90
title: "Акции и спецпредложения"
parent: "Маркетплейс"
date: 2023-10-26 00:00:00 +0300
---

# Управление акциями и спец-предложениями магазина

Магазин может управлять набором акций и спец-предложений, которые будут отображены в маркетплейсе.

Для добавления или изменения спец-предложения, отправьте следующий запрос:

- метод: `POST`
- ресурс: `/special-offer`
- тело запроса - объект [CreateSpecialOfferRequest](#createspecialofferrequest)
- тело ответа - объект [SpecialOfferResponse](#specialofferresponse)
- Возможные [ошибки](/docs/dictionary/error/)


<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /special-offer
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
User-Agent: MyApp 1.0
Accept: application/json
{
   "merchantId" : "ffffffff-ffff-ffff-ffff-ffffffffffff",
   "externalId" : "1234",
   "active" : true,
   "startAt" :"2023-01-01T12:00:00Z",
   "finishAt" :"2029-01-01T23:59:59Z",
   "name" : "Скидка на День Рождения",
   "description" : "Скидка 15% на всё меню в день рождения",
   "tags" : [
      "birthday"
   ]
}
```
</section>
<section markdown="1">
``` json
{
   "data":{
      "id" : 123,
      "merchantId" : "ffffffff-ffff-ffff-ffff-ffffffffffff",
      "externalId" : "1234",
      "active" : true,
      "startAt" : "2023-01-01T12:00:00Z",
      "finishAt" : "2029-01-01T23:59:59Z",
      "name" : "Скидка на День Рождения",
      "description" : "Скидка 15% на всё меню в день рождения",
      "tags" : [
         "birthday"
       ]
   }
}
```
</section>
</details>

## CreateSpecialOfferRequest

| Свойство        | Обязательное | Тип             | Описание                                                            | Пример значения                        |
|-----------------|--------------|-----------------|---------------------------------------------------------------------|----------------------------------------|
| merchantId      | да           | string(36)      | Идентификатор магазина                                              | `01771534-1a57-f184-dee3-ebeb91dded76` |
| externalId      | да           | string(36)      | Идентификатор спец-предложения во внтуренней системе учёта магазина | `1234` |
| active          | да           | bool            | Флаг активности спец-предложения                                    | `true` |
| startAt         | да           | datetime        | Время начала действия спец-предложения                              | `2023-01-01T12:00:00Z` |
| finishAt        | да           | datetime        | Время окончания действия спец-предложения                           | `2029-01-01T23:59:59Z` |
| description     | да           | string(1000)    | Описание                                                            | `Скидка 15% на всё меню в день рождения` |
| tags            | да           | array of string | Теги                                                                | `birthday` |

## SpecialOfferResponse

Повторяет свойства объекта [CreateSpecialOfferRequest](#createorderrequest) с дополнительными свойствами:

| Свойство                  | Обязательное | Тип   | Описание                                         | Пример значения |
|---------------------------|--------------|-------|--------------------------------------------------|-----------------|
| id                        | да           | int   | Идентификатор спец-предложения в маркетплейсе    | `123`           |


---

[Читать далее &raquo;](/docs/partner){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
