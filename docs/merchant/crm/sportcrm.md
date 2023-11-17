---
layout: default
nav_order: 20
title: "SportCRM"
parent: "Модули для CRM"
grand_parent: "Приём платежей"
date: 2023-11-17 00:00:00 +0300
---

# Описание модуля SportCRM

![SportCRM](/assets/images/crm/sportcrm.png){: .img-right}

[SportCRM](https://sportcrm.club) — это облачная система для организации и контроля тренировочных и соревновательных процессов
в спортивных клубах. Помогает контролировать работу администраторов, тренеров и партнёров по франшизе. Модуль Инвойсбокс
предоставляет простую возможность приёма оплаты для спортивных клубов и полное соответствие ФЗ-54 без лишних хлопот.

## Настройка модуля

Зайдите в SportCRM в раздел Управление > Настройки > Филиалы.

![SportCRM](/assets/images/crm/sportcrm/1.jpg){: .img}

В выпадающем окне выберите Инвойсбокс

![SportCRM](/assets/images/crm/sportcrm/2.jpg){: .img}

Укажите в настройках Идентификатор Магазина (v2), Региональный код, API ключ, которые можно получить в [личном кабинете Инвойсбокс](https://business.invoicebox.ru).

![SportCRM](/assets/images/crm/sportcrm/3.jpg){: .img}

Также пропишите URL уведомления, которые сгенерирует SportCRM. Тип уведомления надо выбрать Оплата/HTTP/Post (HTTP POST запрос с данными оплаты в переменных).

![SportCRM](/assets/images/crm/sportcrm/4.jpg){: .img}
