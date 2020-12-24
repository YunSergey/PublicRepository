# Bandwidth Exceeded Notification

This MikroTik script will send a notification when the bandwidth is exceeded on the interface (exceeding the download or upload speed). The script will send an email or Telegram message, but you can schedule other events to be executed.

## Description
+ [EN: MikroTik script: Bandwidth excess notification](https://mhelp.pro/mikrotik-script-bandwidth-excess-notification/utm_source=github);
+ [ES: Script MikroTik: Notificación de exceso de ancho de banda](https://mhelp.pro/es/script-mikrotik-notificacion-de-exceso-de-ancho-de-banda/utm_source=github);
+ [RU: MikroTik скрипт: Уведомление о превышении полосы пропускания](https://mhelp.pro/ru/mikrotik-skript-uvedomlenie-o-prevyshenii-polosy-propuskaniya/utm_source=github);
+ [FR: Script MikroTik: Notification d’excès de bande passante](https://mhelp.pro/fr/script-mikrotik-notification-dexces-de-bande-passante/utm_source=github);
+ [DE: MikroTik-Script: Benachrichtigung über Bandbreite Überschritten](https://mhelp.pro/de/mikrotik-script-benachrichtigung-ueber-bandbreite-ueberschritten/utm_source=github);
+ [NL: MikroTik-script: Melding van overmatige bandbreedte](https://mhelp.pro/nl/mikrotik-script-melding-van-overmatige-bandbreedte/utm_source=github);


## Variables
Specify variables:
1. **NotifyPeriod** – interval for sending notifications;
2. **Interface** – check interface (specify value from Traffic Monitor trigger);
3. **Threshold** – trigger response threshold (specify value from Traffic Monitor trigger).

---
Verified: RouterBOARD 952Ui-5ac2nD, RouterOS 6.48 (stable)

Yun Sergey [MHelp.pro] 2020