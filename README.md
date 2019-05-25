My implementation of the coding task listed at [https://gist.github.com/VinhCGI/c503ea8a9c7c0b7fe0778dd8b9f42b40](https://gist.github.com/VinhCGI/c503ea8a9c7c0b7fe0778dd8b9f42b40)

This assumes git, Python 3, and Firefox are installed. Implemented and tested in Ubuntu 18.10.

# Installation and execution instructions

+ Install pipenv
```console
pip install --user pipenv
```

+ Install geckodriver (if necessary)
```console
wget -O firefox-driver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xzf firefox-driver.tar.gz
sudo chown root:root geckodriver
sudo mv geckodriver /opt
sudo ln -s /opt/geckodriver /usr/local/bin/geckodriver
rm firefox-driver.tar.gz
```

+ Clone the repo
```console
git clone https://github.com/kvonhorn/cgi-assessment
```

+ Install the packages into the environment
```console
cd cgi-assessment
pipenv install
```

+ Run the tests
```console
pipenv run nosetests tasks.py
```

