import whisper

model = whisper.load_model('medium')
result = model.transcribe('en.mp3', fp16=False)
print(result['text'])
