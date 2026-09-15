import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace CSS
old_css_regex = r'\.hub-content \{.*?(?=\.hub-footer \{)'
new_css = """
      .hub-editorial-hero {
        width: 100%;
        aspect-ratio: 16 / 10;
        margin-bottom: 1.25rem;
      }
      .hub-hero-placeholder {
        width: 100%;
        height: 100%;
        background-color: #f4f4f4;
        border: 2px dashed #ddd;
        border-radius: 6px;
      }
      .hub-editorial-list {
        list-style: none;
        padding: 0;
        margin: 0 0 1.5rem 0;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        flex-grow: 1;
      }
      .hub-editorial-list li a {
        display: flex;
        justify-content: space-between;
        align-items: center;
        text-decoration: none;
        color: #333;
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.5rem 0;
        border-bottom: 1px solid #f0f0f0;
        transition: color 0.2s ease;
      }
      .hub-editorial-list li a:last-child {
        border-bottom: none;
      }
      .hub-editorial-list li a:hover {
        color: #ed017f;
      }
      .hub-editorial-list li a .arrow {
        color: #ccc;
        transition: transform 0.2s ease, color 0.2s ease;
      }
      .hub-editorial-list li a:hover .arrow {
        transform: translateX(4px);
        color: #ed017f;
      }

      """
text = re.sub(old_css_regex, new_css, text, flags=re.DOTALL)

# HTML for Featured Hubs
featured_html = """
    <section class="featured-hubs-section section-reset">
      <div class="container">
        <div class="featured-hubs-grid">
          
          <div class="hub-card">
            <h3 class="hub-title">Top Computing & Tech</h3>
            <div class="hub-editorial-hero">
              <div class="hub-hero-placeholder"></div>
            </div>
            <ul class="hub-editorial-list">
              <li><a href="#">HP & Asus Laptops <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Gaming Consoles <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Starlink Kits <span class="arrow">&rarr;</span></a></li>
            </ul>
            <div class="hub-footer">
              <a href="#">Shop Tech Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Bestselling Smartphones</h3>
            <div class="hub-editorial-hero">
              <div class="hub-hero-placeholder"></div>
            </div>
            <ul class="hub-editorial-list">
              <li><a href="#">Samsung Galaxy <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Apple iPhones <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Xiaomi & Redmi <span class="arrow">&rarr;</span></a></li>
            </ul>
            <div class="hub-footer">
              <a href="#">Upgrade Now</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Home & Power Essentials</h3>
            <div class="hub-editorial-hero">
              <div class="hub-hero-placeholder"></div>
            </div>
            <ul class="hub-editorial-list">
              <li><a href="#">Solar Generators <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Refrigerators <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Washing Machines <span class="arrow">&rarr;</span></a></li>
            </ul>
            <div class="hub-footer">
              <a href="#">Shop Home Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Health & Beauty Deals</h3>
            <div class="hub-editorial-hero">
              <div class="hub-hero-placeholder"></div>
            </div>
            <ul class="hub-editorial-list">
              <li><a href="#">Oral Care <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Vitamins <span class="arrow">&rarr;</span></a></li>
              <li><a href="#">Fragrances <span class="arrow">&rarr;</span></a></li>
            </ul>
            <div class="hub-footer">
              <a href="#">Discover Beauty</a>
            </div>
          </div>

        </div>
      </div>
    </section>
"""
text = re.sub(r'<section class="featured-hubs-section section-reset">.*?</section>', featured_html.strip(), text, flags=re.DOTALL)

# HTML for Category Collections
collections_html = """
    <section class="category-collections-section section-reset">
      <div class="collections-grid">
                
        <div class="hub-card">
          <h3 class="hub-title">Grooming & Personal Care</h3>
          <div class="hub-editorial-hero">
            <div class="hub-hero-placeholder"></div>
          </div>
          <ul class="hub-editorial-list">
            <li><a href="#">Hair & Beard <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Shaving Gear <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Deodorants <span class="arrow">&rarr;</span></a></li>
          </ul>
          <div class="hub-footer">
            <a href="#">Shop Grooming</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Skincare & Beauty</h3>
          <div class="hub-editorial-hero">
            <div class="hub-hero-placeholder"></div>
          </div>
          <ul class="hub-editorial-list">
            <li><a href="#">Face Serums <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Cleansers <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Sun Protection <span class="arrow">&rarr;</span></a></li>
          </ul>
          <div class="hub-footer">
            <a href="#">Discover Beauty</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Groceries & Pantry</h3>
          <div class="hub-editorial-hero">
            <div class="hub-hero-placeholder"></div>
          </div>
          <ul class="hub-editorial-list">
            <li><a href="#">Rice & Grains <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Cooking Oils <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Seasonings <span class="arrow">&rarr;</span></a></li>
          </ul>
          <div class="hub-footer">
            <a href="#">Shop Groceries</a>
          </div>
        </div>

        <div class="hub-card">
          <h3 class="hub-title">Household Essentials</h3>
          <div class="hub-editorial-hero">
            <div class="hub-hero-placeholder"></div>
          </div>
          <ul class="hub-editorial-list">
            <li><a href="#">Tissue Paper <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Air Fresheners <span class="arrow">&rarr;</span></a></li>
            <li><a href="#">Hand Washes <span class="arrow">&rarr;</span></a></li>
          </ul>
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

