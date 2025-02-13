#!/usr/bin/env python3
import json
import requests
import subprocess

API_KEY = "替换的api"  # 将此处替换为您的实际 API 密钥

def run_nmap_scan(target, parameters):
    """
    对目标运行 nmap 扫描，并返回结果。
    """
    try:
        command = ['nmap'] + parameters.split() + [target]
        print("执行命令：", " ".join(command))
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("nmap 扫描失败:", e)
        return None

def get_deepseek_analysis_and_suggestions(scan_results):
    """
    调用 DeepSeek API 获取扫描分析和建议。
    """
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    prompt = (
        "以下是 nmap 扫描结果：\n\n"
        f"{scan_results}\n\n"
        "请分析上述 nmap 扫描结果，指出当前扫描中存在的潜在问题或未获取的关键信息，并提供改进建议。"
        "要求输出结果为一个 JSON 对象，格式如下：\n"
        "{\n"
        '  "analysis": "对当前扫描结果的分析",\n'
        '  "options": [\n'
        '    {\n'
        '      "id": 1,\n'
        '      "description": "建议描述",\n'
        '      "nmap_parameters": "nmap 扫描参数"\n'
        '    },\n'
        '    ...\n'
        '  ]\n'
        "}\n"
        "请确保返回的内容仅为 JSON 数据，不要附带其他说明性文本。"
    )
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个经验丰富的网络安全专家，擅长分析 nmap 扫描结果并提出后续扫描建议。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
        "response_format": {"type": "json_object"}
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return content
    except Exception as e:
        print("调用 DeepSeek API 时出错:", e)
        return None

if __name__ == "__main__":
    target = input("请输入目标 IP 或域名: ").strip()
    parameters = "-A"  # 初始扫描参数
    while True:
        scan_result = run_nmap_scan(target, parameters)
        if not scan_result:
            print("nmap 扫描失败，退出。")
            break

        print("调用 DeepSeek API 获取扫描分析和建议，请稍候...\n")
        analysis_and_suggestions_str = get_deepseek_analysis_and_suggestions(scan_result)
        if not analysis_and_suggestions_str:
            print("未能获取扫描分析和建议。")
            break

        try:
            analysis_and_suggestions_json = json.loads(analysis_and_suggestions_str)
        except json.JSONDecodeError as e:
            print("解析 DeepSeek 输出的 JSON 时出错:", e)
            print("DeepSeek 输出内容为:")
            print(analysis_and_suggestions_str)
            break

        analysis = analysis_and_suggestions_json.get("analysis", "无分析结果")
        options = analysis_and_suggestions_json.get("options", [])
        if not options:
            print("未收到任何扫描建议。")
            break

        print("AI 对当前扫描结果的分析：")
        print(analysis)
        print("\n收到以下扫描建议选项：")
        for option in options:
            print(f"选项 {option['id']}: {option['description']}")
            print(f"建议的 nmap 参数: {option['nmap_parameters']}\n")

        choice = input("请输入你选择的选项编号（或输入 'q' 退出）: ").strip()
        if choice.lower() == 'q':
            print("退出扫描流程。")
            break

        selected_option = next((opt for opt in options if str(opt.get("id")) == choice), None)
        if not selected_option:
            print("未找到匹配的选项，退出。")
            break

        parameters = selected_option["nmap_parameters"]
        output_file = f"nmap_scan_option_{selected_option['id']}.txt"
        with open(output_file, "w") as f:
            f.write(scan_result)
        print(f"新的 nmap 扫描完成，结果保存到 {output_file}")
