import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "novatech_.db"

tickets = [
    ("WEB-001", "L'index ne doit pas afficher de tiquets", "Critique", "Ouvert", None, "Web"),
    ("WEB-002", "Le lien vers l'analyse des drones est mort sur la page d'accueil", "Haute", "Ouvert", None, "Web"),
    ("WEB-003", "Ajouter un badge Nouvelle version sur la page Méthodologie", "Moyenne", "Ouvert", None, "Web"),
    ("WEB-004", "Masquer les informations sensibles dans le HTML", "Critique", "Ouvert", None, "Sécurité"),
    ("WEB-005", "Le tableau des tickets ne s'affiche pas correctement sur les petits écrans", "Moyenne", "Ouvert", None, "Web"),
    ("DATA-001", "Créer une base SQLite contenant les tickets du portail", "Moyenne", "Ouvert", "DSI", "Data"),
    ("DATA-002", "Écrire une requête SQL listant uniquement les tickets ouverts", "Basse", "Ouvert", "DSI", "Data"),
    ("PY-001", "Créer un script Python exportant les tickets en HTML", "Moyenne", "Ouvert", "DSI", "Python"),
    ("PY-002", "Ajouter dans le README la procédure d'exécution des scripts Python", "Basse", "Ouvert", None, "Documentation"),
]

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS tickets")

cursor.execute("""
CREATE TABLE tickets (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    assignee TEXT,
    category TEXT NOT NULL
)
""")

cursor.executemany("""
INSERT INTO tickets (id, title, priority, status, assignee, category)
VALUES (?, ?, ?, ?, ?, ?)
""", tickets)

conn.commit()
conn.close()

print(f"Base initialisée : {DB_PATH}")