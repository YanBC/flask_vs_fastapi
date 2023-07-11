# Run
```
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000 --workers 2
```

In another terminal
```bash
# sudo apt install -y seige
siege http://127.0.0.1:8000
```
