# Create PPP Users
Bulk create VPN users from a CSV file

## Description
+ [EN: Bulk create VPN users from a file](https://mhelp.pro/mikrotik-script-bulk-create-vpn-users-from-a-file/);
+ [ES: Crear usuarios de VPN de forma masiva a partir de un archivo](https://mhelp.pro/es/mikrotik-script-crear-usuarios-de-vpn-de-forma-masiva-a-partir-de-un-archivo/); 
+ [RU: Массовое создание VPN пользователей из файла](https://mhelp.pro/ru/mikrotik-skript-massovoe-sozdanie-vpn-polzovateley-iz-fayla/);
+ [FR: Créer en masse des utilisateurs VPN à partir d’un fichier](https://mhelp.pro/fr/mikrotik-script-creer-en-masse-des-utilisateurs-vpn-a-partir-dun-fichier/);
+ [DE: Massenerstellung von VPN-Benutzern aus einer Datei](https://mhelp.pro/de/mikrotik-script-massenerstellung-von-vpn-benutzern-aus-einer-datei/);
+ [NL: Maak in bulk VPN-gebruikers aan op basis van een bestand](https://mhelp.pro/nl/mikrotik-script-maak-in-bulk-vpn-gebruikers-aan-op-basis-van-een-bestand/);

## Variables
Specify variables:
1. **FileName** - file name;
2. **Separator** - value separator (depends on locale).

## Errors
If you get the following errors:
- `syntax error (line 2 column 7)`;
- `expected command name (line 1 column 29)`;

Look what separator is used in the import file and specify it in the variable *Separator*.

---
Verified: RouterBOARD 952Ui-5ac2nD, RouterOS 6.47.8 (stable)

Yun Sergey [MHelp.pro] 2020