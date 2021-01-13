# KCAPTCHA Generator

[KCAPTCHA](http://www.captcha.ru/en/kcaptcha/) Generator

__Sample Images__

![Sample Image1]()

![Sample Image2]()

## Prerequisite

- php, php-gd
- python3

### Ubuntu

```sh
sudo apt-get install php7.2-cli php-gd
pip install -r requirements.txt
```

### Windows

```sh
..
pip install -r requirements.txt
```

## Usage

```
python generate.py -h
...
```

### Basic Usage

```sh
python generate.py
```

### Examples

```sh
python generate.py -s 1000 -n 6 --chars abcdefghijklmnopqrstuvwxyz
```