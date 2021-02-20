systemctl disable --now scrapyd.timer
rm /usr/lib/systemd/system/scrapyd.service /usr/lib/systemd/system/scrapyd.timer
systemctl daemon-reload