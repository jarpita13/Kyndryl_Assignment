##To install Chrome Driver
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv chromedriver /usr/local/bin/
rm chromedriver_linux64.zip

##To Install Gecko Driver
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
sudo mv /usr/bin/geckodriver /usr/local/bin
rm geckodriver-v0.23.0-linux64.tar.gz

##To install windows Chrome Driver
wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_win32.zip
unzip chromedriver_win32.zip
sudo chmod +x chromedriver
sudo mv chromedriver /usr/local/bin/
rm chromedriver_win32.zip

