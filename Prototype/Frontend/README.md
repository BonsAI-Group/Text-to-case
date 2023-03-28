# Automatic form filling prototype - React frontend
This is a web application for the prototype of the Text-to-case project. It is created with React and uses Python FastAPI as a backend.


## Prerequisites
To run the application, you need to have the following installed:
- Node.js
- Yarn

Node can be installed from [here](https://nodejs.org/en/download).

Once Node is installed, you can install Yarn with:
```
npm install -g yarn
```

## How to install
The application can be installed by executing the following command:
```
yarn install
```

## How to run
To run the application, execute the following command:
```
yarn start
```
NOTE: The application uses OpenAPI documentation to generate code required to communicate with the backend, which is automatically generated when executing this command. If the backend is not running, executing this command will throw an error, but the application will still run. When running the application for the first time, or after making changes to the backend, make sure the backend is running before executing this command. See the section "OpenAPI documentation" for more information.

## OpenAPI documentation
The web application uses automatically generated code based on the OpenAPI documentation of the backend. To regenerate the code, run:
```
yarn open-api
```