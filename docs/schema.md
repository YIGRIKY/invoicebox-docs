---
layout: nocompress
nav_order: 2
title: "Схема взаимодействия"
---

![Схема взаимодействия](/assets/images/api-invoicebox.png)

1. Покупатель оформляет заказ на сайте Магазина и выбирает способ оплаты через систему &laquo;ИнвойсБокс&raquo;.
1. Магазин создает в системе &laquo;ИнвойсБокс&raquo; заказ [через метод API](/docs/order/create/).
1. Система возвращает ссылку на платёжную страницу для оплаты заказа.
1. Магазин перенаправляет покупателя по полученной ссылке.
1. Покупатель заполняет необходимые для оплаты сведения и получет счёт для оплаты.
1. Покупатель оплачивает счёт.
1. Система &laquo;ИнвойсБокс&raquo; перенаправляет покупателя обратно на сайт Магазина.
1. Система &laquo;ИнвойсБокс&raquo; оповещает Магазин об успешной оплате заказа.
1. Покупатель обращается в Магазин для оформления возврата заказа.
1. Опционально, Магазин запрашивает [через метод API](/docs/refund/get/) доступные к возврату позиции в заказе.
1. Магазин создает возврат в системе &laquo;ИнвойсБокс&raquo; заказ [через метод API](/docs/refund/create/).
1. Система &laquo;ИнвойсБокс&raquo; осуществляет возврат денежных средств покупателю.

[](https://sequencediagram.org/index.html?presentationMode=readOnly#initialData=C4S2BsFMAJEIQRREEKwggeEEAwg1BMIIdhBWA4QZgfCCAsIIoJwgggiCBCIBroPIg050AggAoCS0bAdgG4D2IAMaQAQnwAeAKACGAV2B8usgLYAjSACdJMwQo3RA+CAFAXCCBhEED8IKkqJA3CCAZEEkAHaRtCCQzrsGiAcEFSBmEFQsXEBeECcXNw9pL05eAWExcWhtIzNLa3sAWgA+P0DgkIAuOAIsIlRESmgcYyDJPKDQnO5+IVEJYsAkEEBpECwCDGhkSuJ0clLykLpq1FqcSRb49vEchoLiwAwQEhDKXEAREFxaygJAARBp2fRcBnJum1roEPQCcxsrU3qAxpCc1IsrWztigZEMdEA9zMdUBgbKDcIh7uhnn9AGwgIVMgDkQBiUCGTQBiIG8ful-gAeImZHLZBZtRJdHD4YhkKg0OGMRHWFEEUjQXYnQikSQEv5ZClxKkdaCAPBBWah5iKEhJviZfhkAYZgaDUODIdDJnDzIrCTZ6A8GKhSFU0PlQtLKXLlrkPmtoIBiEAwiCIBGQ2th0AIgEYQaCmcjmRCACRAQhyfay4TUgtKgA)
[](https://sequencediagram.org/index.html#initialData=C4S2BsFMAJEIQRREEKwggeEEAwg1BMIIdhBWA4QZgfCCAsIIoJwgggiCBCIBroPIg050gGCCC8IBgRYIggBgXCCMCCABQCS0AG4BmAFABDAK7AA9gDs5AWwBGkAE5TZAYyXbogfBBegYRBA-CCpKiQNwggGRApABxnbQ+kK+XBogHBBUQGYQVCxcFhc3Dy8ZH2Y2DnJuPmg9AF5UwDwQcnNASRBEKgw7RBZcRGgCSzsbQGkQdKkzHisbewcAWgA+AODQlgAuOAIsIlRESmgcHhCpLpCwjtZ2Ll5yfsAkEGqsAgxoZFHidHJB4ZL6CZDUKQWEpPIOmZ7+phIWSlxAERBcScoCQAEQcdRJjhoLgGORqnZJtAWOgKlVKOZpkFZiwOg0mrZHP0TIgfsVUJYfqhCsVSlD0JUbIBFEEAbCAscyAORAGJRCSVAGIgCLR1gxDgAPDzWh12lclnw1jh8MQyAVSYwKZQaSwOEyWbhWWQADTQSwEOzmQDiICSyuQ9ZTKBdOc1HPN4iKVtAMnKDiazZcbYllqiLFyWlicXiCUSiiUytrGt67PRoQxUKQxmhumELsL3Xw7kiHtBAMQgGEQRAIyCDpIIgEYQaDmciWRCACRBFaRynLEFJ0hk3r8C4bMIMMITvhg6hbuWmE317cXCTkRpRyKd0OwsN2bPmtQR-oCEfcwvzrYsU3azLqDcGGJZcORIdrQqzcHXtmcsI2NyihW6bmsNlsdnthuVWz92ydO3nHskxfD12gHH17WyPICkLMo5wXM1oGeRBaWqeAGFxIgCikIA)

# Схема взаимодействия с ИнвойсБокс API v3

<div class="mermaid">
sequenceDiagram
    autonumber
    participant Покупатель
    participant Магазин
    participant ИнвойсБокс 
    rect rgb(0, 255, 0)
      Покупатель->>Магазин: Создает заказ
      Магазин->>ИнвойсБокс: Вызов метода создания заказа
      ИнвойсБокс->>Магазин: Идентификатор заказа и ссылка на оплату
      Магазин->>Покупатель: Перенаправление на платёжную страницу
      Покупатель-->>ИнвойсБокс: Взаимодействие с платёжной страницей, получение счёта
      Покупатель->>ИнвойсБокс: Оплата счёта
      ИнвойсБокс->>Покупатель: Перенаправление покупателя на сайт магазина
      ИнвойсБокс->>Магазин: Уведомление об успешной оплате
    end
    rect rgb(0, 0, 255)
      Покупатель->>Магазин: Обращается за возвратом по заказу
      Магазин-->ИнвойсБокс: Получение списка позиций в заказе
      Магазин->>ИнвойсБокс: Вызов метода оформления возврата
      ИнвойсБокс->>Покупатель: Осуществление возврата денежных средств
    end
</div>

[Читать далее](/docs/order){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
