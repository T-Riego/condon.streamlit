#!/bin/bash
# Setup único na VPS — rodar como root uma vez
# bash /var/www/condon/infra/setup-vps.sh
set -e

EMAIL="tiago@riegos.dev"

echo "==> Criando rede Docker compartilhada..."
docker network create traefik-net 2>/dev/null || echo "Rede traefik-net já existe."

echo "==> Subindo Traefik + Portainer..."
cd /var/www/condon/infra
docker compose up -d

echo "==> Instalando certbot..."
apt-get update -q
apt-get install -y certbot python3-certbot-nginx

echo "==> Copiando config nginx (blocos sem SSL ainda)..."
cp /var/www/condon/infra/nginx-condon.conf /etc/nginx/sites-available/condon
ln -sf /etc/nginx/sites-available/condon /etc/nginx/sites-enabled/condon

# Habilitar apenas os blocos HTTP enquanto não há cert
# (nginx não sobe se referenciar cert que não existe)
nginx -t && systemctl reload nginx

echo ""
echo "==> Emitindo SSL — portainer.riegos.dev (Cloudflare proxy ON)"
echo "    (HTTP-01 challenge passa pelo Cloudflare normalmente)"
certbot --nginx -d portainer.riegos.dev \
  --non-interactive --agree-tos -m $EMAIL

echo ""
echo "==> Emitindo SSL — subdomínios condon.* (Cloudflare proxy DEVE estar OFF)"
certbot --nginx \
  -d condon.streamlit.riegos.dev \
  -d condon.web.riegos.dev \
  -d condon.api.riegos.dev \
  --non-interactive --agree-tos -m $EMAIL

nginx -t && systemctl reload nginx

echo ""
echo "==> Infra pronta!"
echo "    Portainer:  https://portainer.riegos.dev"
echo "    Streamlit:  https://condon.streamlit.riegos.dev  (após deploy)"
echo "    Web:        https://condon.web.riegos.dev        (após deploy)"
echo "    API:        https://condon.api.riegos.dev        (após deploy)"
echo "    Traefik:    interno em 127.0.0.1:8090"
