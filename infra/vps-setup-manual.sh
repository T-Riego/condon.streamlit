#!/bin/bash
# Setup completo da VPS — rodar como root em 187.77.55.125
# Uso: bash /tmp/vps-setup-manual.sh
set -e

BASE="/var/www/condon"
EMAIL="tiago@riegos.dev"
SUPABASE_URL="https://mgkyqailpawykhzsidxd.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1na3lxYWlscGF3eWtoenNpZHhkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NzI1Njc5NCwiZXhwIjoyMDkyODMyNzk0fQ.p9ZTMAo38MMHfZFduFCBGlzLyj_mej6164O-A8QIdRQ"
SUPABASE_ANON="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1na3lxYWlscGF3eWtoenNpZHhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcyNTY3OTQsImV4cCI6MjA5MjgzMjc5NH0.fhngOe8nYj07ln8yH19X0YLop_yBf24MDuaEstqu7Po"

echo "==> [1/7] Clonando repositórios em $BASE ..."
mkdir -p "$BASE"
git clone https://github.com/T-Riego/condon.streamlit "$BASE/streamlit" 2>/dev/null || (cd "$BASE/streamlit" && git pull)
git clone https://github.com/T-Riego/condon.web       "$BASE/web"       2>/dev/null || (cd "$BASE/web" && git pull)
git clone https://github.com/T-Riego/condon.api       "$BASE/api"       2>/dev/null || (cd "$BASE/api" && git pull)

echo "==> [2/7] Criando .env da API ..."
cat > "$BASE/api/.env" << EOF
SUPABASE_URL=$SUPABASE_URL
SUPABASE_SERVICE_KEY=$SUPABASE_KEY
ALLOWED_ORIGINS=https://condon.web.riegos.dev,http://localhost:5173
EOF

echo "==> [3/7] Criando .env do frontend (build args Docker) ..."
cat > "$BASE/web/.env" << EOF
VITE_API_URL=https://condon.api.riegos.dev
VITE_SUPABASE_URL=$SUPABASE_URL
VITE_SUPABASE_ANON_KEY=$SUPABASE_ANON
EOF

echo "==> [4/7] Criando rede Docker compartilhada ..."
docker network create traefik-net 2>/dev/null || echo "Rede traefik-net já existe."

echo "==> [5/7] Subindo Traefik + Portainer ..."
mkdir -p "$BASE/infra"

cat > "$BASE/infra/traefik.yml" << 'TRAEFIK'
api:
  insecure: false

providers:
  docker:
    exposedByDefault: false
    network: traefik-net

entryPoints:
  web:
    address: ":80"
TRAEFIK

cat > "$BASE/infra/docker-compose.yml" << 'INFRA'
version: "3.8"

networks:
  traefik-net:
    external: true

services:
  traefik:
    image: traefik:latest
    container_name: traefik
    restart: unless-stopped
    networks:
      - traefik-net
    ports:
      - "8090:80"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./traefik.yml:/traefik.yml:ro
    labels:
      - "traefik.enable=false"

  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    networks:
      - traefik-net
    ports:
      - "9000:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  portainer_data:
INFRA

cd "$BASE/infra" && docker compose up -d

echo "==> [6/7] Configurando nginx ..."
NGINX_CONF="/etc/nginx/sites-available/condon"
cat > "$NGINX_CONF" << 'NGINX'
server {
    listen 80;
    server_name condon.streamlit.riegos.dev;
    location / {
        proxy_pass         http://127.0.0.1:8090;
        proxy_http_version 1.1;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   Upgrade           $http_upgrade;
        proxy_set_header   Connection        "upgrade";
        proxy_read_timeout 86400;
    }
}
server {
    listen 80;
    server_name condon.web.riegos.dev;
    location / {
        proxy_pass         http://127.0.0.1:8090;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
    }
}
server {
    listen 80;
    server_name condon.api.riegos.dev;
    location / {
        proxy_pass         http://127.0.0.1:8090;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
    }
}
server {
    listen 80;
    server_name portainer.riegos.dev;
    location / {
        proxy_pass         http://127.0.0.1:9000;
        proxy_http_version 1.1;
        proxy_set_header   Host              $host;
        proxy_set_header   Upgrade           $http_upgrade;
        proxy_set_header   Connection        "upgrade";
    }
}
NGINX

ln -sf "$NGINX_CONF" /etc/nginx/sites-enabled/condon
nginx -t && systemctl reload nginx

echo "==> [7/7] Emitindo SSL (Cloudflare proxy deve estar OFF para os condon.*) ..."
apt-get install -y certbot python3-certbot-nginx -q

certbot --nginx \
  -d condon.streamlit.riegos.dev \
  -d condon.web.riegos.dev \
  -d condon.api.riegos.dev \
  --non-interactive --agree-tos -m "$EMAIL"

nginx -t && systemctl reload nginx

echo ""
echo "==> Infra pronta! Agora faça push nos 3 repos para disparar o CI/CD:"
echo "    git push  →  condon.streamlit  (já feito)"
echo "    git push  →  condon.web        (já feito)"
echo "    git push  →  condon.api        (já feito)"
echo ""
echo "    Portainer: http://127.0.0.1:9000 (acesse via SSH tunnel)"
