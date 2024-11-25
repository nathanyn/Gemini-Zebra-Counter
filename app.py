import google.generativeai as genai
import config
import PIL.Image

genai.configure(api_key=config.API_KEY)

img = PIL.Image.open('image.jpg')
model = genai.GenerativeModel('gemini-1.5-flash')
#response = model.generate_content(img)

response = model.generate_content(["Guestimate the number of zebras in the image", img], stream=True)
response.resolve()

print(response.text)



