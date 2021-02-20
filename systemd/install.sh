cp scrapyd.timer scrapyd.service /usr/lib/systemd/system
systemctl daemon-reload
systemctl enable --now scrapyd.timer