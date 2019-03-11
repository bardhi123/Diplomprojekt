# Diplomprojekt

## Build Algorithm Image
In the root directory of the algorithm project run:
```
docker build . -t algorithm
```

## Build Image
```
docker build . -t diplomprojekt
```

## Run Image
```
docker run -d --rm -p 8000:8000 diplomprojekt
OR
docker-compose up
```

## Point Browser to
```
http://localhost:8000/
```
