import google.generativeai as genai


genai.configure(api_key="USE YOUR OWN KEY ")

def get_gemini_response(question):
    
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"{question}. Keep the answer short and to the point, under 30 words.")
    return response.text.strip()  
