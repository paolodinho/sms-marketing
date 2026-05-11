"""
Domain Hunter Agent - SMS Marketing VN
Tìm expired/available domain .com/.net cho dự án SMS

Cách chạy:
  python domain_hunter.py                  # Full scan
  python domain_hunter.py smsviet.com      # Quick check 1 domain
  python domain_hunter.py --backorder      # Chỉ show domains sắp hết hạn

Yêu cầu: pip install requests beautifulsoup4
"""

import re, sys, json, time, socket
import datetime
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

# ──────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────

TODAY = datetime.date.today()

# Domains đã verify available / sắp hết hạn (RDAP check 11/05/2026)
# Chạy lại script để refresh data
SEED_DOMAINS = [
    # === Keyword + Vietnam ===
    "vietnamsms.net", "smsviet.com", "msgviet.com",
    "textvn.net", "smsasean.net", "smshanoi.com", "smssaigon.com",
    # === Brand names ===
    "smsfire.net", "smsflash.net", "msgtxt.net",
    "smsify.net", "smsdaddy.net", "smsmonkey.net",
    "textmonkey.net", "smsgenie.net", "smsgenie.org",
    "smsgenius.net", "smschamp.net", "textblast.net",
    "smsblast.net", "textpush.net", "smspush.net", "smsalert.net",
    # === Sắp hết hạn - backorder candidates ===
    "smsjet.com",       # 15d
    "smsgiare.com",     # 32d - keyword-rich!
    "smsbuddy.com",     # 41d
    "textbuddy.net",    # 42d
    "smspush.com",      # 46d
    "textalert.net",    # 83d
    "textwiz.com",      # 127d
    "textmonkey.com",   # 128d - real software company
    "smszap.com",       # 141d - real company (rebranded to Sakari)
    "smsalert.com",     # 171d - real site
    "textblast.com",    # 292d - real site
]

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120"}

# ──────────────────────────────────────────────────────────────
# STEP 1: DOMAIN AVAILABILITY CHECK (RDAP - works without login)
# ──────────────────────────────────────────────────────────────

