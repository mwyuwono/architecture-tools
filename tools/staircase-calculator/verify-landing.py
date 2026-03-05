#!/usr/bin/env python3
"""Zero-Trust Verification for Architecture Tools Landing Page"""

import json
from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/index.html"
RESULTS = {
    "console_errors": [],
    "checks": []
}

def add_check(name, passed, details=""):
    RESULTS["checks"].append({
        "name": name,
        "passed": passed,
        "details": details
    })
    status = "✅" if passed else "❌"
    print(f"{status} {name}: {details}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Collect console errors
        page.on("console", lambda msg: RESULTS["console_errors"].append(msg.text) if msg.type == "error" else None)

        print("\n=== ZERO-TRUST VERIFICATION: Landing Page ===\n")

        # Load page
        response = page.goto(URL, wait_until="networkidle")
        add_check("Page loads", response.status == 200, f"HTTP {response.status}")

        # Wait for fonts and images
        page.wait_for_timeout(2000)

        # === SECTION 1: Hero Section ===
        print("\n--- Hero Section ---")

        hero = page.locator(".hero").first
        hero_box = hero.bounding_box()
        add_check("Hero section visible", hero_box and hero_box["height"] > 0, f"height={hero_box['height'] if hero_box else 0}px")

        brand = page.locator(".brand-label").first
        brand_visible = brand.is_visible()
        add_check("Brand label visible", brand_visible, brand.text_content() if brand_visible else "not found")

        title = page.locator(".hero-title").first
        title_visible = title.is_visible()
        add_check("Hero title visible", title_visible and "Architecture" in title.text_content(), "contains 'Architecture'")

        # === SECTION 2: Featured Tools Section ===
        print("\n--- Featured Tools Section ---")

        featured = page.locator(".featured-section").first
        featured_box = featured.bounding_box()
        add_check("Featured Tools section exists", featured_box and featured_box["height"] > 0, f"height={featured_box['height'] if featured_box else 0}px")

        featured_title = page.locator(".featured-title").first
        add_check("Featured Tools heading", featured_title.is_visible() and "Featured Tools" in featured_title.text_content(), featured_title.text_content() if featured_title.is_visible() else "not found")

        # Tool Card
        tool_card = page.locator(".tool-card").first
        tool_card_box = tool_card.bounding_box()
        add_check("Stair Calculator card exists", tool_card_box and tool_card_box["height"] > 0, f"height={tool_card_box['height'] if tool_card_box else 0}px")

        tool_title = page.locator(".tool-card-title").first
        add_check("Card title is 'Stair Calculator'", tool_title.is_visible() and "Stair Calculator" in tool_title.text_content(), tool_title.text_content() if tool_title.is_visible() else "not found")

        # Open Tool button
        tool_button = page.locator(".tool-button").first
        tool_button_href = tool_button.get_attribute("href")
        add_check("'Open Tool' button links to stairs.html", tool_button_href == "stairs.html", f"href='{tool_button_href}'")

        # === SECTION 3: IRC Compliant Section ===
        print("\n--- IRC Compliant Section ---")

        irc = page.locator(".irc-section").first
        irc_box = irc.bounding_box()
        add_check("IRC section visible", irc_box and irc_box["height"] > 0, f"height={irc_box['height'] if irc_box else 0}px")

        irc_link = page.locator(".irc-link").first
        irc_href = irc_link.get_attribute("href")
        add_check("IRC link is external (not stairs.html)", "iccsafe.org" in irc_href, f"href contains 'iccsafe.org'")
        add_check("IRC link opens in new tab", irc_link.get_attribute("target") == "_blank", f"target='{irc_link.get_attribute('target')}'")

        # === SECTION 4: Design Tokens ===
        print("\n--- Design Token Verification ---")

        brand_color = page.evaluate("""() => {
            const el = document.querySelector('.brand-label');
            return getComputedStyle(el).color;
        }""")
        add_check("Brand label uses primary color", "44, 76, 59" in brand_color, f"color={brand_color}")

        irc_bg = page.evaluate("""() => {
            const el = document.querySelector('.irc-section');
            return getComputedStyle(el).backgroundColor;
        }""")
        add_check("IRC section uses primary background", "44, 76, 59" in irc_bg, f"bg={irc_bg}")

        # === SECTION 5: Interactive States ===
        print("\n--- Interactive States ---")

        # Hero image hover
        hero_container = page.locator(".hero-image-container").first
        img_filter_before = page.evaluate("""() => {
            const el = document.querySelector('.hero-image');
            return getComputedStyle(el).filter;
        }""")
        hero_container.hover()
        page.wait_for_timeout(800)
        img_filter_after = page.evaluate("""() => {
            const el = document.querySelector('.hero-image');
            return getComputedStyle(el).filter;
        }""")
        add_check("Hero image grayscale hover effect", "grayscale(1)" in img_filter_before and "grayscale(0" in img_filter_after, f"before={img_filter_before}, after={img_filter_after}")

        # === SECTION 6: Console Errors ===
        print("\n--- Console Errors ---")

        real_errors = [e for e in RESULTS["console_errors"] if "favicon" not in e.lower()]
        add_check("Zero console errors", len(real_errors) == 0, f"{len(real_errors)} errors" if real_errors else "clean")

        # === SECTION 7: Navigation ===
        print("\n--- Navigation ---")

        # Click Open Tool button
        tool_button.click()
        page.wait_for_load_state("networkidle")
        current_url = page.url
        add_check("'Open Tool' navigates to stairs.html", "stairs.html" in current_url, f"url={current_url}")

        browser.close()

        # === SUMMARY ===
        print("\n=== VERIFICATION SUMMARY ===")
        passed = sum(1 for c in RESULTS["checks"] if c["passed"])
        total = len(RESULTS["checks"])
        print(f"\nPassed: {passed}/{total}")

        if passed == total:
            print("\n✅ ALL CHECKS PASSED")
        else:
            print("\n❌ SOME CHECKS FAILED")
            for c in RESULTS["checks"]:
                if not c["passed"]:
                    print(f"   - {c['name']}: {c['details']}")

        return passed == total

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
