cp video_card_checker.service video_card_checker.timer /usr/lib/systemd/system
systemctl daemon-reload
systemctl enable --now video_card_checker.timer