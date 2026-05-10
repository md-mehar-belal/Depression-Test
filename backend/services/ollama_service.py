import json
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"  # or "llama2", "mistral"

# def generate_recommendation(prediction, confidence, user_data):
#     """
#     Generate mental health recommendation using Ollama
    
#     Args:
#         prediction: 0 (no depression) or 1 (depression)
#         confidence: confidence score (0.0 - 1.0)
#         user_data: dict with user questionnaire responses
    
#     Returns:
#         str: Mental health recommendation/tip
#     """
    
#     try:
#         # Build context from prediction
#         severity = "high" if confidence > 0.7 else "moderate" if confidence > 0.5 else "low"
#         condition = "showing signs of depression" if prediction == 1 else "doing relatively well"

#         # Create prompt for Ollama
#         prompt = f"""Based on the following assessment:
# - Mental Health Status: {condition}
# - Confidence Level: {severity} ({confidence:.2%})
# - User responses indicate patterns related to mood, sleep, and energy levels

# Provide a SHORT, compassionate mental health tip or recommendation (2-3 sentences max):"""
def generate_recommendation(prediction, confidence, user_data):
    try:
        # Map classifier output to severity + condition
        severity_map = {
            0: ("low", "mentally stable"),
            1: ("mild", "showing mild signs of depression"),
            2: ("moderate", "experiencing moderate depression symptoms"),
            3: ("high", "experiencing severe depression symptoms")
        }

        severity, condition = severity_map.get(prediction, ("unknown", "uncertain state"))
        print(f"Generating recommendation for condition: {condition}, severity: {severity}, confidence: {confidence:.2%}")
        # Optional: refine severity using confidence
        if confidence > 0.8:
            confidence_level = "high confidence"
        elif confidence > 0.6:
            confidence_level = "moderate confidence"
        else:
            confidence_level = "low confidence"

        prompt = f"""
        Based on the following assessment:
        - Mental Health Status: {condition}
        - Severity Level: {severity}
        - Model Confidence: {confidence_level} ({confidence:.2%})
        - User responses reflect mood, sleep, and energy patterns

        Provide a SHORT, compassionate, actionable mental health tip (2–3 sentences max).
        Tailor intensity based on severity (gentle for low, more supportive/urgent for high).
        """


        # Call Ollama API
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.7
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"Ollama response: {result.get('response', '')}")
            return result.get("response", "Unable to generate recommendation").strip()
        else:
            return f"Error: Unable to generate recommendation (Status: {response.status_code})"
            
    except requests.exceptions.ConnectionError:
        return "⚠️ Ollama service not running. Please start Ollama first (ollama serve)"
    except requests.exceptions.Timeout:
        return "⚠️ Ollama request timed out. Try again with a smaller model."
    except Exception as e:
        return f"Error generating recommendation: {str(e)}"