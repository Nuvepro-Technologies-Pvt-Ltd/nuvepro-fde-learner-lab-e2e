#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

if ! python3 -m venv .venv 2>/dev/null; then
  sudo apt-get update
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3-venv
  python3 -m venv .venv
fi

.venv/bin/python -m pip install --disable-pip-version-check --quiet --upgrade pip
.venv/bin/python -m pip install --disable-pip-version-check --quiet -r requirements.txt
.venv/bin/python .nuvepro/verify_package.py

cat > "$HOME/Desktop/start-fde-lab.sh" <<EOF
#!/usr/bin/env bash
cd "$repo_dir"
exec .venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
EOF
chmod +x "$HOME/Desktop/start-fde-lab.sh"

if command -v systemctl >/dev/null 2>&1 && sudo -n true 2>/dev/null; then
  sudo tee /etc/systemd/system/nuvepro-fde-lab.service >/dev/null <<EOF
[Unit]
Description=Nuvepro FDE learner lab
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$repo_dir
ExecStart=$repo_dir/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
  sudo systemctl daemon-reload
  sudo systemctl enable --now nuvepro-fde-lab.service
fi
