import os
import openai
from dotenv import load_dotenv

# evnファイルを読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.environ['OPENAI_API_KEY']

# プロンプトを入力
prompt = input('prompt : ')

# プロンプトを送信
response = openai.Completion.create(
    model='text-davinci-003',
    max_tokens=1024,
    prompt=prompt
)

# レスポンスを取得、表示
response_text = response.choices[0].text
print(response_text)