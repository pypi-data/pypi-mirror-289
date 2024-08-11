import re
from typing import Dict, Any
import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def get_paper_details(url: str) -> Dict[str, Any]:
    if "arxiv.org" in url:
        return await get_arxiv_details(url)
    elif "pubmed.ncbi.nlm.nih.gov" in url:
        return await get_pubmed_details(url)
    else:
        raise ValueError("Unsupported URL")

async def get_arxiv_details(url: str) -> Dict[str, Any]:
    arxiv_id = re.search(r"(?:arxiv\.org/abs/)(.+)", url).group(1)
    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            soup = BeautifulSoup(await response.text(), "lxml-xml")

            entry = soup.find("entry")
            title = entry.find("title").text
            authors = [author.find("name").text for author in entry.find_all("author")]
            abstract = entry.find("summary").text

            return {
                "id": arxiv_id,
                "title": title,
                "authors": authors,
                "abstract": abstract,
            }

async def get_pubmed_details(url: str) -> Dict[str, Any]:
    pubmed_id = re.search(r"(?:pubmed\.ncbi\.nlm\.nih\.gov/)(\d+)", url).group(1)
    summary_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pubmed_id}&retmode=json"
    abstract_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pubmed_id}&retmode=xml"

    async with aiohttp.ClientSession() as session:
        async with session.get(summary_url) as response:
            summary_data = await response.json()
            result = summary_data["result"][pubmed_id]

        async with session.get(abstract_url) as response:
            abstract_xml = await response.text()
            abstract_soup = BeautifulSoup(abstract_xml, "lxml-xml")
            abstract = abstract_soup.find("AbstractText")
            abstract_text = abstract.text if abstract else "Abstract not available"

        title = result["title"]
        authors = result["authors"]

        return {
            "id": pubmed_id,
            "title": title,
            "authors": [f'{author["name"]}' for author in authors],
            "abstract": abstract_text,
        }


async def pubmed_to_pdf_url(url, session):
    print("url", url)
    pubmed_id = url.split("/")[-1]

    async with session.get(url) as r:
        if r.status != 200:
            raise Exception(
                f"Error fetching page for PubMed ID {pubmed_id}. Status: {r.status}"
            )
        html_text = await r.text()
        soup = BeautifulSoup(html_text, 'html.parser')

        # First, try to find a PMC ID
        pmc_id_match = re.search(r"PMC\d+", html_text)
        if pmc_id_match:
            pmc_id = pmc_id_match.group(0)[3:]
            pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmc_id}/pdf/"
            async with session.get(pdf_url) as pdf_r:
                if pdf_r.status == 200:
                    return pdf_url

        # If no PMC ID or PDF not available, look for full-text links
        full_text_links = soup.select('.full-text-links-list a')
        for link in full_text_links:
            href = link.get('href')
            if href:
                # You might want to prioritize certain domains or file types
                if href.endswith('.pdf') or 'pdf' in href.lower():
                    return href
                else:
                    # Return the first available link if no PDF link is found
                    return href

        # If no full-text links are found
        raise Exception(f"No full-text link found for PubMed ID {pubmed_id}.")


async def likely_pdf(response):
    try:
        text = await response.text()
        text = text.lower()
        if "invalid article id" in text:
            return False
        if "no paper" in text or "not found" in text:
            return False
        if "404" in text and "error" in text:
            return False
        if "404" in text and "not found" in text:
            return False
        if "403" in text and "forbidden" in text:
            return False
    # Bytestream? Probably a PDF
    except UnicodeDecodeError:
        return True
    # we're still unsure, so let's check mimetype
    if response.headers["Content-Type"] == "application/pdf":
        return True
    return False

async def test_get_arxiv_details():
    url = "https://arxiv.org/abs/2303.08774"
    result = await get_arxiv_details(url)
    print(f"ArXiv paper details: {result}")
    assert result['id'] == "2303.08774"
    assert 'title' in result
    assert 'authors' in result
    assert 'abstract' in result

async def test_get_pubmed_details():
    url = "https://pubmed.ncbi.nlm.nih.gov/35580832"
    result = await get_pubmed_details(url)
    print(f"PubMed paper details: {result}")
    assert result['id'] == "35580832"
    assert 'title' in result
    assert 'authors' in result
    assert 'abstract' in result

async def test_pubmed_to_pdf_url():
    url = "https://pubmed.ncbi.nlm.nih.gov/35580832"
    async with aiohttp.ClientSession() as session:
        pdf_url = await pubmed_to_pdf_url(url, session)
    print(f"PubMed full-text URL: {pdf_url}")
    assert pdf_url.startswith("http")  # Check that we got a URL
    async with aiohttp.ClientSession() as session:
        async with session.get(pdf_url) as response:
            assert response.status == 200  # Check that the URL is accessible

async def test_likely_pdf():
    pdf_url = "https://arxiv.org/pdf/2303.08774.pdf"
    async with aiohttp.ClientSession() as session:
        async with session.get(pdf_url) as response:
            is_likely_pdf = await likely_pdf(response)
    print(f"Is likely PDF: {is_likely_pdf}")
    assert is_likely_pdf == True

async def test_get_paper_details():
    arxiv_url = "https://arxiv.org/abs/2303.08774"
    pubmed_url = "https://pubmed.ncbi.nlm.nih.gov/35580832"
    
    arxiv_result = await get_paper_details(arxiv_url)
    pubmed_result = await get_paper_details(pubmed_url)
    
    print(f"ArXiv paper details: {arxiv_result}")
    print(f"PubMed paper details: {pubmed_result}")
    
    assert arxiv_result['id'] == "2303.08774"
    assert pubmed_result['id'] == "35580832"
    
    try:
        await get_paper_details("https://example.com")
    except ValueError as e:
        print(f"Expected error raised: {e}")
    else:
        raise AssertionError("ValueError not raised for unsupported URL")

async def run_tests():
    print("Running tests...")
    await test_get_arxiv_details()
    await test_get_pubmed_details()
    await test_pubmed_to_pdf_url()
    await test_likely_pdf()
    await test_get_paper_details()
    print("All tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(run_tests())