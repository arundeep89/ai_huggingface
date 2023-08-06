from gradio_client import Client

client = Client("https://arundeep89-blip-api.hf.space/")
result = client.predict(
				"https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg",	# str in 'input' Textbox component
				api_name="/predict"
)
print(result)