set -e
sudo apt install trash-cli
sudo curl -o /usr/local/bin/rmdirtrash https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmdirtrash
sudo curl -o /usr/local/bin/rmtrash https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmtrash
sudo chmod +x /usr/local/bin/rmtrash /usr/local/bin/rmdirtrash
echo "alias rm='rmtrash'
alias rmdir='rmdirtrash'
alias sudo='sudo '" >> ~/.bashrc
sudo bash -c "echo \"alias rm='rmtrash'
alias rmdir='rmdirtrash'
alias sudo='sudo '\" >> /root/.bashrc" #为sudo提供回收站
source ~/.bashrc
