import requests
from bs4 import BeautifulSoup
import csv

url = "https://djinni.co/jobs/?primary_keyword=python"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("ul", class_="list-unstyled list-jobs mb-4")
    job_cards = job_list.find_all("li", class_="mb-4")

    if job_cards:
        print(f"Found {len(job_cards)} job listings.")

        with open("python_developer_jobs.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Job Title", "Job Link"])

            for job in job_cards:
                title = job.find("a", class_="job-item__title-link").text.strip()
                link = "https://djinni.co" + job.find("a", class_="job-item__title-link")["href"]
                writer.writerow([title, link])

        print("Data has been written to python_developer_jobs.csv")
    else:
        print("No job listings found.")
else:
    print("Failed to retrieve the page")
