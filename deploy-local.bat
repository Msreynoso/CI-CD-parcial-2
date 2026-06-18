@echo off
echo ================================
echo  Actualizando contenedor local
echo ================================

echo.
echo [1/3] Deteniendo contenedor anterior...
docker stop parcial-cicd 2>nul
docker rm parcial-cicd 2>nul

echo.
echo [2/3] Descargando imagen actualizada desde Docker Hub...
docker pull msreynoso/parcial-cicd:latest

echo.
echo [3/3] Iniciando contenedor...
docker run -d --name parcial-cicd -p 8080:80 msreynoso/parcial-cicd:latest

echo.
echo ================================
echo  Listo! Abre: http://localhost:8080
echo ================================
pause
