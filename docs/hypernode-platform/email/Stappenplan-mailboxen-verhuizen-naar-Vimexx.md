# Stappenplan mailboxen verhuizen naar Vimexx


**Let op:** Indien je zelfstandig je e-mail verhuist naar Vimexx zonder gebruik te maken van de verhuisservice dan kunnen wij geen verantwoordelijkheid nemen voor eventuele problemen die daaruit voorkomt.

Hieronder vind je de stappenplan hoe je de verhuisservice kunt aanvragen, en hoe je aan de juiste gegevens komt om je e-mail goed in te stellen nadat Vimexx het heeft gemigreerd.

## Stappenplan in het kort:

1. [Maak een account aan bij V](https://www.vimexx.nl/registe)imexx.
1. Bestel een webhosting plus pakket via dez[e link (ook al g](https://www.vimexx.nl/cart/add/hosting/114)ebruik je het alleen voor mail).
1. Vraag de [verhuisservice aan.](https://www.vimexx.nl/help/verhuisservice-aanvraag-indienen#Verhuizing_starten)
1. Selecteer ‘Domein + Mail’in onder Wat wil je verhuizen?, ook al wil je alleen je e-mail verhuizen.
1. Vul alleen de volgende informatie in op het verhuisservice formulier:
- het domein (of domeinen) van de mail adressen die je wilt verhuizen.
- vervolgens vul je per domein het volgende in:
  - alle mail adressen die je wilt verhuizen.
  - de wachtwoorden van de mail adressen.
  - de mailserver (imap.byte.nl).
- de overige velden (zoals subdomeinen, verhuiscode, dns gegevens) laat je leeg.
1. Het ticket is nu aangemaakt, iemand van Vimexx zal binnenkort de migratie in gang zetten en verdere informatie versturen.
1. Zodra het afgerond is krijg je hier bevestiging van, ga dan naar je hosting pa[nel bij Vimexx en druk op ‘D](https://my.vimexx.nl/userhosting)irect inloggen’ bij je Webhosting Plus pakket om bij DirectAdmin te komen.
1. Je ziet 2 opties, selecteer niet je domeinnaam maar de onderste optie (eindigt met zxcs-klant.nl)
1. Ga naar DNS Management en haal hier je IPV4 en IPV6 adres op
1. Ga naar het [Byte Service Panel](https://service.byte.nl/protected/overzicht/)
1. Selecteer je domein -> Instellingen -> DNS en pas het volgende toe:
- Verwijder de MXregel met smtp2.byte.nl met Prio 20
- Wijzig het smtp1.byte.nl Prio 10, verander deze naar mail.DOMEINNAAM.XXX

(DOMEINNAAM uiteraard vervangen met jouw domein naam en .XXX met welke extensie, .nl/.com/.be, etc.)

- Voeg een nieuw record toe met de volgende gegevens:
  - Name:mail
  - Type:A
  - Content:vul hier het IPV4 adres in
  - Prio:Dit laat je leeg
  - TTL:600
- Voeg vervolgens nog een nieuw record toe met de volgende gegevens:
  - Name:mail
  - Type:AAAA
  - Content:vul hier het IPV6 adres in
  - Prio:Dit laat je leeg
  - TTL:600
- Pas je SPF record aan:
- Kijk weer naar je DNS gegevens op DirectAdmin bij Vimexx.
- Kopieer alleen het dikgedrukte / rood gemarkeerde uit de SPF regel:"v=spf1a mx **ip4:185.104.29.146 ip6:2a06:2ec0:1:0:0:0:0:155 include:filter-out.zxcs.nl** ~all"
- Pas op de Byte control panel je SPF regel aan, en plak deze content in je SPF regel zodat het er als volgt uit komt te zien:
- v=spf1mx a include:spf.domainnaam.hypernode.io include:spf.mandrillapp.com **ip4:185.104.29.146 ip6:2a06:2ec0:1:0:0:0:0:155 include:filter-out.zxcs.nl** ?all

**Let hierbij goed op de spaties. De exacte details zullen verschillen per domein en per klant.**

- Herhaal deze stap voor elk domeinnaam waarvan je de e-mail hebt verhuisd
1. Je bent nu klaar met het instellen van de DNS records, ga weer naar DirectAdmin -> E-mail Accounts.
1. Je ziet hier alle mailadressen die zijn verhuisd, op deze pagina kun je alle informatie terugvinden hoe je dit nu goed instelt per e-mail client (Office Outlook, Thunderbird, Gmail, etc).

## Uitgebreide uitleg:

1. **Account aanmaken:**

Op [https://www.vimexx.nl/register kan je](https://www.vimexx.nl/register) rechtstreeks een nieuw account aanmaken. Je kunt hier kiezen om een particulier of zakelijk account aan te maken. Het is belangrijk om de juiste keuze te maken i.v.m. de factuur die na de bestelling aangemaakt wordt.

2. **Pakket aanschaffen:**

Via een speciale link kun je een plus pakket afnemen:[https://www.vimexx.nl/cart/add/hosting/114](https://www.vimexx.nl/cart/add/hosting/114)

Het is belangrijk deze link te gebruiken, gezien Vimexx dan ook weet dat je afkomstig bent van Hypernode B.V. waardoor het verhuis proces soepeler zal verlopen.

3. **Verhuisservice aanvragen:**

Zodra je het hosting pakket hebt besteld kun je de verhuisservice aanvragen: <https://www.vimexx.nl/help/verhuisservice-aanvraag-indienen#Verhuizing_starten>

Specifiek kun je deze vinden onder ‘Mijn Hostings’in het Vimexx klantenpaneel.

![Screenshot 1](https://user-images.githubusercontent.com/121667008/233336264-964f3ed4-fdf0-4eb1-a48a-498ab7012feb.png)

4. **Het invullen van het verhuisservice aanvraag formulier**
1. Selecteer eerst ‘Domein toevoegen’en vul hier het domeinnaam in van de e-mail adressen die je wilt verhuizen. Dit kunnen er meerdere zijn:

2. Onder het domein zelf selecteer je ‘Domein + Mail’in onder Wat wil je verhuizen?, ook al wil je alleen je e-mail verhuizen:

3. Vervolgens vul je het domeinnaam in die je wilt verhuizen onder ‘Domeinnaam’en druk je op ‘Een e-mail adres toevoegen’.

4. Zit hier alle mailadressen in die je wilt verhuizen inclusief:
- de wachtwoorden van de mailadressen.
- de mailserver (imap.byte.nl).

1. de overige velden (zoals subdomeinen, verhuiscode, dns gegevens) laat je leeg.
1. Je kunt hier nog eventuele opmerkingen kwijt, het is wellicht handig te vermelden dat je vanaf Hypernode komt. Vink vervolgens aan dat alleen de gemarkeerde velden worden overgezet en druk op ‘Verhuizing aanvragen’

5. **Na het aanvragen van de verhuisservice**

Afhankelijk van de drukte kan het enkele dagen duren voordat je verzoek wordt opgepakt. Een medewerker van Vimexx zal vervolgens ervoor zorgen dat alles verhuisd wordt en je hiervan op de hoogte brengen. Je kunt ten alle tijden hier de status van je ticket(s) inzien:https[://my.vimexx.nl/ticket](https://my.vimexx.nl/ticket)

6. **Na de migratie**

Nadat je bevestiging hebt ontvangen dat de verhuizing is afgerond, ontvang je verdere instructies van Vimexx. In de meeste gevallen dien je nu een aantal DNS records te wijzigen op ons Service Pa[nel, dit gaat als v](https://service.byte.nl/)olgt. Ze de volgende stappen hoe verder:

7. **Log in bij DirectAdmin op het Vimexx klantenpaneel**

Ga naar [https://my.vimexx.nl/userhosting en klik](https://my.vimexx.nl/userhosting) op ‘Direct inloggen’.

Hiermee kom je op het DirectAdmin panel van Vimexx.

8. **Pak je DNS gegevens er bij**

Je ziet als het goed is nu je domein(en) en ook een uitgebreide URL die eindigt met zxcs-klant.nl of iets wat hier op lijkt, klik daar op:

Klik vervolgens onder ‘Your account’op ‘DNS Management’:

9. **Haal je IPV4 en IPV6 adres op**

Deze 2 IP adressen heb je straks nodig, je kunt of een tabblad openhouden met deze informatie of je kunt deze gegevens alvast kopiëren in een kladblok.

Je dient de 2 IP adressen te noteren van de nametype ‘Mail’, specifiek het adres achter ‘A’of ‘AAAA’:

Let op, dit IP adres zal voor jou anders zijn dan die in de screenshot.

10. **Vind je SPF record**

Je hebt ook een SPF record nodig, hiervan dien je alleen maar een deel te kopiëren, het stuk achter ‘MX‘en het stuk voor ‘~all’. Let hierbij ook op de spaties.

Kopieer dit en zet het in een kladblok. Het zou er zo uit moeten zien:

ip4:101.115.24.000 ip6:2a01:2ec0:1:0:0:0:0:155 include:filter-out.zxcs.nl![]

Let op:Ook hier zal het exacte IP adres van jou anders zijn, dit voorbeeld is puur om aan te tonen welk deel je moet kopieeren.

11. **Pas je gegevens aan op het Byte service panel:**

Ga vervolgens naar htt[ps://service.byte.nl/protected/overzicht/ en selecteer](https://service.byte.nl/protected/overzicht/) het domein waarvan je je gegevens wilt aanpassen

Druk op Instellingen en dan DNS:

12. **Pas je MX Records aan**

Je ziet vervolgens twee MXrecords:

Verwijder het MX20 Record (de onderste):

Pas vervolgens de bovenste aan:

Zet hier nu mail.domeinnaam.nl onder Content en vervang domeinnaam met de naam van jouw domein. Typ dus niet letterlijk mail.domeinnaam.nl in want dat gaat niet werken.

13. **Voeg 2 nieuwe records toe, A en AAAA,**

Druk op de knop ‘Voeg toe’

Zet hier vervolgens deze gegevens in, met type A en het IPV4 adres die je eerder genoteerd hebt.

Doe nu hetzelfde, maar dan met Type AAAA en het IPV6 adres:

14. **Pas je SPF Record aan.**

Zoek je SPF Record op en bewerk deze:

Plak vervolgens het deel van de SPF Record van Vimexx die je eerder hebt opgeslagen, en plaats deze in je huidige SPF Record zodat het als volgt er in komt te staan:

v=spf1mx a include:spf.domeinnaam.hypernode.io include:spf.mandrillapp.com **ip4:185.104.29.146 ip6:2a06:2ec0:1:0:0:0:0:155![](Aspose.Words.35f248b1-a3f5-40cb-87b5-9dddc6862fc4.024.png) include:filter-out.zxcs.nl** ?all

Let ook op de spaties, en je IP adres zal dus anders zijn dan in dit voorbeeld.

15. **Stel je e-mail in**

Ga nu terug naar DirectAdmin in je Vimexx klantenpaneel, en kies vervolgens je domeinnaam:

Kies daarna voor ‘E-mail accounts’onder E-mail management, je komt nu op de volgende pagina:

Je vindt hier alle mailadressen die zijn verhuisd, en alle gegevens die je nodig hebt om het goed in te stellen op jouw e-mail applicatie/platform. Je ziet onderaan ook instructies hoe je jouw e-mailadres toe kunt voegen, hoe je het kunt instellen, en wat te doen als het niet werkt.

Heb je issues of kom je er niet uit nadat Vimexx je e-mail al gemigreerd heeft? Neem dan contact op met hun support [afdeling.](https://www.vimexx.nl/help)
