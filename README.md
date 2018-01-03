# flask-docker
Fast and easy way to ship Python web apps, anywhere. Be shipping 🚀

Building apps using Python is fun.
But shipping them, not so much (unlike PHP & NodeJS, which are supported almost everywhere)
However, Docker makes it really easy, here is how:

- `Flask`: Web app framework. You could take any other WSGI framework
- `Gunicorn`: Production grade App server for Python
- `Whitenoise`: Serving static files (js, css, images etc)
- `Docker`: Contenarize codebase + all of the above tech to ship


## Ship

In few steps, you can run on local, your colleague's local, AWS, Azure, anywhere.
See `Dockerfile`

Docker Container -> Container Registry -> Cloud

First build container:
* `docker build . -t flask-docker:0.1`

Test local container:
* Run: `docker run -p 8000:8000 flask-docker:0.1`
* Open: `http://localhost:8000`

If you want to deploy in the cloud:
* Tag it: `docker tag flask-docker:0.1 container_registry.com/flask-docker:0.1`
* Push to remote container registry: `docker push container_registry.com/flask-docker:0.1`
* Run in remote server: `docker run -d -p 80:8000 flask-docker:0.1`

See `Dockerfile` for more detail.
