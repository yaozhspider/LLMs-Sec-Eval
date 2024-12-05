###接口地址
http://36.103.235.152:18093
### 接口说明
#### 1. 获取问题接口
路径: /get_question/{id}
方法: GET
参数:
id (路径参数): 问题的ID，可以是具体的ID、sample（获取采样问题）。
seed (查询参数，可选): 用于采样问题的随机种子，默认为42。
返回:
如果id为具体问题ID，返回该问题的详细信息。
如果id为sample，返回采样的问题列表。
错误:
如果问题ID不存在，返回404错误。
#### 2. 提交预测接口
路径: /submit_prediction
方法: POST
请求体:
predictions (JSON数组): 包含预测的列表，每个预测包含id和predict字段。
返回:
source_accuracy: 每个问题来源的正确率。
average_accuracy: 所有预测的平均正确率。
错误:
如果问题ID不存在，返回404错误。
#### 3. 获取错误预测接口
路径: /incorrect_predictions
方法: GET
返回:
incorrect_ids: 包含所有错误预测的问题ID列表。

### 示例
#### 获取采样问题
GET /get_question/sample?seed=42
#### 提交预测
POST /submit_prediction
Content-Type: application/json

[
  {"id": "q1", "predict": "A"},
  {"id": "q2", "predict": "B"}
]
#### 获取错误预测
GET /incorrect_predictions
