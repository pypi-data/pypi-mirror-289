import requests
import re
import json
import socket
import struct

# Replace with your Google Gemini API key
GEMINI_API_KEY = 'AIzaSyBCULLOAqCsE0FRMRLrh2eDRnvbGFfThXE'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def _analyze_script_with_gemini(script):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': (
                    "Analyze the following Roblox Lua script for potential malware or security risks. Make it only roblox related, no ddosing, user data, or etc can be done on roblox."
                    "Identify and list any parts of the script that may be considered harmful, malicious, or suspicious. "
                    "Provide a detailed response outlining each potential threat or behavior that could be considered malware, "
                    "including any specific functions, URLs, or patterns associated with malicious activity. "
                    "\n\nRoblox Lua Script:\n" + script
                )
            }]
        }]
    }
    
    try:
        response = requests.post(
            GEMINI_API_URL,
            headers=headers,
            params={'key': GEMINI_API_KEY},
            json=data
        )
        response.raise_for_status()
        result = response.json()

        # Print full API response for debugging
        print("Full API Response:", json.dumps(result, indent=2))  

        # Extract and return the detailed analysis response
        if 'candidates' in result and len(result['candidates']) > 0:
            # Directly access the detailed analysis
            text = result['candidates'][0].get('content', {}).get('parts', [{}])[0].get('text', '')
            return text
        else:
            # If 'candidates' are not present, look for the analysis text directly
            if 'text' in result:
                return result['text']
        return "No detailed response available."
    except requests.RequestException as e:
        print(f"Error while analyzing with Gemini API: {e}")
        return "Error analyzing script."

def _fetch_script_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching script from URL: {e}")
        return None

def _extract_urls_from_script(script):
    # Regular expression to find URLs in the script
    url_pattern = r'http[s]?://\S+'
    return re.findall(url_pattern, script)

def sim(script):
    try:
        urls = _extract_urls_from_script(script)
        
        if urls:
            print(f"[Roblox Lua]: Found URLs in the script: {urls}")
            for url in urls:
                if url.endswith('.lua'):
                    print(f"[Roblox Lua]: Attempting to load script from: {url}")
                    loaded_script = _fetch_script_from_url(url)
                    if loaded_script:
                        print(f"[Roblox Lua]: Simulating download from URL: {url}")
                        analysis_result = _analyze_script_with_gemini(loaded_script)
                        print(f"[MALWARE DETECTION] For URL content:\n{analysis_result}")
                    else:
                        print(f"[Roblox Lua]: Failed to download or analyze script from URL: {url}")
                    
        # Analyze the original script
        analysis_result = _analyze_script_with_gemini(script)
        if "Error" in analysis_result:
            print(analysis_result)
        else:
            print(f"[MALWARE DETECTION] For original script:\n{analysis_result}")
            
    except Exception as e:
        print(f"An error occurred while analyzing the Lua script: {e}")

def execute(script):
    header = bytearray(16)
    struct.pack_into('<I', header, 8, len(script) + 1)

    try:
        with socket.create_connection(('127.0.0.1', 5553), timeout=3) as s:
            s.sendall(header + script.encode() + b'\x00')
            print('F9 in Roblox to see script activity.')
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
