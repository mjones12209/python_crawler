systemctl disable --now scrapyd.timer
rm /usr/lib/systemd/system/scrapyd.timer /usr/lib/systemd/system/scrapyd.service
systemctl daemon-reload