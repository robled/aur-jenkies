# aur-jenkies
Templates to build Arch Linux AUR packages with Jenkins

## Installation
```
pip install jenkins-job-builder>=1.4
git clone https://github.com/robled/aur-jenkies.git
```

## Usage

Create a file in the project directory named **packages.yaml.inc** and include your list of packages like so:

```
- devilspie2
- pam-krb5
- geteltorito
```

![jenkies.png](jenkies.png "JENKIES!")
