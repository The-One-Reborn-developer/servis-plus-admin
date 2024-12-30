# Servis Plus Admin

Admin panel for the [Servis Plus WebApp](https://github.com/The-One-Reborn-developer/servis-plus-dev)

[Dev](https://servisplus-admin-development.mooo.com:10443) | [Demo](https://servisplus-admin-demo.mooo.com:11443)

## Features

* Display database table content.

## Dependencies

* [flask](https://flask.palletsprojects.com/en/3.0.x/)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [nginx](https://nginx.org/en/)
* [certbot](https://certbot.eff.org/)
* [python3-certbot-nginx](https://github.com/certbot/certbot/tree/main/certbot-nginx)
* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)

## Branches and Environments

* dev (develop)
* demo (demo)
* prod (master)

Setup the .env for branches:

```bash
sudo bash launchers/git_scripts.sh
```

## Running

```bash
sudo bash launchers/{choose environment}.sh
```
