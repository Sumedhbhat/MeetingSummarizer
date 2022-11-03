# import torch
# import zipfile
# import torchaudio
# import os
# from glob import glob

# # gpu also works, but our models are fast enough for CPU
# device = torch.device('cpu')
# model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
#                                        model='silero_stt',
#                                        language='en',  # also available 'de', 'es'
#                                        device=device)
# (read_batch, split_into_batches,
#  read_audio, prepare_model_input) = utils  # see function signature for details

# # download a single file in any format compatible with TorchAudio
# speech_file = os.path.join(os.getcwd(), '..', 'Audio', 'out0.wav')
# test_files = glob(speech_file)
# batches = split_into_batches(test_files, batch_size=10)
# input = prepare_model_input(read_batch(batches[0]),
#                             device=device)

# output = model(input)
# for example in output:
#     print(decoder(example.cpu()))
import os
import torch
import subprocess
import tensorflow as tf
import tensorflow_hub as tf_hub
from omegaconf import OmegaConf

language = 'en'  # also available 'de', 'es'

# load provided utils using torch.hub for brevity
_, decoder, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-models', model='silero_stt', language=language)
(read_batch, split_into_batches,
 read_audio, prepare_model_input) = utils

# see available models
torch.hub.download_url_to_file(
    'https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml', 'models.yml')
models = OmegaConf.load('models.yml')
available_languages = list(models.stt_models.keys())
assert language in available_languages

# load the actual tf model
torch.hub.download_url_to_file(
    models.stt_models.en.latest.tf, 'tf_model.tar.gz')
subprocess.run(
    'rm -rf tf_model && mkdir tf_model && tar xzfv tf_model.tar.gz -C tf_model',  shell=True, check=True)
tf_model = tf.saved_model.load('tf_model')

# download a single file in any format compatible with TorchAudio
torch.hub.download_url_to_file(
    'https://opus-codec.org/static/examples/samples/speech_orig.wav', dst='speech_orig.wav', progress=True)
test_files = ['speech_orig.wav']
batches = split_into_batches(test_files, batch_size=10)
input = prepare_model_input(read_batch(batches[0]))

# tf inference
res = tf_model.signatures["serving_default"](
    tf.constant(input.numpy()))['output_0']
print(decoder(torch.Tensor(res.numpy())[0]))
