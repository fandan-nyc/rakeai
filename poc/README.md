# local dev and test:
```
cd poc
pip install -r app/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 7111
```
# test in docker:
```
docker build -t api .
docker run -p 80:80 api
```