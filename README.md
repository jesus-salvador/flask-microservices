# Flask microservices - demo apps
### CRUDs
run the flask app
```python products.py```

### API doc with swagger
open ``swagger_config.yml`` on [Swagger editor](https://editor-next.swagger.io/)
[Find out more about Swagger](http://swagger.io)

### GraphQL
build && run the server
```
    docker build . -t graphqlservice \
    && docker run -dp 8080:4000 graphqlservice
```
