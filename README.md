[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker">
  </a>

  <h3 align="center">FastAPI + PostgreSQL + PgAdmin + JWT Authentication + Docker-Compose</h3>

  <p align="center">
    Boilerplate code for quick docker implementation of REST API with JWT Authentication using FastAPI, PostgreSQL and PgAdmin.
    <br />
    <br />
    <a href="https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![https://reddimohan.github.io][product-screenshot]]()

### Built With

* [FastAPI](https://fastapi.tiangolo.com)
* [PostgreSQL - postgres12](https://hub.docker.com/_/postgres)
* [PgAdmin](https://hub.docker.com/r/dpage/pgadmin4)
* [jwt](https://jwt.io)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites - Ubuntu
Install Docker and docker-compose
* Docker - Click [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) for installation steps for Ubuntu.
* docker-compose - Click [here](https://docs.docker.com/compose/install) to Install by selecting Linux tab in the page.
* Create a copy of `api/.env` file from `api/.env.template` and update all the parameters.



### Installation

1. Clone the repo
```sh
git clone https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.git
```
2. Install Docker and docker-compose - links provided above
3. Go to project folder and Build the docker images
```sh
docker-compose build
```
4. Bring up the docker-compose to access the API
```sh
docker-compose up -d # It brings up the all services in the docker-compose.yaml including postgres and pgadmin
```
5. You can access the Rest Service and PgAdmin GUI using below ports
```sh
docker ps # It gives the list of running containers with their ports
```
```sh Output
CONTAINER ID        IMAGE                                                             COMMAND                  CREATED             STATUS              PORTS                           NAMES
2ab9e521b530        fastapi-restapi-postgresql-pgadmin-authentication-docker_server   "uvicorn main:app --…"   5 minutes ago       Up 5 minutes        0.0.0.0:9000->8000/tcp          api_service

57ecb3d87421        dpage/pgadmin4                                                    "/entrypoint.sh"         5 minutes ago       Up 5 minutes        443/tcp, 0.0.0.0:5050->80/tcp   pgadmin

ab8487f8a0a7        postgres:12                                                       "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        0.0.0.0:5499->5432/tcp          postgres_db
```
#### Now API and PgAdmin can be accessed from 9000 and 5050, mentioned below
* API - http://0.0.0.0:9000/docs
* PgAdmin - http://0.0.0.0:5050

## Docker Commands for debugging

##### Bring up the all containers
```sh
docker-compose up -d # It brings up the all services in the docker-compose.yaml including postgres
```
##### Bring down the all containers which stops API service, postgresql and pgadmin
```sh
# Locate docker-compose.yaml file and go to that directory
docker-compose down
```
##### Login to postgres container
```sh
docker-compose run pgdb bash # to bring up the terminal
```
##### Connect to database database in console after Login to postgres container
```sh
psql --host=pgdb --username=<username> --dbname=<password>
```
You can find the `host` `username` `password` from the `.env` file which should be configured in first place

```sh
# Postgres
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db_name>
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mohan - [LinkedIn](https://linkedin.com/in/reddimohan) - [Twitter](https://twitter.com/reddimohan)

Project Link: [https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker](https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.svg?style=flat-square
[contributors-url]: https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.svg?style=flat-square
[forks-url]: https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/network/members
[stars-shield]: https://img.shields.io/github/stars/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.svg?style=flat-square
[stars-url]: https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/stargazers
[issues-shield]: https://img.shields.io/github/issues/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.svg?style=flat-square
[issues-url]: https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/issues
[license-shield]: https://img.shields.io/github/license/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker.svg?style=flat-square
[license-url]: https://github.com/reddimohan/FastAPI-RestAPI-PostgreSQL-PgAdmin-Authentication-docker/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/reddimohan
[product-screenshot]: apidocs.png

