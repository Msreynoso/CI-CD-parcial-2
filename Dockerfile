FROM nginx:alpine

# Copiamos el HTML al directorio de nginx
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
