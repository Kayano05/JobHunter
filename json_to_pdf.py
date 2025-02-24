import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
import os
import platform


def get_system_fonts_path():
    system = platform.system()
    if system == "Darwin":  # macOS
        return [
            "/System/Library/Fonts/",
            "/Library/Fonts/",
            os.path.expanduser("~/Library/Fonts/")
        ]
    elif system == "Windows":
        return [
            "C:\\Windows\\Fonts\\",
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\Windows\\Fonts\\")
        ]
    else:  # Linux
        return [
            "/usr/share/fonts/",
            "/usr/local/share/fonts/",
            os.path.expanduser("~/.fonts/")
        ]


def find_chinese_font():
    chinese_fonts = {
        "Darwin": [  # macOS
            ("STHeiti Light.ttc", "STHeiti"),
            ("STHeiti Medium.ttc", "STHeiti"),
            ("PingFang.ttc", "PingFang"),
            ("Hiragino Sans GB.ttc", "Hiragino"),
            ("SourceHanSansSC-Regular.otf", "SourceHanSans"),
            ("NotoSansCJK-Regular.ttc", "NotoSans"),
        ],
        "Windows": [
            ("simhei.ttf", "SimHei"),
            ("msyh.ttf", "Microsoft YaHei"),
            ("simsun.ttc", "SimSun"),
            ("SourceHanSansSC-Regular.otf", "SourceHanSans"),
            ("NotoSansCJK-Regular.ttc", "NotoSans"),
        ],
        "Linux": [
            ("SourceHanSansSC-Regular.otf", "SourceHanSans"),
            ("NotoSansCJK-Regular.ttc", "NotoSans"),
            ("wqy-microhei.ttc", "WenQuanYi"),
            ("wqy-zenhei.ttc", "WenQuanYi"),
        ]
    }

    system = platform.system()
    font_paths = get_system_fonts_path()

    local_fonts = [
        "SourceHanSansSC-Regular.otf",
        "simhei.ttf",
        "msyh.ttf",
        "simsun.ttc"
    ]
    for font_file in local_fonts:
        if os.path.exists(font_file):
            try:
                font_name = os.path.splitext(font_file)[0]
                pdfmetrics.registerFont(TTFont(font_name, font_file))
                return font_name
            except:
                continue

    for font_dir in font_paths:
        if os.path.exists(font_dir):
            for font_file, font_name in chinese_fonts.get(system, []):
                font_path = os.path.join(font_dir, font_file)
                if os.path.exists(font_path):
                    try:
                        pdfmetrics.registerFont(TTFont(font_name, font_path))
                        return font_name
                    except:
                        continue

    try:
        import urllib.request
        print("正在下载思源黑体...")
        url = "https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf"
        urllib.request.urlretrieve(url, "SourceHanSansSC-Regular.otf")
        pdfmetrics.registerFont(TTFont("SourceHanSans", "SourceHanSansSC-Regular.otf"))
        return "SourceHanSans"
    except:
        print("无法下载思源黑体")

    return None


class JobPdfConverter:
    def __init__(self, json_file, pdf_file):
        self.json_file = json_file
        self.pdf_file = pdf_file
        self.styles = getSampleStyleSheet()

        self.font_name = find_chinese_font()
        if not self.font_name:
            raise Exception("未能找到或安装中文字体，无法继续生成PDF。请按照README中的说明安装中文字体。")

        self.setup_styles()

    def setup_styles(self):

        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#1a468a'),
            fontName=self.font_name
        )

        self.job_title_style = ParagraphStyle(
            'JobTitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceBefore=15,
            spaceAfter=5,
            textColor=colors.HexColor('#2c5282'),
            fontName=self.font_name
        )

        self.info_style = ParagraphStyle(
            'JobInfo',
            parent=self.styles['BodyText'],
            fontSize=12,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor('#4a5568'),
            fontName=self.font_name
        )

    def create_job_section(self, job_data):

        elements = []

        elements.append(Paragraph(job_data['title'], self.job_title_style))

        company_text = f"<b>公司：</b>{job_data['company']}"
        elements.append(Paragraph(company_text, self.info_style))

        salary_text = f"<b>薪资：</b>{job_data['salary']}"
        elements.append(Paragraph(salary_text, self.info_style))

        location_text = f"<b>地点：</b>{job_data['location']}"
        elements.append(Paragraph(location_text, self.info_style))

        elements.append(Spacer(1, 20))
        return elements

    def convert(self):

        with open(self.json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        doc = SimpleDocTemplate(
            self.pdf_file,
            pagesize=A4,
            rightMargin=inch,
            leftMargin=inch,
            topMargin=inch,
            bottomMargin=inch
        )

        elements = []

        title = "职位信息报告"
        elements.append(Paragraph(title, self.title_style))
        elements.append(Spacer(1, 30))

        stats_text = f"共找到 {len(data)} 个职位"
        elements.append(Paragraph(stats_text, self.info_style))
        elements.append(Spacer(1, 20))

        for job in data:
            elements.extend(self.create_job_section(job))

        doc.build(elements)


def convert_jobs_to_pdf(json_file, pdf_file):
    try:
        converter = JobPdfConverter(json_file, pdf_file)
        converter.convert()
        print(f"PDF报告已生成：{pdf_file}")
    except Exception as e:
        print(f"生成PDF时出错：{str(e)}")
        raise


if __name__ == "__main__":
    sample_data = {
        "title": "Java 开发运维工程师",
        "company": "亿迅",
        "salary": "8-12K",
        "location": "北京·朝阳区·798"
    }

    with open('sample.json', 'w', encoding='utf-8') as f:
        json.dump([sample_data], f, ensure_ascii=False, indent=4)

    convert_jobs_to_pdf('sample.json', 'output.pdf')
