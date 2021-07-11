sudo apt install trash-cli curl
sudo curl -o /usr/local/bin/rmdirtrash https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmdirtrash
sudo curl -o /usr/local/bin/rmtrash https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmtrash
echo "alias rm='rmtrash'
alias rmdir='rmdirtrash'
alias sudo='sudo '" >> ~/.bashrc
