cp scrapyd.service scrapyd.timer /usr/lib/systemd/system
systemctl daemon-reload
systemctl enable --now scrapyd.timer