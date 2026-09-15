import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace CSS
old_css_regex = r'\.hub-editorial-hero \{.*?(?=\.hub-footer \{)'
new_css = """
      /* Top Section: Circular Avatars */
      .hub-avatar-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        flex-grow: 1;
        margin-bottom: 1.5rem;
        justify-content: center;
      }
      .hub-avatar-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 0.5rem;
        text-decoration: none;
      }
      .hub-avatar-placeholder {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background-color: #f9f9f9;
        border: 2px dashed #ccc;
        transition: border-color 0.3s, transform 0.3s;
      }
      .hub-avatar-item:hover .hub-avatar-placeholder {
        border-color: #ed017f;
        transform: scale(1.05);
      }
      .hub-avatar-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #444;
      }

      /* Bottom Section: Chips/Tag Cloud */
      .hub-chips-hero {
        width: 100%;
        aspect-ratio: 16 / 9;
        background-color: #f4f4f4;
        border: 2px dashed #ddd;
        border-radius: 8px;
        margin-bottom: 1rem;
      }
      .hub-chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        flex-grow: 1;
      }
      .hub-chip {
        padding: 0.35rem 0.75rem;
        background-color: #f0f0f0;
        border-radius: 16px;
        font-size: 0.75rem;
        font-weight: 500;
        color: #333;
        text-decoration: none;
        transition: background-color 0.2s, color 0.2s;
      }
      .hub-chip:hover {
        background-color: #ed017f;
        color: #fff;
      }

      """
text = re.sub(old_css_regex, new_css, text, flags=re.DOTALL)

# HTML for Featured Hubs (Circular Avatars)
featured_html = """
    <section class="featured-hubs-section section-reset">
      <div class="container">
        <div class="featured-hubs-grid">
          
          <div class="hub-card">
            <h3 class="hub-title">Top Computing & Tech</h3>
            <div class="hub-avatar-grid">
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Laptops</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Consoles</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Starlink</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Printers</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Shop Tech Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Bestselling Smartphones</h3>
            <div class="hub-avatar-grid">
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Samsung</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">iPhones</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Xiaomi</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Tecno</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Upgrade Now</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Home & Power</h3>
            <div class="hub-avatar-grid">
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Generators</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Fridges</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Washers</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">ACs</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Shop Home Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Health & Beauty</h3>
            <div class="hub-avatar-grid">
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Oral Care</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Vitamins</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Fragrances</span>
              </a>
              <a href="#" class="hub-avatar-item">
                <div class="hub-avatar-placeholder"></div>
                <span class="hub-avatar-label">Makeup</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Discover Beauty</a>
            </div>
          </div>

        </div>
      </div>
    </section>
"""
text = re.sub(r'<section class="featured-hubs-section section-reset">.*?</section>', featured_html.strip(), text, flags=re.DOTALL)

# HTML for Category Collections (Tag Cloud)
collections_html = """
    <section class="category-collections-section section-reset">
      <div class="collections-grid">
                
        <div class="hub-card">
          <h3 class="hub-title">Grooming & Personal Care</h3>
          <div class="hub-chips-hero"></div>
          <div class="hub-chips-container">
            <a href="#" class="hub-chip">Hair & Beard</a>
            <a href="#" class="hub-chip">Shaving Gear</a>
            <a href="#" class="hub-chip">Deodorants</a>
            <a href="#" class="hub-chip">Trimmers</a>
          </div>
          <div class="hub-footer">
            <a href="#">Shop Grooming</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Skincare & Beauty</h3>
          <div class="hub-chips-hero"></div>
          <div class="hub-chips-container">
            <a href="#" class="hub-chip">Face Serums</a>
            <a href="#" class="hub-chip">Cleansers</a>
            <a href="#" class="hub-chip">Sun Protection</a>
            <a href="#" class="hub-chip">Masks</a>
          </div>
          <div class="hub-footer">
            <a href="#">Discover Beauty</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Groceries & Pantry</h3>
          <div class="hub-chips-hero"></div>
          <div class="hub-chips-container">
            <a href="#" class="hub-chip">Rice & Grains</a>
            <a href="#" class="hub-chip">Cooking Oils</a>
            <a href="#" class="hub-chip">Seasonings</a>
            <a href="#" class="hub-chip">Canned Foods</a>
          </div>
          <div class="hub-footer">
            <a href="#">Shop Groceries</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Household Essentials</h3>
          <div class="hub-chips-hero"></div>
          <div class="hub-chips-container">
            <a href="#" class="hub-chip">Tissue Paper</a>
            <a href="#" class="hub-chip">Air Fresheners</a>
            <a href="#" class="hub-chip">Hand Washes</a>
            <a href="#" class="hub-chip">Detergents</a>
          </div>
          <div class="hub-footer">
            <a href="#">Stock Up Now</a>
          </div>
        </div>

      </div>
    </section>
"""
text = re.sub(r'<section class="category-collections-section section-reset">.*?</section>', collections_html.strip(), text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

