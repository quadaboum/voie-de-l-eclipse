# 🌑 La Voie de l’Éclipse

> Ceci est un projet web artistique et immersif, réalisé dans un but **créatif, fictif et expérimental**.  
> Aucune incitation réelle. Tout est **pour rire**. Rien n'est réel.

---

## 🚀 Description

La Voie de l’Éclipse est une plateforme interactive en Flask + PostgreSQL.  
Elle propose un univers sombre, mystique et évolutif, basé sur un système d’invitation.  
Son design ésotérique est volontairement immersif et narratif.

---

## ⚙️ Technologies utilisées

- Python 3.x (Flask)
- PostgreSQL (via Railway)
- psycopg2 / Werkzeug
- HTML + CSS custom (ambiance sombre + effets visuels)
- Hébergement via [Railway.app](https://railway.app)

---

## 🧾 Installation locale

```bash
git clone https://github.com/ton-user/voie-de-l-eclipse.git
cd voie-de-l-eclipse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Exécuter si tu testes en local avec une base PostgreSQL
python init_db.py
python app.py
```

---

## 🧪 Déploiement Railway (recommandé)

1. Crée un projet sur [Railway](https://railway.app)
2. Ajoute le plugin PostgreSQL
3. Récupère la variable `DATABASE_URL`
4. Ajoute-la dans les Variables de ton projet
5. Lance `init_db.py` une seule fois pour créer les tables

---

## ❗ Avertissement

Ce projet est **fictif**, **non lucratif**, et n'a aucune vocation sérieuse.  
Tout contenu, même choquant ou absurde, n’est là que pour explorer les limites du storytelling web.  
Aucune action ne doit être interprétée comme réelle ou applicable.

---

## 🌀 Licence

Projet ouvert, usage libre à des fins non commerciales.  
**Ne pas copier le contenu sans mention.**  
Tout ce qui est dit ici **reste ici.**
