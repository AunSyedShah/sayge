# JavaScript

This project uses Yarn for JavaScript package management.
Installation: https://yarnpkg.com/getting-started/install

If you'd like to have installed packages/scripts in your PATH add this to your environment:
```shell
export PATH=$PWD/client/node_modules/.bin:$PATH
```

## Project setup

```shell
$ yarn  # installs packages in client/ folder
$ cd client
$ yarn run start
```

To set which API to use you need to set an environment variable:
```shell
export REACT_APP_API_URL=http://localhost:8000/api
```
