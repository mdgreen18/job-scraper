import requests
from bs4 import BeautifulSoup

def fetch_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    jobs = []
    for job in soup.select("div.card"):
        title = job.select_one("h2.title")
        company = job.select_one("h3.company")
        if title and company:
            jobs.append((title.text.strip(), company.text.strip()))
    return jobs

def display_jobs(jobs):
    print("\n--- Job Listings ---")
    for i, (title, company) in enumerate(jobs, 1):
        print(f"{i}. {title} at {company}")

if __name__ == "__main__":
    url = "https://realpython.github.io/fake-jobs/"
    job_list = fetch_jobs(url)
    display_jobs(job_list)

