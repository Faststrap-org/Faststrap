# Deploying to a VPS

Recommended VPS providers by price:

- Hetzner CX11: €3.29/month (best price/performance in Europe)
- DigitalOcean Basic: $4/month
- Vultr: $2.50/month
- Oracle Cloud Always Free: permanently free (2 AMD VMs)

## Server Setup

```bash
sudo apt update && sudo apt install python3-pip nginx -y
pip install faststrap uvicorn gunicorn

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker \
  --bind 127.0.0.1:5001
```

## Nginx Config (Including SSE)

```nginx
server {
    listen 80;
    server_name yourapp.com;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api/stream {
        proxy_pass http://127.0.0.1:5001;
        proxy_buffering off;
        proxy_cache off;
        proxy_set_header Connection '';
        proxy_http_version 1.1;
        chunked_transfer_encoding on;
    }
}
```

## Optional: Cloudflare Tunnel

```bash
cloudflared tunnel create my-app
cloudflared tunnel run --url http://localhost:5001 my-app
```

Benefits: DDoS protection, SSL termination, global CDN, no firewall port opening, full SSE/WebSocket support.

