echo 'server starting manually'
python3 worker.py
echo 'worker started  successfully'
gunicorn --bind 0.0.0.0:5000 wsgi:app
echo 'server started in gunicorn successfully'