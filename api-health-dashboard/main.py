import json
import time
import requests


def load_targets():
    """
    读取 targets.json 文件中的接口配置。
    返回值是一个列表，列表中每个元素都是一个字典，
    里面保存了一个待检测接口的基本信息。
    """
    with open("targets.json", "r", encoding="utf-8") as f:
        return json.load(f)


def check_target(target):
    """
    检测单个接口的状态。

    参数：
        target: 一个字典，包含 name、url、method、timeout 等字段

    返回：
        result: 一个字典，记录本次检测结果
    """
    name = target.get("name", "未命名接口")
    url = target.get("url", "")
    method = target.get("method", "GET").upper()
    timeout = target.get("timeout", 5)

    # 记录开始时间，用来计算请求耗时
    start_time = time.time()

    try:
        # 当前第一版只支持 GET 请求
        if method == "GET":
            response = requests.get(url, timeout=timeout)
        else:
            raise ValueError(f"暂不支持的请求方式：{method}")

        # 计算响应时间
        response_time = time.time() - start_time

        # 这里根据状态码判断接口是否健康
        # 一般来说，200~399 可以视为成功
        status_code = response.status_code
        is_success = 200 <= status_code < 400

        result = {
            "name": name,
            "url": url,
            "method": method,
            "success": is_success,
            "status_code": status_code,
            "response_time": round(response_time, 3),
            "error": ""
        }

    except Exception as e:
        # 如果请求失败，则记录异常信息
        response_time = time.time() - start_time

        result = {
            "name": name,
            "url": url,
            "method": method,
            "success": False,
            "status_code": None,
            "response_time": round(response_time, 3),
            "error": str(e)
        }

    return result


def save_results(results):
    """
    将所有检测结果保存到 results.json 文件中。
    """
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


def print_result(result):
    """
    将单个接口的检测结果打印到终端。
    """
    if result["success"]:
        print(
            f"[成功] {result['name']} | 状态码: {result['status_code']} | "
            f"耗时: {result['response_time']} 秒"
        )
    else:
        if result["status_code"] is not None:
            print(
                f"[失败] {result['name']} | 状态码: {result['status_code']} | "
                f"耗时: {result['response_time']} 秒"
            )
        else:
            print(
                f"[失败] {result['name']} | 错误信息: {result['error']} | "
                f"耗时: {result['response_time']} 秒"
            )


def main():
    """
    主函数：
    1. 读取待检测接口
    2. 依次检测每个接口
    3. 打印结果
    4. 保存结果
    5. 输出统计信息
    """
    print("开始进行 API 健康检查...\n")

    # 读取待检测接口列表
    targets = load_targets()

    # 用列表保存所有检测结果
    results = []

    # 依次检测每一个接口
    for target in targets:
        result = check_target(target)
        results.append(result)
        print_result(result)

    # 将结果保存到本地文件
    save_results(results)

    # 统计信息
    total_count = len(results)
    success_count = sum(1 for r in results if r["success"])
    fail_count = total_count - success_count

    print("\n检测完成，结果已保存到 results.json 文件中。")
    print("========== 检测统计 ==========")
    print(f"接口总数：{total_count}")
    print(f"成功数量：{success_count}")
    print(f"失败数量：{fail_count}")

    # 输出失败接口明细
    if fail_count > 0:
        print("\n失败接口如下：")
        for r in results:
            if not r["success"]:
                if r["status_code"] is not None:
                    print(f"- {r['name']}（状态码：{r['status_code']}）")
                else:
                    print(f"- {r['name']}（错误：{r['error']}）")


if __name__ == "__main__":
    main()