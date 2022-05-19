chmod +x ./run.sh
chmod +x ./mhc-scoreboard.service

python3.9 -m venv ./.venvs/mhc-scoreboard
source ./.venvs/mhc-scoreboard/bin/activate
pip install -r requirements.txt
pip install RPi.GPIO

cp ./mhc-scoreboard.service /etc/systemd/system/mhc-scoreboard.service