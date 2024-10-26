from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker

# 配置客户端
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30,  # 每次拉取的时间
    "auth_basic": {"username": "admin", "password": "isqingyu"}
}


# 添加你的业务逻辑
# ...
# 根据业务逻辑的结果标记任务为完成、失败或 BPMN 错误
# failure, bpmn_error = random_true(), random_true()  # 此代码模拟随机失败
# if failure:
#     # 这将标记 Camunda 中的任务为失败
#     return task.failure(error_message="task failed", error_details="failed task details",
#                         max_retries=3, retry_timeout=5000)
# elif bpmn_error:
#     return task.bpmn_error(error_code="BPMN_ERROR_CODE", error_message="BPMN Error occurred",
#                            variables={"var1": "value1", "success": False})
# # 传递任何你想要发送到 Camunda 的输出变量作为字典到 complete()
def handle_task(task: ExternalTask) -> TaskResult:
    is_free = task.get_variable("isFree")
    print("is_free", is_free)
    if is_free is None:
        return task.bpmn_error(error_code="BPMN_NOT_FREE", error_message="完啦",
                               variables={"va1": "error", "success": False})
    elif not is_free:
        return task.failure(error_message="我是python客户端，我不尝试自修",
                            error_details="我是python客户端，我不尝试自修\n异常stacktrace", max_retries=0,
                            retry_timeout=5000)
    else:
        return task.complete({"var1": 1, "var2": "value"})


if __name__ == '__main__':
    worker = ExternalTaskWorker(worker_id="python-client", config=default_config,
                                base_url="http://127.0.0.1:9988/hela/engine-rest")
    worker.subscribe("try_myself_repair", handle_task)
