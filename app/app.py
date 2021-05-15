#!/usr/bin/env python
import os
from config import app
from controllers.user_controller import api

# register the api
app.register_blueprint(api)

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)
