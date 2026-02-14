from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyAah2MOTVDX1VnkCbLLfA8kFfqK42viVjU"))


def generate_sql(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Convert this to SQL only: {prompt}"
        )

        return response.text.strip()

    except Exception as e:
        return "Error: API limit or model issue. Try later." 