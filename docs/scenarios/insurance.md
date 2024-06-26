---
layout: default
nav_order: 80
title: "🏥 B2B продажи услуг страхования пассажиров"
parent: "Сценарии и бизнес-кейсы"
permalink: /docs/scenarios/insurance
date: 2024-02-08 00:00:00 +0300
---

# Сценарий продажи услуг страхования пассажиров

Решения Инвойсбокс API позволяют интегрировать способы оплаты по счёту для организаций и ИП.

Сервис Инвойсбокс сделает приём платежей от корпоративных клиентов за услуги страхования быстрым,
безопасным и удобным непосредственно в процессе оформления авиа или железнодорожного билета. Система
Инвойсбокс поможет подтвердить оплату онлайн или на месте, а также предоставит отчётные документы
клиенту через ЭДО или в бумажном виде курьером или почтой.

![Подключить](/assets/images/scenarios/insurance/frame1.png){: .imgt}

## Базовая схема взаимодействия

### Реализация мини-приложения

![Маркетплейс](/assets/images/scenarios/insurance/marketplace.png){: .imgt-left}

На стороне учётной системы страховых услуг формируется [мини-приложение](/docs/marketplace/mini-apps).
В мини-приложении реализуются следующие функции (экраны):
- Экран детальной информации о страховании поездки и форма заказа
- Опционально, другие экраны в соответствии с процессами покупки в рамках системы страхования
- Экран подтверждения заказа
- Функция создания заказа в системе Инвойсбокс
- Экран успешного подтверждения оплаты заказа

Информация об услуге страхования публикуется в [маркетплейсе Инвойсбокс](/docs/marketplace).
Для получения дополнительной информации см. также [описание работы мини-приложения](/docs/marketplace/mini-apps/description/) с
мини-приложением.

### Оформление заказа и счёта на оплату

Клиент, на платёжной странице, в процессе оформления авиа- или ж/д- перевозки или в приложении Инвойсбокс, изъявляет
желание добавить к заказу услугу страхования. Платёжная страница или приложение Инвойсбокс инициализирует мини-приложение
системы страхования. Мини-приложение может подсказать подходящие параметры исходя из данных основного заказа.
Покупатель оформляет заказ в мини-приложении и подтверждает его оплату. По факту подтверждения оплаты заказа, покупатель
получает ваучер на услугу.

Система Инвойсбокс перечисляет денежные средства консолидированным платежом на следующий рабочий день на
расчётный счёт юридического лица оператора услуг страхования.

{: .immediately }
> В случае, если у вас возникли вопросы, пожалуйста, [обратитесь к специалистам](https://www.invoicebox.ru/ru/contacts/feedback.html)
> системы Инвойсбокс. Мы ответим на любые ваши вопросы!