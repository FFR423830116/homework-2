import requests

# 从配置文件读取，不写死在代码里
try:
    from config import ACCESS_TOKEN
except ImportError:
    print("请先创建 config.py 并填写 ACCESS_TOKEN")
    exit()


def ai_ask(prompt):
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={ACCESS_TOKEN}"

    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    return result.get("result", "请求失败")


if __name__ == '__main__':
    print("=" * 50)
    print("     百度AI 智能学习小助手")
    print("  安全版：密钥不写入主程序")
    print("=" * 50)

    while True:
        user_input = input("\n请输入问题（q 退出）：")
        if user_input.lower() == "q":
            break
        print("\nAI 思考中...\n")
        print(ai_ask(user_input))