import google.generativeai as genai


GOOGLE_API_KEY = 'GOOGLE_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')  

def ask_gemini(question):
  response = model.generate_content(question)
  response.resolve()
  return response.text