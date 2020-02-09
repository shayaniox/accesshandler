# accesshandler

Resource access limit handler

### What does it do?

The **Access Handler** is a web service that stores the _Rules_ user create.
The _Rules_ contains:

- pattern: It can be either an exact explicit url or a regex
- limit: Shows how many times an specific IP can request for an url matched
  the pattern

Also this web service recieves logs by the format of:

```json
{
  "url": "example.com/foo",
  "IP": "1.1.1.1"
}
```

showing the which `IP` requested for `url`.

The goal is to check if an specific `IP` requested more than limit time interval
for specific `url` matched the patterns and inform by `429 Too Many Requests`
HTTP status.

### Installing Dependencies

```bash
sudo apt-get install libass-dev libpq-dev postgresql \
    build-essential redis-server redis-tools
```

### Installing Project by pip

**NOTE:** Highly recommended to use `virtual environment`. There some pip 
packages for this purpose. But I offer you using `virtualenvwrapper` package.

You can install by 'pip install' and use https by the following way:

```bash
pip install git+https://github.com/shayan-7/accesshandler.git
```

Or you can use SSH:

```bash
pip install git+git@github.com:shayan-7/accesshandler.git
```

### Installing Project (edit mode)

So, your changes will affect instantly on the installed version

#### accesshandler

```bash
cd /path/to/workspace
git clone git@github.com:shayan-7/accesshandler.git
cd accesshandler
pip install -e .
```

#### Enabling the bash autocompletion for accesshandler

```bash
echo "eval \"\$(register-python-argcomplete accesshandler)\"" >> $VIRTUAL_ENV/bin/postactivate
deactivate && workon accesshandler
```

### Setup Database

#### Configuration

Accesshandler is zero configuration application and there is no extra
configuration file needed, but if you want to have your own
configuration file, you can make a `accesshandler.yml` in the following
path: `~/.config/accesshandler.yml` such as following format:

```yml
db:
  url: postgresql://postgres:postgres@localhost/accesshandler_dev
  test_url: postgresql://postgres:postgres@localhost/accesshandler_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

```bash
accesshandler db create --drop --mockup
```

#### Drop old database: **TAKE CARE ABOUT USING THAT**

```bash
accesshandler [-c path/to/config.yml] db drop
```

#### Create database

```bash
accesshandler [-c path/to/config.yml] db create
```

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

```bash
accesshandler [-c path/to/config.yml] db create --drop
```

#### Create schema

```bash
accesshandler [-c path/to/config.yml] db schema
```

### Running tests

To check all tests passing and **100%** coverage run the following command:

```bash
pip install -r requirements-ci.txt
pytest --cov=accesshandler
```

### Serving

- Gunicorn

```bash
$ ./gunicorn
```

### Deployment

For deploying the web service follow
the [DEPLOY.md](github.com/shayan-7/accesshandler/deployment/DEPLOY.md)