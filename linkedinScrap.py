from selenium import webdriver
from linkedin_scraper import Person, actions, Job ,Company

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--window-size=1920x1080")  # Set window size
# chrome_options.add_argument("--disable-gpu")  # Disable GPU (for compatibility)
# chrome_options.add_argument("--incognito")  # Open in incognito mode

driver = webdriver.Chrome()

# Optionally, log in to LinkedIn (if scraping private profiles)
# actions.login(driver, email="", password="")

person = Person("https://www.linkedin.com/in/arslan-arshad-ai-engineer/", driver=driver)
print(f"Name: {person.name}")
print(f"Job Title: {person.location}")
print(f"Job Title: {person.job_title}")
print(f"Job Title: {person.contacts}")
print(f"Company: {person.company}")
print(f"About: {person.about}")
print(f"Experiences: {person.experiences}")
print(f"Education: {person.educations}")
print(f"Skills: {person.skills}")
print(f"Interests: {person.interests}")
print(f"Recommendations: {person.Recommendations}")
for experience in person.experiences:
    print(f"Title: {experience.title}")
    print(f"Company: {experience.company}")
    print(f"Date Range: {experience.date_range}")
    print(f"Location: {experience.date_posted}")
    print(f"Description: {experience.description}")
    print("-" * 40)
for education in person.educations:
    print(f"School: {education.School}")
    print(f"Degree: {education.Degree}")
    print(f"Field of Study: {education.Field}")
    print(f"Dates Attended: {education.date_range}")
    print("-" * 40)
for skill in person.skills:
    print(f"- {skill}")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMPANY %%%%%%%%%%%%%%%%%%%%%%%%%

company = Company("https://ca.linkedin.com/company/google")

print(f"Job Title: {company.about_us}")
print(f"Company: {company.company_size}")
print(f"Location: {company.company_type}")
print(f"Description: {company.employees}")
print(f"Applicants: {company.linkedin_url}")

print(f"Job Title: {company.name}")
print(f"Company: {company.website}")
print(f"Location: {company.headquarters}")
print(f"Description: {company.specialties}")
print(f"Applicants: {company.get_employees}")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Jobs %%%%%%%%%%%%%%%%%%%%%%%%%

job = Job("https://www.linkedin.com/jobs/view/some-job/", driver=driver)
print(f"Job Title: {job.job_title}")
print(f"Company: {job.company}")
print(f"Location: {job.location}")
print(f"Description: {job.job_description}")
print(f"Applicants: {job.applicant_count}")
print(f"Date Posted: {job.posted_date}")
print(f"Company: {job.benefits}")

# scrape(close_on_complete=True)
driver.quit()