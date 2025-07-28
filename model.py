import onnxruntime as ort
import threading

model_lock = threading.Lock()
session = None
input_name = None
output_name = None

def load_model(model_path):
    global session, input_name, output_name
    with model_lock:
        session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name

def run_inference(input_tensor):
    with model_lock:
        return session.run([output_name], {input_name: input_tensor})

def get_lock():
    return model_lock
