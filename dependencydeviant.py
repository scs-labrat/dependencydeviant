import requests
from bs4 import BeautifulSoup
import csv

def get_unique_urls(dependency_name):
    query = f"site:github.com {dependency_name}"
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = set()
    for a_tag in soup.find_all('a', href=True):
        if 'url?q=https://github.com' in a_tag['href']:
            url = a_tag['href'].split('url?q=')[1].split('&')[0]
            urls.add(url)
    return urls

def main():
    with open('dependencies.txt', 'r') as file:
        dependencies = [line.strip() for line in file]
    
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Dependency', 'URL'])
        
        for dependency in dependencies:
            print(f'Processing {dependency}...')
            urls = get_unique_urls(dependency)
            for url in urls:
                writer.writerow([dependency, url])
            print(f'Done with {dependency}.')
            
if __name__ == "__main__":
    main()
