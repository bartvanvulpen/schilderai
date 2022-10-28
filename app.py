import flask
from flask import Flask, render_template, request, jsonify
import time
from transformers import pipeline
import torch

app = Flask(__name__)


import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image


api_key = "37b86c9b-cad6-4519-bdc5-710b21e9c19e"
model_key = "8c1e5f73-e50e-4246-b71d-d07b8f2d7298"




@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def show_img():  # put application's code here

    # print('clicked!')
    prompt = request.form['prompt_input']


    model_inputs = {
        "prompt": prompt,
        "num_inference_steps": 50,
        "guidance_scale": 9,
        "height": 512,
        "width": 512,
        "seed": 3242
    }

    # Run the model
    out = banana.run(api_key, model_key, model_inputs)

    # Extract the image and save to output.jpg
    image_byte_string = out["modelOutputs"][0]["image_base64"]
    image_encoded = image_byte_string.encode('utf-8')
    # image_bytes = image_encoded.decode('utf-8')
    #
    # print(image_bytes)



    return jsonify({'status': True, 'image': image_byte_string})




#
#
# # Init is ran on server startup
# # Load your model to GPU as a global variable here using the variable name "model"
# def init():
#     global model
#
#     device = 0 if torch.cuda.is_available() else -1
#     model = pipeline('fill-mask', model='bert-base-uncased', device=device)
#
#
# # Inference is ran for every server call
# # Reference your preloaded global model variable here.
# def inference(model_inputs: dict) -> dict:
#     global model
#
#     # Parse out your arguments
#     prompt = model_inputs.get('prompt', None)
#     if prompt == None:
#         return {'message': "No prompt provided"}
#
#     # Run the model
#     result = model(prompt)
#
#     # Return the results as a dictionary
#     return result

if __name__ == '__main__':
    app.run()
