import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Our Deals title
text = text.replace('<span>Our Deals</span>', '<span>Bundles & Savings</span>')

# Replace Shop By Category labels
replacements = {
    'Home Appliances': 'Home Faves',
    'Televisions': 'TV Steals',
    'Air Conditioners': 'Cool Zone',
    'Audio': 'Sound Central',
    'Refrigerators': 'Always Fresh',
    'Washing Machines': 'Easy Laundry',
    'Microwaves': 'Easy Meals',
    'Monitors': 'Clear View'
}

for old, new in replacements.items():
    text = text.replace(f'<span class="card-fallback-text">{old}</span>', f'<span class="card-fallback-text">{new}</span>')
    text = text.replace(f'<div class="shop-category-label">{old}</div>', f'<div class="shop-category-label">{new}</div>')

# Replace Bento Grid items
bento_html = """
      <div class="bento-grid">
        <div class="bento-item bento-large" style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
          <span style="font-size: 16px; font-weight: 500; text-transform: uppercase; color: #fff;">Groceries</span>
          <span style="font-size: 14px; font-weight: 300; color: #f0f0f0;">Shop & Chop</span>
        </div>
        <div class="bento-item bento-wide" style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
          <span style="font-size: 16px; font-weight: 500; text-transform: uppercase; color: #fff; letter-spacing: 1px;">Fashion & Footwear</span>
          <span style="font-size: 14px; font-weight: 300; color: #f0f0f0;">Head to Toe</span>
        </div>
        <div class="bento-item" style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
          <span style="font-size: 16px; font-weight: 500; text-transform: uppercase; color: #fff; text-align: center;">Fitness & Sports</span>
          <span style="font-size: 14px; font-weight: 300; color: #f0f0f0; text-align: center;">Stay Active</span>
        </div>
        <div class="bento-item" style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
          <span style="font-size: 16px; font-weight: 500; text-transform: uppercase; color: #fff; text-align: center;">Baby & Kids</span>
          <span style="font-size: 14px; font-weight: 300; color: #f0f0f0; text-align: center;">Little Treasures</span>
        </div>
      </div>
"""

old_bento_pattern = re.compile(r'<div class="bento-grid">.*?</div>\s*</section>', re.DOTALL)
text = re.sub(old_bento_pattern, bento_html.strip() + '\n    </section>', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

