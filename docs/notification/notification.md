---
layout: default
title: "Обработка уведомлений"
nav_order: 5
has_children: true
permalink: /docs/notification
---

# Обработка уведомлений

Система «ИнвойсБокс» уведомляет Магазин о факте оплаты счёта несколькими способами. В первую очередь,
все уведомления о платежах направляются по электронной почте магазина или SMS. Ежедневно система
«ИнвойсБокс» также направляет сводный реестр платежей (Переводов) за прошедшие сутки.

Если Магазину требуется получать уведомления о платежах в автоматическом режиме, например, для передачи
статуса оплаты заказа в CMS или иную систему учёта, система «ИнвойсБокс» может направлять такие
уведомления по заранее заданным параметрам (ссылке). Система «ИнвойсБокс» поддерживает множество
форматов уведомлений, в том числе форматы сторонних платёжных решений.

В текущем разделеописаны базовые форматы уведомлений.

{: .fs-6 .fw-300 }