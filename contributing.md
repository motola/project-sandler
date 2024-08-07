# CONTRIBUTING
 
## Ho to run Docker locally (Volume)

````
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGe_NAMe  sh -c "flask --host 0.0.0.0"
`````