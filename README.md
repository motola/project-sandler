# Store Collection Backend Service

This project is a backend service designed to manage a collection of stores, including their associated items and tags. It provides robust user authentication using JSON Web Tokens (JWT) and is built with Python and Flask. The service facilitates the organization and retrieval of store-related data, ensuring secure and efficient access for authenticated users.

- [Description](#Description)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage](#Usage)
- [API Endpoints](#APIEndpoints)
- [Deployment](#Deployment)
- [Contributing](#Contributing)
- [License](#License)
- [Contact](#Contact)

## Description
This backend service allows users to:

- Create and manage store collections.
- Authenticate using JWT.

## Installation

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the Repository:
`````
git clone https://https://github.com/motola/project-sandler.git
cd project Sandler
``````````
2. Build and run the Docker container::
`````
docker-compose up --build
``````````
3. The service will be available at http://localhost:5000

Dockerfile
`````
FROM python:3.10

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]

``````````
## Installation

### Environment Variables
Create a .env file in the root directory with the following variables:
`````
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///store.db
JWT_SECRET_KEY=your_jwt_secret_key
`````
### Requirements
The project dependencies are listed in requirements.txt:
`````
flask
flask-smorest
python-dotenv
sqlalchemy
flask-sqlalchemy
flask-jwt-extended
passlib
flask-migrate

`````
Install them with:

`````
pip install -r requirements.txt

`````

## Usage
### Running the Service
After setting up the environment variables and installing the dependencies, you can run the service with:

``````
flask run
``````

The service will be available at http://localhost:5000.

## API Endpoints
### User Authentication

- POST /auth/register: Register a new user.
- POST /auth/login: Authenticate a user and return a JWT access and refresh token.
- GET /users: Get all users.

### Store Collection

- GET /store: Get all stores.
- POST /store: Create a new store.
- GET /store/<id>: Get a specific store by ID.
- PUT /store/<id>: Update a store by ID.
- DELETE /store/<id>: Delete a store by ID.

### Item Collection
- GET /item/<id>: Get an Item by ID.
- DELETE /item/<id>: Delete an Item by ID.
- PUT /item/<id>: Update an item by ID.
- GET /item Get all Items
- POST /item Post an Items 

## Deployment
To deploy the application using Docker, ensure Docker and Docker Compose are installed. Then, follow these steps:

1. Build the Docker image:
````
docker-compose build
`````
2. Run the Docker container:
`````
docker-compose up
`````
## Contributing
If you want to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.


## Contact
For questions or comments, please reach out at https://www.akinolaolutola.com


