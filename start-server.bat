@echo off
title ChinaStyle Server (port 4321)
echo ============================================
echo  ChinaStyle - Traditional Wear Travel Guide
echo  Server running at http://localhost:4321
echo  Close this window to stop the server.
echo ============================================
echo.
cd /d D:\workspaces\website\chinese-traditional-wear
python -m http.server 4321 --directory dist
pause
