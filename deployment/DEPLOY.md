# Deployment instruction on Ubuntu

_**Note:**_ All commands in this file should be executed by the `root` user.
Here we are preparing fresh machine for use.

### Before running the scripts

Uncomment these lines to enable some source in `/etc/apt/sources.list`:

```
deb-src http://archive.ubuntu.com/ubuntu bionic main restricted
deb-src http://archive.ubuntu.com/ubuntu bionic-updates main restricted
```

And then:

``` bash
apt update
apt upgrade
```

### Network configuration

Then, configure network.

#### IPv4 config

Open the `/etc/gai.conf`.
Uncomment the following line starting with `precedence`:

```
# precedence ::ffff:0:0/96 100
```

#### IPv6 Disableing

Open the `/etc/default/grub` and change/add:

From:
```
GRUB_CMDLINE_LINUX_DEFAULT=""
```

To:
```
GRUB_CMDLINE_LINUX_DEFAULT="ipv6.disable=1"
```

Now update grub and reboot:

``` bash
update-grub
reboot
```

### Accesshandler

``` bash
./pre-install.sh
```

#### Configuring nginx and redis to refuse IPv6

To prepare nginx, edit `/etc/nginx/sites-available/default`.
Comment line contains `listen [::]:80 default_server` with `#` like this:

```
# listen [::]:80 default_server
```

To prepare redis, edit ` /etc/redis/redis.conf` and change from:

```
bind 127.0.0.1 ::1
```

To:
```
bind 127.0.0.1
```

Then continue to install:

``` bash
./install.sh
```
