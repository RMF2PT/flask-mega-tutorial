#!/home/ubuntu/.virtualenvs/venv1/bin/python
import os
from app import app
#app.run(debug=True)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)),debug=True)
