import requests

def get_qq_data(qq_number):
    api_url = f"https://zy.xywlapi.cc/qqapi?qq={qq_number}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200:
            return data
        else:
            print("API请求失败")
            return None
    except Exception as e:
        print(f"发生异常: {e}")
        return None

def main():
    qq_input = input("请输入QQ号：")
    qq_data = get_qq_data(qq_input)
    
    if qq_data:
        print("API返回数据为：")
        print(qq_data)
    else:
        print("无数据")

if __name__ == "__main__":
    main()
