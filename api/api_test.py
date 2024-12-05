import httpx

BASE_URL = "http://36.103.235.152:18091"  # 替换为你的FastAPI应用的URL

def get_question(question_id, seed=None):
    url = f"{BASE_URL}/get_question/{question_id}"
    if seed is not None:
        url += f"?seed={seed}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("Question(s) retrieved successfully:")
        print(response.json())
    else:
        print(f"Failed to retrieve question(s): {response.status_code}")

def submit_prediction(predictions):
    response = httpx.post(f"{BASE_URL}/submit_prediction", json=predictions)
    if response.status_code == 200:
        print("Prediction submitted successfully:")
        print(response.json())
    else:
        print(f"Failed to submit prediction: {response.status_code}")

def get_incorrect_predictions():
    response = httpx.get(f"{BASE_URL}/incorrect_predictions")
    if response.status_code == 200:
        print("Incorrect predictions retrieved successfully:")
        print(response.json())
    else:
        print(f"Failed to retrieve incorrect predictions: {response.status_code}")

if __name__ == "__main__":
    # 示例用法

    # 使用随机种子获取采样问题
    seed = 42
    get_question("sample", seed=seed)  # 获取采样问题

    question_id = "3a1ef4ef-edb7-48e1-9ec7-da833563d004"
    predictions = [
        {"id": question_id, "predict": "C"},
        {"id": "616e482f-9248-407c-82bd-1e62ef4f9414", "predict": "B"},
        {"id": "0f0c93e4-a132-4efc-bd17-11183165f7e5", "predict": "D"}
    ]
    get_question(question_id) 
    submit_prediction(predictions)

    get_incorrect_predictions()
