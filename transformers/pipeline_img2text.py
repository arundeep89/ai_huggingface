from transformers import pipeline

#captioner = pipeline(model="ydshieh/vit-gpt2-coco-en")
captioner = pipeline(model="Salesforce/blip-image-captioning-base")
res = captioner("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
print(res)