import os
import pytest
from PIL import Image
from io import BytesIO


@pytest.mark.visual
@pytest.mark.regression
def test_inventory_visual_snapshot(authenticated_page):
    page = authenticated_page

    page.goto("https://www.saucedemo.com/inventory.html")
    page.wait_for_load_state("networkidle")

    snapshot_dir = os.path.join("reports", "visual_baseline")
    os.makedirs(snapshot_dir, exist_ok=True)

    baseline_path = os.path.join(snapshot_dir, "inventory_baseline.png")

    current_bytes = page.screenshot(full_page=True)

    # First run → create baseline
    if not os.path.exists(baseline_path):
        with open(baseline_path, "wb") as f:
            f.write(current_bytes)
        assert True
        return

    # Load images
    current_image = Image.open(BytesIO(current_bytes))
    baseline_image = Image.open(baseline_path)

    # Compare sizes first
    assert current_image.size == baseline_image.size, "Image dimensions changed!"

    # Compare pixel data
    diff_pixels = 0
    total_pixels = current_image.size[0] * current_image.size[1]

    current_pixels = current_image.load()
    baseline_pixels = baseline_image.load()

    for x in range(current_image.size[0]):
        for y in range(current_image.size[1]):
            if current_pixels[x, y] != baseline_pixels[x, y]:
                diff_pixels += 1

    diff_ratio = diff_pixels / total_pixels

    # Allow small visual noise (0.1%)
    assert diff_ratio < 0.001, f"Visual regression detected! Diff ratio: {diff_ratio}"
