import requests as req
import time

class Error(Exception):
    def __init__(self, message):
        self.message = message
    
class Prodia:
    def __init__(self, prompt, model="absolutereality_v181.safetensors [3d9d4d2b]", aspect_ratio="square", negative_prompt='', steps=25, cfg=7, seed=time.time(), sampler="DPM++ 2M Karras"):
        self.prompt = prompt
        self.model = model
        self.aspect_ratio = aspect_ratio
        self.negative_prompt = negative_prompt
        self.steps = steps
        self.cfg = cfg
        self.seed = seed
        self.sampler = sampler
    
    def get_link(self):
        return f"https://api.prodia.com/generate?new=true&prompt={self.prompt}&model={self.model}&negative_prompt={self.negative_prompt}&steps={self.steps}&cfg={self.cfg}&seed={self.seed}&sampler={self.sampler}&aspect_ratio={self.aspect_ratio}"
      
    def generate_image(self):
        link = self.get_link()
        response = req.get(link)
        response = response.json()
        self.jobID = response["job"]
        self.status = response["status"]
        polling = self.poll_req()
        return polling
    
    def poll_req(self):
        try:
            polling = True
            while polling:
                response = req.get(f"https://api.prodia.com/job/{self.jobID}")
                status = response.json()
                if status["status"] == "generating":
                    time.sleep(5)
                    print(f"Status: Generating, Polling Once More")
                    continue
                elif status["status"] == "succeeded":
                    return f"https://images.prodia.xyz/{self.jobID}.png?download=1"
                else:
                    raise Error("Unexpected status when polling")   
        except Error as e:
            print("Error Occurred")
            print(e)

x = Prodia(prompt="Pretty girl, cute")
result = x.generate_image()
print(result)