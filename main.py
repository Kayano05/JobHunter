import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from json_to_pdf import convert_jobs_to_pdf


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    try:

        driver_path = ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        service = Service(executable_path=driver_path)

        print(f"使用 ChromeDriver 路径: {driver_path}")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        print(f"ChromeDriver 启动失败: {str(e)}")
        print(f"请确保已安装最新版本的 Chrome 浏览器")
        raise


def crawl_job_info(driver, job_title, city_code="101010100", max_pages=5):
    base_url = f"https://www.zhipin.com/web/geek/job?query={job_title}&city={city_code}"
    driver.get(base_url)
    time.sleep(random.uniform(3, 5))
    job_list = []
    page = 1

    while page <= max_pages:
        print(f"正在爬取第 {page} 页...")
        try:

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".job-card-wrapper"))
            )

            job_cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-wrapper")
            for card in job_cards:
                try:
                    title = card.find_element(By.CSS_SELECTOR, ".job-name").text
                    company = card.find_element(By.CSS_SELECTOR, ".company-name").text
                    salary = card.find_element(By.CSS_SELECTOR, ".salary").text
                    location = card.find_element(By.CSS_SELECTOR, ".job-area").text
                    job_list.append({
                        "title": title,
                        "company": company,
                        "salary": salary,
                        "location": location
                    })
                except Exception as e:
                    print(f"解析职位卡片时出错: {str(e)}")

            print(f"第 {page} 页爬取完成，当前共爬取到 {len(job_list)} 个职位")

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, ".ui-icon-arrow-right")
                if "disabled" in next_button.find_element(By.XPATH, "..").get_attribute("class"):
                    print("已到达最后一页")
                    break
                next_button.click()
                time.sleep(random.uniform(3, 5))
                page += 1
            except Exception as e:
                print(f"翻页时出错: {str(e)}")
                break

        except Exception as e:
            print(f"爬取第 {page} 页时出错: {str(e)}")
            break

    return job_list


def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"数据已保存到 {filename}")
        return filename
    except Exception as e:
        print(f"保存文件时出错: {str(e)}")
        return None


def main():
    driver = setup_driver()
    try:
        job_title = input("请输入要查询的职位名称: ")
        city_code = input("请输入城市代码（例如北京101010100，默认为北京）: ") or "101010100"
        max_pages = int(input("请输入要爬取的最大页数（默认为5）: ") or 5)

        print(f"正在爬取 {job_title} 在 {city_code} 的职位信息...")
        result = crawl_job_info(driver, job_title, city_code, max_pages)

        if result:

            timestamp = time.strftime('%Y%m%d_%H%M%S')
            json_filename = f"{job_title}_{city_code}_jobs_{timestamp}.json"
            pdf_filename = f"{job_title}_{city_code}_jobs_{timestamp}.pdf"

            if save_to_json(result, json_filename):

                convert_jobs_to_pdf(json_filename, pdf_filename)
                print(f"\n处理完成:")
                print(f"1. JSON文件：{json_filename}")
                print(f"2. PDF报告：{pdf_filename}")
                print(f"\n共爬取到 {len(result)} 个职位")
                print("\n爬取结果预览（前3个）:")
                for job in result[:3]:
                    print(f"职位: {job['title']}")
                    print(f"公司: {job['company']}")
                    print(f"薪资: {job['salary']}")
                    print(f"地点: {job['location']}")
                    print("-" * 30)
        else:
            print("未获取到数据，请检查网络连接或查询条件")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
