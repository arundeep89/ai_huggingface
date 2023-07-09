from transformers import pipeline 
classifier = pipeline("sentiment-analysis")
res = classifier("I love going to the gym")
print(res)