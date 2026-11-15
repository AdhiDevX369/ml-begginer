"""Scrape house-for-sale listings from LankaPropertyWeb into sl_houses_live.csv.

Stage 1 walks the search pages of each area and collects listing ids.
Stage 2 opens every listing's detail page and reads the structured Overview block
(bedrooms, bathrooms, floor area, land) plus the full price.

Progress is cached in .scrape_cache/, so re-running resumes where it stopped.
Usage: python scrape_lankapropertyweb.py [target_listings]
"""
import json
import os
import re
import sys
import time
from urllib.robotparser import RobotFileParser

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE = "https://www.lankapropertyweb.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MLClassBot/1.0; course project)"}
DELAY = 1.0
CACHE = ".scrape_cache"
OUT = "sl_houses_live.csv"

# Colombo city plus suburbs within roughly 25 km of Fort
AREAS = [
    "Colombo+All_0",
    "Western_Dehiwala", "Western_Mount+Lavinia", "Western_Nugegoda", "Western_Battaramulla",
    "Western_Rajagiriya", "Western_Kotte", "Western_Maharagama", "Western_Boralesgamuwa",
    "Western_Piliyandala", "Western_Kottawa", "Western_Malabe", "Western_Thalawathugoda",
    "Western_Pannipitiya", "Western_Wattala", "Western_Kelaniya", "Western_Ratmalana",
    "Western_Moratuwa", "Western_Kadawatha", "Western_Athurugiriya",
]

session = requests.Session()
session.headers.update(HEADERS)
robots = RobotFileParser()
robots.parse(session.get(BASE + "/robots.txt", timeout=15).text.splitlines())


def get(url):
    if not robots.can_fetch(HEADERS["User-Agent"], url):
        raise PermissionError(f"robots.txt disallows {url}")
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=20)
            time.sleep(DELAY)
            if resp.status_code == 200:
                return resp.text
            if resp.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(5 * (attempt + 1))
    return None


def text_of(tag):
    return tag.get_text(" ", strip=True) if tag else None


def parse_search_page(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = []
    for card in soup.select("article.listing-item"):
        cards.append({"listing_id": card.get("data-ad-id"),
                      "card_location": text_of(card.select_one(".location"))})
    next_link = soup.find("a", href=re.compile(r"page=2&"))
    return cards, (next_link["href"] if next_link else None)


def collect_ids(target):
    path = os.path.join(CACHE, "ids.json")
    found = json.load(open(path)) if os.path.exists(path) else {}
    for area in AREAS:
        if len(found) >= target:
            break
        html = get(f"{BASE}/forsale-{area}-House.html")
        if not html:
            print(f"  {area}: no page")
            continue
        cards, page2 = parse_search_page(html)
        page, before = 1, len(found)
        while cards:
            new = [c for c in cards if c["listing_id"] and c["listing_id"] not in found]
            for c in new:
                found[c["listing_id"]] = c["card_location"]
            if not new or not page2 or len(found) >= target:
                break
            page += 1
            html = get(BASE + page2.replace("page=2&", f"page={page}&"))
            cards = parse_search_page(html)[0] if html else []
        print(f"  {area}: +{len(found) - before} listings ({page} pages), total {len(found)}")
        json.dump(found, open(path, "w"))
    return found


def parse_detail(html):
    soup = BeautifulSoup(html, "html.parser")
    overview = {}
    for item in soup.select("#Overview .overview-item"):
        overview[text_of(item.select_one(".label"))] = text_of(item.select_one(".value"))
    locality = None
    for script in soup.find_all("script", type="application/ld+json"):
        m = re.search(r'"addressLocality"\s*:\s*"([^"]*)"', script.string or "")
        if m:
            locality = m.group(1).strip()
    title = text_of(soup.find("h1"))
    return {
        "title": title,
        "locality": locality,
        "property_type": overview.get("Property Type"),
        "raw_beds": overview.get("Bedrooms"),
        "raw_baths": overview.get("Bathrooms/WCs"),
        "raw_sqft": overview.get("Floor area"),
        "raw_perches": overview.get("Area of land"),
        "raw_price": text_of(soup.select_one(".main_price")),
    }


def fetch_details(ids):
    path = os.path.join(CACHE, "details.jsonl")
    done = set()
    if os.path.exists(path):
        done = {json.loads(line)["listing_id"] for line in open(path)}
    todo = [i for i in ids if i not in done]
    print(f"Stage 2: {len(done)} cached, {len(todo)} to fetch")
    with open(path, "a") as f:
        for n, listing_id in enumerate(todo, 1):
            html = get(f"{BASE}/sale/property_details-{listing_id}.html")
            row = {"listing_id": listing_id, "card_location": ids[listing_id]}
            if html:
                row.update(parse_detail(html))
            f.write(json.dumps(row) + "\n")
            f.flush()
            if n % 50 == 0:
                print(f"  {n}/{len(todo)}")
    return pd.read_json(path, lines=True, dtype={"listing_id": str})


if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 1300
    os.makedirs(CACHE, exist_ok=True)
    print("Stage 1: collecting listing ids")
    ids = collect_ids(target)
    df = fetch_details(ids)
    df["scraped_on"] = time.strftime("%Y-%m-%d")
    df.to_csv(OUT, index=False)
    print(f"Saved {len(df)} rows to {OUT}")
