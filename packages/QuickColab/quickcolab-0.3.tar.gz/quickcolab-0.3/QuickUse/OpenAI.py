import os
import openai
from dotenv import load_dotenv, set_key

class OpenAISDK:
    def __init__(self):
        self.env_file = '.env'
        load_dotenv(self.env_file)
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.base_url = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
        if self.api_key:
            openai.api_key = self.api_key
        openai.api_base = self.base_url
        self.history = []
        
    def set_api_key(self, api_key):
        """設置 API key"""
        self.api_key = api_key
        openai.api_key = api_key
        set_key(self.env_file, 'OPENAI_API_KEY', api_key)
        
    def get_api_key(self):
        """獲取 API key"""
        return self.api_key
    
    def set_base_url(self, base_url):
        """設置 base URL"""
        self.base_url = base_url
        openai.api_base = base_url
        set_key(self.env_file, 'OPENAI_API_BASE', base_url)
        
    def get_base_url(self):
        """獲取 base URL"""
        return self.base_url
    
    def chat_completion(self, message, model="gpt-3.5-turbo", **kwargs):
        """發送聊天請求並更新歷史記錄"""
        self.history.append({"role": "user", "content": message})
        
        params = {
            "model": model,
            "messages": self.history
        }
        params.update(kwargs)
        
        response = openai.ChatCompletion.create(**params)
        assistant_message = response.choices[0].message['content']
        self.history.append({"role": "assistant", "content": assistant_message})
        return assistant_message
    
    def text_completion(self, prompt, model="text-davinci-003", **kwargs):
        """發送文本補全請求"""
        params = {
            "model": model,
            "prompt": prompt
        }
        params.update(kwargs)
        
        return openai.Completion.create(**params)
    
    def get_history(self):
        """獲取對話歷史"""
        return self.history
    
    def clear_history(self):
        """清空對話歷史"""
        self.history = []
    
    def print_usage_guide(self):
        """打印使用指南"""
        print("OpenAI SDK Usage Guide")
        print("======================\n")
        print("1. Set API Key:")
        print("   sdk.set_api_key('your-api-key')")
        print("2. Set Base URL:")
        print("   sdk.set_base_url('https://your-custom-endpoint.com/v1')")
        print("3. Chat Completion:")
        print("   response = sdk.chat_completion('Hello!', temperature=0.7, max_tokens=150)")
        print("4. Text Completion:")
        print("   response = sdk.text_completion('Once upon a time', temperature=0.8, max_tokens=100)")
        print("5. Get Chat History:")
        print("   history = sdk.get_history()")
        print("6. Clear Chat History:")
        print("   sdk.clear_history()")
        print("\nNote: You can pass additional parameters to chat_completion and text_completion methods.")
        print("Current API Key:", self.get_api_key() or "Not set")
        print("Current Base URL:", self.get_base_url())

# 使用示例
sdk = OpenAISDK()
sdk.print_usage_guide()

# 設置 API key
# sdk.set_api_key('your-api-key')

# 設置自定義 base URL
# sdk.set_base_url('https://your-custom-endpoint.com/v1')

# 發送聊天請求，帶有自定義參數
# response = sdk.chat_completion('Hello!', temperature=0.7, max_tokens=150)
# print("Assistant:", response)

# 發送文本補全請求，帶有自定義參數
# response = sdk.text_completion('Once upon a time', temperature=0.8, max_tokens=100)
# print("Completion:", response.choices[0].text)

# 獲取對話歷史
# print("Chat History:", sdk.get_history())

# 清空對話歷史
# sdk.clear_history()
