import sys
import os

from config import OPENAPI_AUTOGEN_DIR

if not os.path.exists(OPENAPI_AUTOGEN_DIR):
    print("Folder '{}' not found.  "
          "Execute openapi-generator to generate it, "
          "e.g.,".format(OPENAPI_AUTOGEN_DIR))
    print()
    print("  "
          "java -jar openapi-generator-cli-4.3.1.jar generate \\\n"
          "     -i openapi/covid-api.yaml \\\n"
          "     -o {} -g python-flask".format(OPENAPI_AUTOGEN_DIR))
    print()
    exit(1)

sys.path.append(OPENAPI_AUTOGEN_DIR)

try:
    import connexion
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    exit(1)

from openapi_server import encoder

app = connexion.App(__name__, )
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi/covid-api.yaml')
app.run(port=9000, debug=True)

