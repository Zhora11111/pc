import io
from PIL import Image
from fastapi.responses import StreamingResponse
@app.get('/images/thumbnail/{filename}',
  response_description="Returns a thumbnail image from a larger image",
  response_class="StreamingResponse",
  responses= {200: {"description": "an image", "content": {"image/jpeg": {}}}})
def thumbnail_image (filename: str):
  # read the high-res image file
  image = Image.open(filename)
  # create a thumbnail image
  image.thumbnail((100, 100))
  imgio = io.BytesIO()
  image.save(imgio, 'JPEG')
  imgio.seek(0)
  return StreamingResponse(content=imgio, media_type="image/jpeg")
import numpy 
 
 
array =[10, 20, 30, 40, 50, 20, 40] 
single_random_choice = numpy.random.choice(array, size=1) 
print("один случайный выбор из массива 1-D", single_random_choice) 
 
multiple_random_choice = numpy.random.choice(array, size=3, replace=False) 
print("несколько случайных выборов из массива 1-D без замены", multiple_random_choice) 
 
multiple_random_choice = numpy.random.choice(array, size=3, replace=True) 
print("несколько случайных выборов из массива 1-D с заменой", multiple_random_choice)
/*
Ancient Scripts by Leaf Garland
*/
 
background { hue 40 sat 0.2 b -0.2}
 
startshape LINES
 
rule LINES {
    20 * {y -90} NEWLINE {hue 90 sat 0.7 b 0.2 a -0.5}
}
 
rule NEWLINE {
    LINE {y 0}
}
 
rule NEWLINE {
    LINE {y 20}
}
 
rule NEWLINE {
    LINE {y 30}
}
 
rule LINE {
    50 * {x 36} CHAR {}
}
 
rule CHAR 0.3 { 
    // space
}
 
rule CHAR {
    2 * {x 20 flip 180} STROKE {r 90}
    2 * {y 20 flip 180} STROKE {}
}
 
rule CHAR {
    4 * {r 60} STROKE {}
}
 
rule CHAR {
    STROKE {r 90}
    3 * {y 10 flip 180} STROKE {}
}
 
rule STROKE {
    B {}
}
 
rule STROKE {
    B {flip 90}
}
 
rule B 30 {
    MARK {}
    B {x .6 r 10}
}
 
rule B 30 {
    MARK {}
    B {x .6 r 3}
}
 
rule B 250 {
    MARK {}
    B {x .9}
}
 
rule B 10 {
    MARK {}	
    B {flip 90}
}
 
rule B 10 { }
 
 
rule MARK 3 {
    CIRCLE {}
}
 
rule MARK {
    CIRCLE {s 2}
}
 
rule MARK {
    SQUARE {s 3}
}
 
rule MARK {
    CIRCLE {s 4}
}
 
rule MARK 0.01 {
    CIRCLE {s 7}
}import requests

oauth_url = 'http://localhost/api/v1/login/access-token'
data = {
    'grant_type': '',
    'username': 'some_username',
    'password': 'some_password',
    'scope': '',
    'client_id': '',
    'client_secret': ''
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}
response = requests.post(oauth_url, data=data, headers=headers)
response = response.json()
public function save($file, $quality = 90) {
if (is_resource($this->image)) {
            if ($extension == 'jpeg' || $extension == 'jpg') {
                imagejpeg($this->image, $file, 90);
                iport http.server
import socketserverhandler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 1234), handler) as httpd:
	httpd.serve_forever()
server{
       server_name <your-site-name>;
       location / {
           include proxy_params;
           proxy_pass http://127.0.0.1:8000;
       }
}	
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
