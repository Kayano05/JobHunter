# BOSS直聘职位信息爬虫与PDF生成器

[简体中文](README.md) | [English](docs/README_en.md) | [日本語](docs/README_ja.md) | [Français](docs/README_fr.md) | [Deutsch](docs/README_de.md)

这是一个Python程序，可以自动爬取BOSS直聘网站的职位信息，并生成格式化的PDF报告。

## 功能特点

- 自动爬取BOSS直聘职位信息
- 支持自定义搜索条件（职位、城市、页数）
- 保存原始数据为JSON格式
- 生成美观的PDF格式报告
- 支持中文显示
- 自动处理分页
- 包含职位名称、公司、薪资、地点等信息

## 系统要求

- Python 3.7+
- Chrome浏览器（用于网页爬取）
- macOS/Linux/Windows
- 能够访问 Google 服务的网络环境（由于程序依赖 ChromeDriver 的下载，中国大陆地区使用时需要科学上网）

## 安装步骤

1. 克隆或下载本项目到本地

2. 创建并激活虚拟环境（推荐）：
```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. 安装依赖包：
```bash
pip install -r requirements.txt
```

4. 中文字体设置（如果PDF中文显示乱码）：

对于 macOS 用户：
- 系统通常已经包含所需的中文字体
- 如果出现乱码，可以下载并安装思源黑体：
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

对于 Windows 用户：
- 确保系统安装了中文字体（如微软雅黑或宋体）
- 或下载并安装思源黑体

对于 Linux 用户：
```bash
# Ubuntu/Debian:
sudo apt-get install fonts-wqy-microhei

# CentOS/RHEL:
sudo yum install wqy-microhei-fonts
```

## 使用方法

1. 运行爬虫程序：
```bash
python main.py
```

2. 根据提示输入搜索条件：
```
请输入要查询的职位名称: Python工程师
请输入城市代码（例如北京101010100，默认为北京）: [回车使用默认值]
请输入要爬取的最大页数（默认为5）: [回车使用默认值]
```

3. 常用城市代码参考：
- 北京: 101010100
- 上海: 101020100
- 广州: 101280100
- 深圳: 101280600
- 杭州: 101210100
- 成都: 101270100

## 输出文件

程序会生成两个文件：

1. JSON文件：包含原始数据
   - 文件名格式：`职位名称_城市代码_jobs_时间戳.json`
   - 例如：`Python工程师_101010100_jobs_20240223_172956.json`

2. PDF报告：格式化的职位信息报告
   - 文件名格式：`职位名称_城市代码_jobs_时间戳.pdf`
   - 例如：`Python工程师_101010100_jobs_20240223_172956.pdf`

## PDF报告内容

生成的PDF报告包含：
- 标题页：显示"职位信息报告"
- 统计信息：显示找到的职位总数
- 职位详情：
  - 职位名称（蓝色突出显示）
  - 公司名称
  - 薪资范围
  - 工作地点

## 注意事项

1. 网络环境说明：
   - 程序在启动时需要下载 ChromeDriver，这个过程需要访问 Google 服务器
   - 如果您在中国大陆地区使用，需要确保可以访问 Google 服务（比如使用科学上网工具）
   - 如果无法访问 Google 服务，程序将无法正常启动和运行

2. 爬虫使用说明：
   - 建议每次爬取间隔一定时间
   - 避免频繁大量抓取
   - 建议使用默认的每次5页限制

3. PDF生成说明：
   - 确保系统安装了中文字体
   - PDF文件会自动分页
   - 支持中文和特殊字符

4. 可能遇到的问题：
   - 如果出现验证码，请稍后再试
   - 如果PDF中文显示乱码，请按照上述字体安装说明操作
   - 如果网络连接失败，请检查网络设置
   - 如果提示 ChromeDriver 下载失败，请检查是否可以访问 Google 服务

## 开发计划

- [ ] 添加更多搜索条件支持
- [ ] 优化PDF报告样式
- [ ] 添加数据分析功能
- [ ] 支持导出更多格式

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

MIT License 