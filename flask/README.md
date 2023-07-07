# Run
```
sudo apt update && sudo apt install -y python3-dev
pip install --upgrade pip
pip install -r requirements.txt
uwsgi --http 127.0.0.1:8000 --master -p 2 -w hello:app
```

In another terminal
```bash
# sudo apt install -y seige
siege http://127.0.0.1:8000
```
