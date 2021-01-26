---
title: "Дополнительные данные заказа"
permalink: /docs/order-metadata/
excerpt: "Order metadata description"
---

Иногда, для расширенной интеграции с платежным шлюзом требуется предоставить дополнительные данные о заказе. 
Это можно сделать путем передачи в запрос дополнительно объекта в формате [json-ld](https://json-ld.org/). Поддерживаются типы объектов, описанные на https://schema.org/

Пример объекта, описывающего бронирование отеля - [LodgingReservation](https://schema.org/LodgingReservation)
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
