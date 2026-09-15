import re

html_content = """
    <section class="category-collections-section section-reset">
      <div class="collections-grid">
                
        <div class="hub-card">
          <h3 class="hub-title">Grooming & Personal Care</h3>
          <div class="hub-content hub-layout-1">
            <div class="hub-item tall">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Hair & Beard</span>
            </div>
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Shaving Gear</span>
            </div>
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Deodorants</span>
            </div>
          </div>
          <div class="hub-footer">
            <a href="#">Shop Grooming</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Skincare & Beauty</h3>
          <div class="hub-content hub-layout-2">
            <div class="hub-item wide">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Face Serums</span>
            </div>
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Cleansers</span>
            </div>
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Sun Protection</span>
            </div>
          </div>
          <div class="hub-footer">
            <a href="#">Discover Beauty</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Groceries & Pantry</h3>
          <div class="hub-content hub-layout-3">
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Rice & Grains</span>
            </div>
            <div class="hub-item small">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Cooking Oils</span>
            </div>
            <div class="hub-item wide">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Seasonings</span>
            </div>
          </div>
          <div class="hub-footer">
            <a href="#">Shop Groceries</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Household Essentials</h3>
          <div class="hub-content hub-layout-4">
            <div class="hub-item full">
              <div class="hub-placeholder"></div>
              <span class="hub-item-label">Tissue Paper</span>
            </div>
          </div>
          <div class="hub-footer">
            <a href="#">Stock Up Now</a>
          </div>
        </div>
      </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<section class="category-collections-section section-reset">.*?</section>', re.DOTALL)
new_text = pattern.sub(html_content.strip(), text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)
