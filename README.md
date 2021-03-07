# fastapi-nginx-unit
A simple 'hello world' app of FastAPI running on NGINX Unit App server using ASGI.

## Running on Docker
```bash
docker-compose up --build
```
After that you can test using `curl` command.
```bash
curl http://localhost
```

## Running test cases (docker)
```bash
# Run the docker server if you haven't started it yet then run below command for executing test cases
docker-compose exec api pytest /fastapi
```

## Running from terminal
1. Create venv in your project directory and install fastapi
```bash
$ python3 -m venv apienv
$ source apienv/bin/activate
(venv)$ pip install --upgrade pip
(venv)$ pip install -r requirements.txt
$ deactivate
```
2. Run the following command for each directory containing app code or data so Unit can access it:
```bash
(venv)$ sudo chown -R unit:unit /path/to/app/
```
3. Create a JSON configuration file containing information about application.
```json
// config.json
{
    "listeners": {
        "*:80": {
            "pass": "applications/fastapi"
        }
    },

    "applications": {
        "fastapi": {
            "type": "python 3.x",
            "path": "/path/to/app/",
            "home": "/path/to/app/venv/",
            "module": "asgi",
            "callable": "app"
        }
    }
}
```
4. Run the server
```bash
(venv)$ unitd
```
5. Push the configurations json file on server
```bash
(venv)$ sudo curl -X PUT --data-binary @config.json --unix-socket \
       /path/to/control.unit.sock http://localhost/config/
```
6. Testing (terminal)
```bash
(venv)$ pytest .
```