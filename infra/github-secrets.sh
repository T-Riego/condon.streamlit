#!/bin/bash
# Configurar secrets nos 3 repos GitHub
# Rodar localmente com: bash github-secrets.sh
# Requer: gh CLI autenticado como T-Riego

VPS_HOST="187.55.77.125"
VPS_USER="root"
# VPS_PASSWORD: definir antes de rodar
# export VPS_PASSWORD="sua_senha"

for REPO in T-Riego/condon.streamlit T-Riego/condon.web T-Riego/condon.api; do
  echo "==> Configurando secrets em $REPO..."
  gh secret set VPS_HOST     --body "$VPS_HOST"     --repo "$REPO"
  gh secret set VPS_USER     --body "$VPS_USER"     --repo "$REPO"
  gh secret set VPS_PASSWORD --body "$VPS_PASSWORD" --repo "$REPO"
  echo "    OK"
done

echo "Secrets configurados nos 3 repos."
