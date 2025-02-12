# Projektdokumentation

## **1. Projektauftrag**
### **Projektidee & Anlass**
Das Ziel dieses Projekts ist die Entwicklung eines Raspberry-Pi-gestützten Alarmsystems zur Bewegungserkennung. Die Idee entstand im Rahmen des Unterrichts, um ein praktisches Anwendungsbeispiel für den Einsatz von Mikrocontrollern, Sensoren und Softwareentwicklung zu erarbeiten.

## **2. Problemanalyse**
### **Ist-Analyse**
Momentan gibt es keine Möglichkeit ein Klassenzimmer vor unbefugtem Zugriff zu schützen. 

### **Soll-Konzept**
Die geplante Lösung besteht aus:
- einem Raspberry Pi als zentrale Steuereinheit
- einem PIR-Bewegungssensor zur Erkennung von Bewegungen
- einer Software, die Bewegung erkennt und daraufhin Aktionen ausführt (z. B. Alarm auslösen, Licht steuern etc.)
- einer Datenbank zur Speicherung von Alarmereignissen

## **3. Durchführung und Auftragsbearbeitung**
### **Wahl der Hard- und Softwareplattformen**
**Hardware:**
- Raspberry Pi 4 + Breadboard
- PIR-Bewegungssensor (HC-SR501)
- LED zur Signalisierung von Events
- RFID Karten und Chips

**Software:**
- Raspberry Pi OS
- Python für die Steuerung des Alarmsystems
- MariaDB
- Fastapi Python Backend
- Next (React-Framework)
- Pewee Python ORM für die Datenbank
- Ntfy für Notifciations

### **Entwicklungsumgebungen**
- VS Code
- Git + GitHub für Versionskontrolle
- Docker (für die Datenbank)

### **Realisierung**
Das System besteht aus mehreren Komponenten:
- **Backend:** Python Backend (Fastapi) zur Steuerung der Sensoren und Verarbeitung der Daten
- **Datenbank:** Speicherung der erkannten Bewegungen und Alarmstatus in MariaDB
- **Frontend:** Möglichkeit, den Status über eine Weboberfläche zu beobachten und managen
- **Notifications**: Das Auslösen eines Alarms schickt eine Benachrichtigung ans Handy

### **Datenbankmodell**
Einfaches ER-Diagramm für die Speicherung der Alarmereignisse:
# ![RaumSecurity ERD - Hakan, Yussuf](https://github.com/user-attachments/assets/766909ad-0862-48f2-b48c-8fd42e43e85e)




## **4. Prozessschritte & Vorgehensweise**
1. Einrichtung des Raspberry Pi und Installation aller benötigten Pakete
2. Anschluss und Test des MFRC522 RFID Sensors 
3. Anschluss des PIR-Sensors und Implementierung der Bewegungserkennung
4. Speicherung der Bewegungsereignisse in der Datenbank
5. Steuerung einer LED oder eines Relais bei erkannter Bewegung
6. Implementierung einer einfachen Benutzeroberfläche zur Statusabfrage (Admin Dashboard)
7. Implementierung der Zeitschaltung

## **5. Maßnahmen zur Qualitätssicherung**
- Gründliches Testen der Sensorik
- Überprüfung der Datenbankeinträge bei Bewegungserkennung
- Debugging der Software

## **6. Abweichungen, Anpassungen und Entscheidungen**
### **Geplante vs. tatsächliche Umsetzung**
- Ursprünglich wurde eine komplette Containerisierung des Projektes mit Docker geplant, aus zeitlichen Gründen wurde hiervon jedoch abgesehen

## **7. Fazit**
Das Projekt hat erfolgreich gezeigt, wie ein einfaches Alarmsystem mit einem Raspberry Pi umgesetzt werden kann. Bei Bedarf kann dieses System einfach Skaliert werden.
