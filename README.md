![Illustration projet](https://simplonline.co/_next/image?url=https%3A%2F%2Fsimplonline-v3-prod.s3.eu-west-3.amazonaws.com%2Fmedia%2Fimage%2Fpng%2F77f97980-4755-4ff8-884e-e14df7073caa-69f5d8014a3b8626140302.png&w=1280&q=75)

# Opération Standardisation DSI — Portail NovaTech

> Le portail interne NovaTech, créé par le service Communication, est devenu ingérable.
> La DSI reprend le relais : stabiliser le projet, structurer Git, corriger les tickets via un workflow professionnel.

---

## Contexte du projet

Le projet existe mais présente plusieurs problèmes :

- Les fichiers HTML contiennent des données en dur
- Une base SQLite existe mais n'est pas clairement exploitée
- Un script Python génère du HTML sans documentation d'usage
- Certains liens sont cassés
- Des informations sensibles sont présentes dans le code
- Aucun workflow Git fiable n'est en place

---

## Objectifs de la journée

- [ ] Auditer l'état actuel du projet
- [ ] Mettre en place une stratégie de branches
- [ ] Travailler uniquement par tickets
- [ ] Utiliser des Pull Requests
- [ ] Documenter les règles de contribution (`CONTRIBUTING.md`)
- [ ] Nettoyer et corriger le portail sans casser le projet

---

## Arborescence du projet

```
brief_J3_code/
├── web/
│   ├── index.html
│   ├── methodologie.html
│   ├── tickets.html
│   └── style.css
├── scripts/
│   ├── init_db.py
│   └── export_tickets.py
├── CONTRIBUTING.md
└── README.md
```

---

## Démarche

### 1. Audit général & initialisation Git

Analyse de l'état du projet, identification des problèmes, mise en place de la structure Git.

### 2. Définition du workflow NovaTech

Rédaction du `CONTRIBUTING.md` établissant :
- Les conventions de nommage des commits
- Les conventions de nommage des branches
- Les règles relatives aux Pull Requests

### 3. Création et attribution des tickets

Chaque correctif ou amélioration passe par un ticket dédié, une branche associée et une PR avant merge.

---

## Installation & lancement

```bash
# Initialiser la base de données
python scripts/init_db.py

# Exporter les tickets en HTML
python scripts/export_tickets.py
```

Ouvrir ensuite `web/index.html` dans un navigateur.

---

## Contribution

Consulter [CONTRIBUTING.md](CONTRIBUTING.md) avant toute modification.
