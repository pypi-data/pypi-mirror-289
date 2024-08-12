from .utils import *
from abstract_apis import *
def getCallRequest(endpoint, *args, **kwargs):
  endpoint = make_endpoint(endpoint)
  data = {"signature": args[0]}
  return getPostRequest(getCallUrl(),updateData(data,kwargs),endpoint=endpoint)
def getCallArgs(endpoint):
  return {'getMetaData': ['signature'], 'getPoolData': ['signature'], 'getTransactionData': ['signature'], 'getPoolInfo': ['signature'], 'getMarketInfo': ['signature'], 'getKeyInfo': ['signature'], 'getLpKeys': ['signature'], 'process': ['signature']}.get(get_endpoint(endpoint))
