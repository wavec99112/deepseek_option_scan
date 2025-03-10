# deepseek_option_scan


deepseek_option_scan.py` 是一个结合 Nmap 扫描与 DeepSeek AI 分析的网络安全工具。

本工具仅供合法的网络安全研究、教学和评估用途。请勿在未经授权的系统上使用，任何非法使用本工具的行为，责任自负。

## 功能特点
- **自动检测目标网络**：支持用户输入目标 IP 或域名，并运行初步扫描。
- **AI 分析与优化**：调用 DeepSeek API 解析 Nmap 结果并提供改进扫描建议。
- **交互式选项选择**：用户可根据 AI 提供的建议选择优化的扫描参数。
- **结果存储**：每次扫描结果都会保存到文本文件。

## 克隆仓库
```bash
git clone https://github.com/wavec99112/deepseek_option_scan.git
cd deepseek_option_scan
```

## 安装
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

## 使用说明
1. 运行脚本后输入目标 IP 或域名。
2. 初始 Nmap 扫描完成后，调用 DeepSeek API 获取建议。
3. 选择 AI 推荐的扫描参数，进行更深入的扫描。
4. 扫描结果自动保存至 `nmap_scan_option_*.txt`。

## 贡献指南
如果你想要贡献代码或报告问题，欢迎提交 Pull Request 或 Issue：

1. Fork 本仓库
2. 创建新的分支 (`git checkout -b feature-branch`)
3. 提交你的修改 (`git commit -am 'Add new feature'`)
4. 推送到分支 (`git push origin feature-branch`)
5. 创建一个新的 Pull Request

## 免责声明
本工具仅供合法的网络安全研究、教学和评估用途。请勿在未经授权的系统上使用，任何非法使用本工具的行为，责任自负。

## 许可证
版权所有 (c) 2024 WAVE-C9

特此免费授予获得本软件及相关文档文件（“软件”）副本的任何人无限制地处理本软件的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，以及允许向其提供本软件的人这样做，但须符合以下条件：

本软件按“原样”提供，不提供任何明示或暗示的担保，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人均不对因本软件或使用本软件或其他交易中的使用或其他交易而产生的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权行为或其他方面。

## 维护者
Wave-C9
