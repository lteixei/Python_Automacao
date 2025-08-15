@echo off
cd /d %~dp0
git add .
git commit -m "Atualização automática dos testes"
git push origin main