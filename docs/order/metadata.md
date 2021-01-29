---
layout: default
nav_order: 5
title: "Метаданные заказа"
parent: "Работа с заказом"
---

# Метаданные заказа

Передача расширенного набора данных по заказу осуществляется путём заполнения свойства заказа `metaData`
в запросе [создания заказа](/docs/order/create/). По-умолчанию свойство заполняется в формате [json-ld](https://json-ld.org/).
Система поддерживат типы объектов, описанные на сайте [https://schema.org/](https://schema.org/).

Для передачи данных бронирования места проживания (отель, хостел, апартаменты и пр.), в поле `metaData`
необходимо передать объект [LodgingReservation](https://schema.org/LodgingReservation)
``` json
{
  "@type": "LodgingReservation",
  "reservationId": "abc456",
  "reservationStatus": "https://schema.org/ReservationConfirmed",
  "underName": {
    "@type": "Person",
    "name": "John Smith"
  },
  "reservationFor": {
    "@type": "LodgingBusiness",
    "name": "Hilton San Francisco Union Square",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "333 O'Farrell St",
      "addressLocality": "San Francisco",
      "addressRegion": "CA",
      "postalCode": "94102",
      "addressCountry": "US"
    },
    "telephone": "415-771-1400"
  },
  "checkinTime": "2017-04-11T16:00:00-08:00",
  "checkoutTime": "2017-04-13T11:00:00-08:00"
}
```

[Читать далее](/docs/refund){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
