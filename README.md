# deepseek_option_scan

## 项目介绍
`deepseek_option_scan.py` 是一个结合 Nmap 扫描与 DeepSeek AI 分析的网络安全工具。

该工具可以：
1. 运行 Nmap 扫描目标系统。
2. 使用 DeepSeek AI 分析扫描结果，提供改进建议。
3. 允许用户选择优化的扫描参数进行进一步扫描。
4. 自动保存扫描结果。

## 功能特点
- **自动 Nmap 扫描**：支持用户输入目标 IP 或域名，并运行初步扫描。
- **AI 分析与优化**：调用 DeepSeek API 解析 Nmap 结果并提供改进扫描建议。
- **交互式选项选择**：用户可根据 AI 提供的建议选择优化的扫描参数。
- **结果存储**：每次扫描结果都会保存到文本文件。

## 安装与运行
### 依赖项
在运行此脚本之前，请确保安装以下依赖项：

```bash
pip install requests
sudo apt install nmap  # 确保已安装 nmap
```

### 运行脚本
```bash
python3 deepseek_option_scan.py
```

## 参数说明
- `target`：目标 IP 或域名。
- `parameters`：初始 Nmap 扫描参数（默认 `-A`）。
- `API_KEY`：需要替换为你的 DeepSeek API 密钥。

## 使用示例
1. 运行脚本后输入目标 IP 或域名。
2. 初始 Nmap 扫描完成后，调用 DeepSeek API 获取建议。
3. 选择 AI 推荐的扫描参数，进行更深入的扫描。
4. 扫描结果自动保存至 `nmap_scan_option_*.txt`。

## 免责声明
本工具仅用于授权的安全测试，请勿用于非法用途，否则后果自负。

## 许可证
本项目采用 MIT 许可证，详见 LICENSE 文件。

