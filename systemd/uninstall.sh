systemctl disable --now scrapyd.service
rm /usr/lib/systemd/system/scrapyd.service
systemctl daemon-reload