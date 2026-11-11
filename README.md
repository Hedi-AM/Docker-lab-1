# Mini-projet Docker — Application Flask

## Ce que fait l'application
Application web Flask qui renvoie une page HTML contenant un message d'accueil configurable.

## Image Docker Hub
- Dépôt : `hediam/mini-projet`
- Versions : `1.0.0`, `1.0.1`
- Alias flottant : `1.0` (pointe actuellement vers `1.0.1`)

## Variables d'environnement
| Variable | Valeur par défaut | Description |
|---|---|---|
| `WELCOME_MESSAGE` | `Bonjour depuis la version 1.0.1 !` | Message affiché sur la page |

## Lancer l'application (image publiée uniquement)
```bash
docker run -d \
  --name web-app \
  -p 8080:5000 \
  -e WELCOME_MESSAGE="Bonjour" \
  --memory 256m \
  --cpus 0.5 \
  hediam/mini-projet:1.0
