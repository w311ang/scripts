set -e
pkg install -y libjpeg-turbo clang python git libsodium freetype
pip install --upgrade pip
pip install wheel
LDFLAGS=" -lm" pip install pillow
git clone https://github.com/NyanChanMeow/SSRSpeed && cd SSRSpeed
pip install -r requirements.txt
echo 'python main.py --skip-requirements-check $@' > main.sh && chmod 700 main.sh
echo 'python web.py --skip-requirements-check $@' > web.sh && chmod 700 web.sh
echo '安装已完成，请使用指令"./main.sh"或"./web.sh"，而非"python main.py"或"python web.py"'
