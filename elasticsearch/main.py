from pprint import pprint
from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()

# host = os.getenv("ELASTIC_SEARCH_URL")

es = Elasticsearch(os.getenv("ELASTIC_SEARCH_URL"), api_key=os.getenv("ELASTIC_SEARCH_API_KEY"))

# es = Elasticsearch(
#     hosts=None,
#  "https://my-elasticsearch-project-fb96fd.es.asia-south1.gcp.elastic.cloud:443",
#  cloud_id=None,
#   api_key=os.getenv("ELASTIC_SEARCH_API_KEY")
# )

client_info = es.info()

pprint("Connected to elastic Search")
print(client_info)
