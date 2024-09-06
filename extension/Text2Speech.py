import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# Text to speech to a file
tts.tts_to_file(text="你好,我叫小明!", speaker_wav="F:\game\WeChatRobot\extension\\voice.wav", language="zh-cn", file_path="F:\game\WeChatRobot\extension\\output.wav")
speak=input("输入文本:")
tts.tts_to_file(text=speak, speaker_wav="F:\game\WeChatRobot\extension\\voice.wav", language="zh-cn", file_path="F:\game\WeChatRobot\extension\\output2.wav")