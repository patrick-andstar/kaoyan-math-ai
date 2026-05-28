# PaddleOCR API 工具

这个工具用于把本地 PDF、图片或在线文件 URL 交给 PaddleOCR API 解析，并把结果保存成 Markdown 和图片文件。

## 1. 配置 token

推荐把 token 放到环境变量里，不要写进脚本或笔记文件：

```powershell
$env:PADDLEOCR_TOKEN="你的 access token"
```

这只对当前 PowerShell 窗口生效。若要长期保存到当前 Windows 用户环境变量：

```powershell
[Environment]::SetEnvironmentVariable("PADDLEOCR_TOKEN", "你的 access token", "User")
```

重新打开 PowerShell 后生效。

## 2. 异步解析

适合 PDF、页数较多的材料，也支持 URL：

```powershell
python tools\paddleocr_client.py "张宇\split\27张宇基础30讲（高数）-按章修正版\01-第1讲-函数极限与连续.pdf" --mode async --output-dir "张宇\ai笔记\paddleocr\01-第1讲"
```

## 3. 同步解析

只支持本地文件，适合小文件或单张图片：

```powershell
python tools\paddleocr_client.py "path\to\file.pdf" --mode sync --output-dir "output"
```

图片也可以直接使用：

```powershell
python tools\paddleocr_client.py "path\to\page.png" --mode sync --output-dir "output"
```

## 4. 常用选项

- `--orientation`：启用文档方向分类。
- `--unwarping`：启用文档矫正。
- `--chart`：启用图表识别。
- `--no-images`：只保存 Markdown，不下载图片。
- `--file-type pdf|image`：扩展名无法判断时手动指定文件类型。

## 5. 输出结构

默认输出到 `output/`，也可以用 `--output-dir` 指定。

```text
output/
├── doc_0.md
├── doc_1.md
└── ...
```

如果 API 返回 Markdown 内图片或版面截图，脚本会一并下载到输出目录。
