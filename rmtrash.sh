sudo apt install trash-cli curl
curl -o /usr/local/bin https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmdirtrash
curl -o /usr/local/bin https://raw.githubusercontent.com/PhrozenByte/rmtrash/master/rmtrash
echo "alias rm='rmtrash'
alias rmdir='rmdirtrash'
alias sudo='sudo '" >> ~/.bashrc
