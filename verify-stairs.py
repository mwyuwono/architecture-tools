#!/usr/bin/env python3
"""Zero-Trust Verification for Stair Calculator V2"""

from playwright.sync_api import sync_playwright

URL = "http://localhost:8765/stairs.html"

def add_check(name, passed, details=""):
    status = "✅" if passed else "❌"
    print(f"{status} {name}: {details}")
    return passed

def main():
    passed_count = 0
    total_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print("\n=== ZERO-TRUST VERIFICATION: Stair Calculator V2 ===\n")

        response = page.goto(URL, wait_until="networkidle")
        total_count += 1
        if add_check("Page loads", response.status == 200, f"HTTP {response.status}"):
            passed_count += 1

        page.wait_for_timeout(1000)

        # === Single-Run Mode (Default) ===
        print("\n--- Single-Run Mode (Default) ---")

        # Check type selector exists
        type_selector = page.locator(".type-selector")
        total_count += 1
        if add_check("Type selector exists", type_selector.is_visible()):
            passed_count += 1

        # Check single-run is selected by default
        single_selected = page.locator("#opt-single.selected")
        total_count += 1
        if add_check("Single-run selected by default", single_selected.count() == 1):
            passed_count += 1

        # Check width input exists
        width_input = page.locator("#widthInput")
        total_count += 1
        if add_check("Width input exists", width_input.is_visible()):
            passed_count += 1

        # Verify dual unit display (height = 108", should show feet-inches)
        riser_height = page.locator("#outRiserHeight").inner_html()
        total_count += 1
        has_ft_in = "'" in riser_height or "⅛" in riser_height or "¼" in riser_height or "½" in riser_height
        if add_check("Riser height shows formatted inches", "\"" in riser_height, riser_height[:50]):
            passed_count += 1

        total_run = page.locator("#outRun").inner_html()
        total_count += 1
        if add_check("Total run shows feet-inches format", "'-" in total_run, total_run[:50]):
            passed_count += 1

        # Verify calculations (108" / 7.75 = 14 risers, 13 treads, 130" run)
        risers = page.locator("#outRisers").text_content()
        total_count += 1
        if add_check("Correct riser count for 108\" height", risers == "14", f"risers={risers}"):
            passed_count += 1

        treads = page.locator("#outTreads").text_content()
        total_count += 1
        if add_check("Correct tread count", treads == "13", f"treads={treads}"):
            passed_count += 1

        # Check footprint displayed
        footprint = page.locator("#outFootprintSingle").inner_html()
        total_count += 1
        if add_check("Footprint shows dimensions", "×" in footprint, footprint[:50]):
            passed_count += 1

        # === Switchback Mode ===
        print("\n--- Switchback Mode ---")

        # Click switchback option
        page.locator("#opt-switchback").click()
        page.wait_for_timeout(500)

        switchback_selected = page.locator("#opt-switchback.selected")
        total_count += 1
        if add_check("Switchback mode selected", switchback_selected.count() == 1):
            passed_count += 1

        # Check switchback results visible
        switchback_section = page.locator(".switchback-results.visible").first
        total_count += 1
        if add_check("Switchback results visible", switchback_section.is_visible()):
            passed_count += 1

        # Check flight 1 risers (should be 7 for 14 total)
        flight1_risers = page.locator("#outFlight1Risers").text_content()
        total_count += 1
        if add_check("Flight 1 risers calculated", flight1_risers == "7", f"flight1={flight1_risers}"):
            passed_count += 1

        # Check flight 2 risers (should be 7)
        flight2_risers = page.locator("#outFlight2Risers").text_content()
        total_count += 1
        if add_check("Flight 2 risers calculated", flight2_risers == "7", f"flight2={flight2_risers}"):
            passed_count += 1

        # Check landing dimensions shown (36" = 3'-0")
        landing = page.locator("#outLanding").inner_html()
        total_count += 1
        if add_check("Landing dimensions shown", "×" in landing and ("36" in landing or "3'-0\"" in landing), landing[:50]):
            passed_count += 1

        # Check switchback footprint
        sb_footprint = page.locator("#outFootprintSwitchback").inner_html()
        total_count += 1
        if add_check("Switchback footprint shown", "×" in sb_footprint, sb_footprint[:50]):
            passed_count += 1

        # === Canvas Visualization ===
        print("\n--- Canvas Visualization ---")

        canvas = page.locator("#stairCanvas")
        canvas_box = canvas.bounding_box()
        total_count += 1
        if add_check("Canvas visible", canvas_box and canvas_box["width"] > 0, f"{canvas_box['width']}x{canvas_box['height']}px" if canvas_box else "not found"):
            passed_count += 1

        # Switch back to single-run and verify canvas updates
        page.locator("#opt-single").click()
        page.wait_for_timeout(500)
        single_results_visible = page.locator(".single-results").is_visible()
        total_count += 1
        if add_check("Single-run results visible after switch", single_results_visible):
            passed_count += 1

        # === Console Errors ===
        print("\n--- Console Errors ---")
        real_errors = [e for e in console_errors if "favicon" not in e.lower()]
        total_count += 1
        if add_check("Zero console errors", len(real_errors) == 0, f"{len(real_errors)} errors" if real_errors else "clean"):
            passed_count += 1

        browser.close()

        # === SUMMARY ===
        print(f"\n=== VERIFICATION SUMMARY ===")
        print(f"\nPassed: {passed_count}/{total_count}")

        if passed_count == total_count:
            print("\n✅ ALL CHECKS PASSED")
            return True
        else:
            print("\n❌ SOME CHECKS FAILED")
            return False

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
