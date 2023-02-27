# TP903
TP Kubernetes

1. Ecrire un microservice http "motd-api" (MOTD == Message of the Day)
  Le microservice retourne toujours un objet json {"message": MESSAGE}
  Le MESSAGE doit être configurable
  Le service prend deux variables d'environnement pour sa configuration: - MESSAGE est le message retourné par l'API - APP_PORT est le port d'écoute de l'API.
