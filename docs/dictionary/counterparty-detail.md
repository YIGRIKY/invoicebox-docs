---
layout: default
nav_order: 20
title: "Поиск по ИНН"
parent: "Справочники"
date: 2023-10-25 00:00:00 +0300
---

# Поиск и получение данных об организации по ИНН

Для получения списка организаций, необходимо вызвать следующий метод API:

- метод: `GET`
- ресурс: `/v3/filter/api/counterparty-detail`
- тело ответа - array of [OrderResponse]

В запросе есть обязательный параметр `vatNumber` - ИНН.

Пример запроса
```
GET /v3/filter/api/counterparty-detail?vatNumber=2323232323
```

## Counterparty

| Свойство                  | Обязательное | Тип             | Описание                                         |
|---------------------------|--------------|-----------------|--------------------------------------------------|
| id                        | да           | string(36)      | Идентификатор оригнизации в системе Инвойсбокс   |
| vatNumber                 | да           | string(20)      | ИНН                                              |
| taxRegistrationReasonCode | нет          | string(9)       | КПП                                              |
| name                      | нет          | string(100)     | Наименование организации                         |
| nameFull                  | нет          | string(300)     | Полное наименование организации                  |
| nameI18n                  | нет          | string(300)     | Полное наименование организации на языке региона |
| registrationNumber        | нет          | string(20)      | Регистрационный код организации                  |
| registrationDate          | нет          | datetime        | Дата регистрации организации                     |
| registrationAddress       | нет          | string(200)     | Адрес регистрации организации                    |
| postAddress               | нет          | string(200)     | Почтовый адрес организации                       |
| postAddressZip            | нет          | string(6)       | Почтовый индекс организации                      |


---

[Читать далее &raquo;](/docs/dictionary/iso4217/){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
