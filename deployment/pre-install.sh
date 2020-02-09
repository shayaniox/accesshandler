#!/usr/bin/env bash

# Install apt dependencies
apt-get install -y libass-dev libpq-dev postgresql build-essential \
redis-server redis-tools git nginx python3-pip

# Ensure about python3.6 and pip3.6
pip3 install --upgrade pip
python3.6 --version
if [ $? != 0  ] ; then
	echo python is not installed !;
	exit 127;
fi
pip3.6 --version > /dev/null
if [ $? != 0  ] ; then
	echo  pip is not installed !;
	exit 127;
fi

# Prepare machine
mkdir -p /etc/accesshandler
mkdir -p /usr/local/accesshandler
groupadd --system accesshandler
useradd --system -g accesshandler accesshandler
echo "d /run/accesshandler 0755 accesshandler accesshandler -" > /usr/lib/tmpfiles.d/accesshandler.conf
systemd-tmpfiles --create
systemctl daemon-reload
systemctl enable redis-server
systemctl enable nginx
grep "listen_addresses\s*=\s*''" /etc/postgresql/10/main/postgresql.conf
if [[ ! $? -eq 0 ]] ; then
	echo "listen_addresses = ''" >> /etc/postgresql/10/main/postgresql.conf
fi
echo "CREATE USER accesshandler" | sudo -u postgres psql
echo "CREATE DATABASE accesshandler OWNER accesshandler" | sudo -u postgres psql
service postgresql restart

