#Copyright © 2021 Maxval Group. All Rights Reserved.
#Unauthorized copying of this file, via any medium is strictly prohibited.
#Proprietary and confidential
#Written by Sonali Rai, September 2021


import requests
import json
from typing import Text

class Constants() :
     "......  constants....."

     CLIENT_ID = "client_id"
     SECRET = "client_secret"
     GRANT_TYPE = "grant_type"
     api_url1 = "https://api-conqa.maxval.com/services/oauth2/token"
     api_url2 = "https://api-qa.maxval.com/v4/pair/identifier/details"

def status(api_url1):

     """ask prmission from MaxVal api 
       
       return status """

     api_url1 = "https://api-conqa.maxval.com/services/oauth2/token"

     client = {"client_id":"be9rtgcpsvjyy70m","client_secret":"6iqwj97xneo75dfj","grant_type":"client_credentials"}

     response =  requests.post(api_url1,data=client)

     print(response.text)
       

def token(api_url2):

     """generating token for sent request  """

     api_url2 = "https://api-qa.maxval.com/v4/pair/identifier/details"

     header={"Authorization":"Bearer RCHxgZExGH_V9EY8ujVwjL3OL724EBlUhrE5EwmQLa5RTe4s2sV8rgtKpdeYdKiuQeKZE_i2e_BEae-oSLu6MJHYhHvD5w6rrTbrZRlMRelhDOo0Vp71PqImNf2GF1XRyuUisjpq9q61avplWV1Dz5bwZ1gIikBWP5CgGD_1U31k_f35OAYGxXAgvqUQtWk0NT9c3ZNI3pMCW9yzw3OfT7fLy86KD7xr9VhpSEbYYF9cu2rwnZIVhHQJvbzQel9WiQRlspcapAwL8POoIJoBKas6sG7CgfogLte_nH9Cyp8 ","Content-Type": "application/json"}

     body = json.dumps({"ClientRequestHandle":"d642c5af-ed1f-47c1-974d-cb652022ce2a","Identifier":[{"number": "US7520435B2", "type": "2"},{"number": "CN110582765A", "type": "2"},{"number": "EP2235987A4", "type": "2"}],"Options":{"ExtractOption":{"Source":"IFI-CLAIMS","Biblio":1,"Litigation": 1,"DownloadImages":0,"TransactionHistory":0,"Ifw":{"extractifw":1,"IncomingCorrespondence":False,"OutgoingCorrespondence":False,"DownloadAllDocument":0,"Document":[ {"Code": "892" }]},"Pta":0,"ContinuityData":0,"Assignments":0},"CacheOption":{"IsCacheEnabled":0,"TimePeriod":24},"WatchOption":{"Frequency":0}}})

     response =  requests.post(api_url2,headers=header)

     print(response.text)


if __name__ == '__main__':
    object_class = Constants()
    status(object_class.api_url1)
    token(object_class.api_url2)