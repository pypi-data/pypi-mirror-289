from ursina import *
from .Tool import get_data_from_api
from .Data import color_dict
from datetime import datetime
import sys, requests, uuid, io
from ursina.prefabs.first_person_controller import FirstPersonController
import json
import subprocess
import shutil
import os

############################### Current Time ###############################
current_time = datetime.now()
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
############################################################################

############################### Global Data ################################

ChainApi = {
    "Aptos": "https://vortex-server-three.vercel.app/api/create-entry",
    "Polygon": "https://vortex-server-three.vercel.app/addEntity"
}
OuputJSON = dict()
#--------------------------------------------------------------------------
TempObjects = list()
TempColors = list()
TempFPS = list()    
TempActions = list()  # Store game actions here
#--------------------------------------------------------------------------

ApiCheckerUrl = ["https://vortex-server-three.vercel.app/api/create-entry", "https://vortex-server-three.vercel.app/addEntity/"]

############################################################################

class Vortex:
    def __init__(self, PrivateKey="", Address="", Chain=None, ApiKey=False, **kwargs):
        if ApiKey:
            try:
                for url in ApiCheckerUrl:
                    response = requests.get(url + ApiKey)
                    response.raise_for_status()
                    print(f"API response from {url}: {response.json()}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None
        else:
            self.PrivateKey = PrivateKey
            self.Address = Address
            self.Chain = Chain
            self.app = Ursina(title="Vortex", **kwargs)

            OuputJSON.update({"config": {"Chain": Chain, "appInstance": str(self.app)}})
            print(OuputJSON)

    def Object(self, **kwargs):
        EntityObject = Entity(**kwargs)
        TempObjects.append({"Objects": {"EntityInstance": EntityObject, "Kwargs": kwargs if kwargs else "No Kwargs are used..!"}})
        TempActions.append({"Action": "Create Object", "Details": kwargs})
        return EntityObject
    
    def Label(self, **kwargs):
        TextObject = Text(**kwargs)
        TempObjects.append({"Label": {"TextInstance": TextObject, "Kwargs": kwargs if kwargs else "No Kwargs are used..!"}})
        TempActions.append({"Action": "Create Label", "Details": kwargs})
        return TextObject
    
    def firstPersonController(self, **kwargs):
        fps = FirstPersonController(**kwargs)
        TempObjects.append({"Label": {"TextInstance": fps, "Kwargs": kwargs if kwargs else "No Kwargs are used..!"}})
        TempActions.append({"Action": "Create First Person Controller", "Details": kwargs})
        return fps
    
    def color(self, color_input):
        FinalColor = object()
        if isinstance(color_input, str):
            if color_input.startswith('#'):
                try:
                    FinalColor = color.hex(color_input)
                except ValueError:
                    FinalColor = color.white
            else:
                FinalColor = color_dict.get(color_input, color.white)
        elif isinstance(color_input, tuple) and len(color_input) == 3:
            try:
                FinalColor = color.rgb(*color_input)
            except ValueError:
                FinalColor = color.white
        else:
            FinalColor = color.white
        TempColors.append(FinalColor)
        TempActions.append({"Action": "Set Color", "Color": color_input})
        return FinalColor
    
    def UpdateBlock(self):
        print("hello", json.dumps(str(OuputJSON)))
        try:
            json_string = json.dumps(str(OuputJSON))
            if json_string:
                ipfs_url = self.upload_json_as_file(json_string)
                
                for chain, url in ChainApi.items():
                    if chain == "Polygon":
                        data_payload = {
                            "dataUri": ipfs_url,
                            "privateKey": self.PrivateKey
                        }
                    else:
                        data_payload = {
                            "ipfscontent": ipfs_url,
                            "timestamp": str(datetime.now().isoformat()),
                            "privateKey": self.PrivateKey
                        }

                    headers = {'Content-Type': 'application/json'}
                    
                    # Make the POST request to each chain's API
                    response = requests.post(url, json=data_payload, headers=headers)
                    
                    # Print the response
                    print(f"Response from {chain} API ({url}):", response.status_code, response.text)
            else:
                print(":)")
        except TypeError as e:
            print(f"Serialization error: {e}")

    def upload_json_as_file(self, json_text):
        filename = f"{uuid.uuid4()}.json"
        json_data = json.loads(json_text)        
        json_bytes = json.dumps(json_data).encode('utf-8')
        json_file_like = io.BytesIO(json_bytes)        
        url = "https://api.verbwire.com/v1/nft/store/file"
        files = { "filePath": (filename, json_file_like, "application/json") }
        headers = {
            "accept": "application/json",
            "X-API-Key": "sk_live_0c7597d2-dd10-44c5-8488-fd60859c61f1"
        }        
        
        response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            try:
                ipfs_response = response.json()
                if "ipfs_storage" in ipfs_response and "ipfs_url" in ipfs_response["ipfs_storage"]:
                    return ipfs_response["ipfs_storage"]["ipfs_url"]
                else:
                    print("Unexpected response format:", ipfs_response)
                    return None
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON response: {e}")
                print("Response text:", response.text)
                return None
        else:
            print(f"Failed to upload file to IPFS: {response.status_code} - {response.text}")
            return None

        
    def run(self):
        try:
            OuputJSON.update({"EngineStart": {"AppInstance": str(self.app)}})
            OuputJSON.update({"Objects": {"ListOfObjects": str(TempObjects)}})
            OuputJSON.update({"Colors": {"ListOfColors": str(TempColors)}})
            self.app.run()
        except (KeyboardInterrupt, SystemExit):
            print("Game forcefully stopped.")
        finally:
            self.UpdateBlock()
            sys.exit()
