# referred a lot from 
# https://github.com/Vourhey/pinatapy/blob/master/pinatapy/__init__.py

import typing as tp
import requests
import os
from dotenv import load_dotenv

load_dotenv()
PINATA_KEY = os.getenv("PINATA_KEY")
PINATA_SECRET_KEY = os.getenv("PINATA_SECRET_KEY")

Headers = tp.Dict[str, str]
ResponsePayload = tp.Dict[str, tp.Any]

API_ENDPOINT = "https://api.pinata.cloud/"

class Pinata:
  def __init__(self):
    self._auth_headers: Headers = {
      "pinata_api_key": PINATA_KEY,
      "pinata_secret_api_key": PINATA_SECRET_KEY,

    }

  @staticmethod
  def _error(response: requests.Response) -> ResponsePayload:
    return {"status": response.status_code, "reason": response.reason, "text": response.text}

  # single file, ipfs destination is "/", no options, save absolute paths
  def pin_file_to_ipfs(self, path_to_file: str):
    url: str = API_ENDPOINT + "pinning/pinFileToIPFS"
    headers: Headers = {k: self._auth_headers[k] for k in ["pinata_api_key", "pinata_secret_api_key"]}
    payload: ResponsePayload = {}
    dest_folder_name = "/"

    files: tp.List[str, tp.Any]
    files = [("file", (path_to_file.split("/")[-1], open(path_to_file, "rb")))]
    
    response: requests.Response = requests.post(url=url, files=files, headers=headers, data=payload)
    return response.json() if response.ok else self._error(response)

  def pin_json_to_ipfs(self, json_to_pin: tp.Any):
      url: str = API_ENDPOINT + "pinning/pinJSONToIPFS"
      headers: Headers = self._auth_headers
      headers["Content-Type"] = "application/json"
      payload: ResponsePayload = {"pinataContent": json_to_pin}
      response: requests.Response = requests.post(url=url, json=payload, headers=headers)
      return response.json() if response.ok else self._error(response)  

  