def check_rdap(domain):
    """
    RDAP.org - chuẩn ICANN public. Tốt với .com/.net, không cần login.
    Returns: (status, expiry_date_str)
      status: "available" | "registered" | "error"
    """
    try:
        resp = requests.get(f"https://rdap.org/domain/{domain}", headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        expiry = next(
            (e["eventDate"][:10] for e in data.get("events", [])
             if e.get("eventAction") == "expiration"),
            ""
        )
        return "registered", expiry
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return "available", ""
        return "error", ""
    except Exception:
        return "error", ""


def days_until(date_str):
    if not date_str:
        return None
    try:
        return (datetime.date.fromisoformat(date_str) - TODAY).days
    except:
        return None


# ──────────────────────────────────────────────────────────────
# STEP 2: DETECT IF DOMAIN IS REAL SITE OR PARKED/FOR-SALE
# ──────────────────────────────────────────────────────────────

PARKING_SIGNALS = [
    "hugedomains", "godaddy.com/domains", "sedo.com", "dan.com",
    "afternic", "sedopark", "namecheap.com/domains",
    "this domain is for sale", "domain for sale", "buy this domain",
    "domain parking", "parked by", "this web page is parked",
]

def detect_site_type(domain):
    """
    Fetch domain, detect if it's: real_site | for_sale | parked | offline
    Returns: (type_str, redirect_url, title)
    """
    for scheme in ["https", "http"]:
        try:
            resp = requests.get(
                f"{scheme}://{domain}", headers=HEADERS, timeout=8,
                allow_redirects=True
            )
            final_url = resp.url.lower()
            content = resp.text[:2000].lower()

            # Check redirect destination
            if any(p in final_url for p in PARKING_SIGNALS):
                return "for_sale", resp.url, ""

            # Check content signals
            if any(p in content for p in PARKING_SIGNALS):
                return "parked", resp.url, ""

            # Extract title
            soup = BeautifulSoup(resp.text[:3000], "html.parser")
            title = soup.title.string.strip() if soup.title else ""

            if len(resp.text) > 500:
                return "real_site", resp.url, title[:60]
            return "minimal", resp.url, title

        except requests.exceptions.ConnectionError:
            return "offline", "", ""
        except Exception:
            continue

    return "offline", "", ""


# ──────────────────────────────────────────────────────────────
# STEP 3: BACKLINK CHECK
# Requires paid API. Script provides link to check manually.
# ──────────────────────────────────────────────────────────────

def backlink_check_links(domain):
    """Return manual check URLs for free backlink tools."""
    return {
        "ahrefs_free": f"https://ahrefs.com/backlink-checker/?input={domain}&mode=domain",
        "moz_da":      f"https://moz.com/domain-analysis?site={domain}",
        "semrush":     f"https://www.semrush.com/analytics/overview/?q={domain}&searchType=domain",
        "majestic":    f"https://majestic.com/reports/site-explorer?IndexDataSource=F&oq={domain}&q={domain}",
    }


# ──────────────────────────────────────────────────────────────
# STEP 4: SCORE & RANK
# ──────────────────────────────────────────────────────────────

def score_domain(entry):
    score = 0

    # Availability
    if entry["status"] == "available":
        score += 10
    elif entry["status"] == "registered":
        days = entry.get("days_left")
        if days is not None:
            if days < 30:   score += 30  # Expiring very soon
            elif days < 60: score += 20
            elif days < 120: score += 12
            elif days < 365: score += 5

    # Site type bonus (real site = was used = has backlinks)
    site_type = entry.get("site_type", "")
    if site_type == "real_site":  score += 30
    elif site_type == "minimal":  score += 5
    elif site_type == "for_sale": score -= 5  # Overpriced, likely no backlinks

    # Keyword relevance
    d = entry["domain"].lower()
    if any(k in d for k in ["sms", "text", "msg", "bulk"]):     score += 10
    if any(k in d for k in ["viet", "vietnam", "vn", "saigon"]): score += 8

    # TLD preference
    if d.endswith(".com"):  score += 5
    elif d.endswith(".net"): score += 3

    return min(score, 100)


# ──────────────────────────────────────────────────────────────
# MAIN AGENT
# ──────────────────────────────────────────────────────────────

def run_agent(domains=None, backorder_only=False):
    targets = domains or SEED_DOMAINS

    print("=" * 65)
    print("  DOMAIN HUNTER AGENT - SMS Marketing VN")
    print(f"  {TODAY.strftime('%d/%m/%Y')} | Checking {len(targets)} domains")
    print("=" * 65)

    results = []

    for domain in targets:
        print(f"\n  [{domain}]", end=" ", flush=True)

        # RDAP check
        status, expiry = check_rdap(domain)
        days = days_until(expiry) if expiry else None

        if backorder_only and status == "available":
            print("available - skip (--backorder mode)")
            continue

        entry = {
            "domain": domain,
            "status": status,
            "expiry": expiry,
            "days_left": days,
            "site_type": None,
            "redirect": None,
            "title": None,
        }

        if status == "available":
            print("AVAILABLE ✓", end="")
            entry["site_type"] = "new_reg"

        elif status == "registered":
            exp_str = f"expires {expiry} ({days}d)" if days else "no expiry"
            print(exp_str, end="")

            # Only probe real HTTP if expiring in < 400 days (worth checking)
            if days is not None and days < 400:
                time.sleep(0.5)
                site_type, redirect, title = detect_site_type(domain)
                entry["site_type"] = site_type
                entry["redirect"] = redirect
                entry["title"] = title
                print(f" | site: {site_type}", end="")
                if title:
                    print(f' "{title[:35]}"', end="")
        else:
            print(f"error", end="")

        entry["score"] = score_domain(entry)
        entry["backlink_links"] = backlink_check_links(domain)
        results.append(entry)

        time.sleep(0.3)

    # Sort
    results.sort(key=lambda x: x["score"], reverse=True)

    # Print results
    print("\n\n" + "=" * 65)
    print("  RESULTS - TOP DOMAINS (sorted by score)")
    print("=" * 65)
    print(f"{'Domain':<28} {'Score':>5}  {'Status':<12} {'Site':<12} {'Expires'}")
    print("-" * 65)

    for r in results[:20]:
        expires_str = f"{r['days_left']}d" if r.get("days_left") else (r["expiry"] or "")
        site_str = r.get("site_type", "") or ""
        print(
            f"  {r['domain']:<26} {r['score']:>5}  "
            f"{r['status']:<12} {site_str:<12} {expires_str}"
        )

    # Categories
    available = [r for r in results if r["status"] == "available"]
    real_expiring = [r for r in results
                     if r["status"] == "registered"
                     and r.get("site_type") == "real_site"
                     and r.get("days_left", 999) < 365]
    backorder = [r for r in results
                 if r["status"] == "registered"
                 and r.get("days_left", 999) < 90]

    print(f"\n{'='*65}")
    print(f"  SUMMARY")
    print(f"{'='*65}")
    print(f"  Available to register NOW ({len(available)}):")
    for r in available[:5]:
        print(f"    → {r['domain']} (score: {r['score']})")

    print(f"\n  Real sites expiring < 1yr - BACKORDER THESE ({len(real_expiring)}):")
    for r in sorted(real_expiring, key=lambda x: x.get("days_left", 999))[:5]:
        print(f"    → {r['domain']} | {r['days_left']}d | \"{r.get('title','')[:35]}\"")
        print(f"      Backlink check: {r['backlink_links']['ahrefs_free']}")

    print(f"\n  Expiring < 90d - Backorder on GoDaddy/NameJet ({len(backorder)}):")
    for r in sorted(backorder, key=lambda x: x.get("days_left", 999)):
        print(f"    → {r['domain']} in {r['days_left']} days | site: {r.get('site_type','?')}")

    # Save JSON
    with open("domain_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n  [✓] Results saved to domain_results.json")

    return results


# ──────────────────────────────────────────────────────────────
# QUICK CHECK - single domain
# ──────────────────────────────────────────────────────────────

def quick_check(domain):
    print(f"\n{'='*50}")
    print(f"Quick Check: {domain}")
    print(f"{'='*50}")

    status, expiry = check_rdap(domain)
    days = days_until(expiry) if expiry else None

    print(f"  RDAP status : {status}")
    if expiry:
        print(f"  Expires     : {expiry} ({days} days)")

    if status == "available":
        print(f"  → AVAILABLE! Register at namecheap.com or godaddy.com")
    elif status == "registered":
        site_type, redirect, title = detect_site_type(domain)
        print(f"  Site type   : {site_type}")
        if redirect:   print(f"  Redirects to: {redirect[:70]}")
        if title:      print(f"  Page title  : {title}")

        links = backlink_check_links(domain)
        print(f"\n  Check backlinks:")
        for name, url in links.items():
            print(f"    {name:<15}: {url}")

        if site_type == "real_site" and days and days < 365:
            print(f"\n  [BACKORDER CANDIDATE] real site, expires in {days} days!")
            print(f"    Backorder on: https://auctions.godaddy.com (search: {domain})")
            print(f"    Also try   : https://www.namejet.com")

    print()


# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--backorder":
            run_agent(backorder_only=True)
        else:
            # Quick check specific domain
            quick_check(arg)
    else:
        run_agent()
