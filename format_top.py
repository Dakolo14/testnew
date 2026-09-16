import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace top section CSS
# We will just inject the new CSS and remove both hub-avatar and hub-editorial CSS to be safe.
css_to_remove = r'(/\* Top Section: Circular Avatars \*/.*?\.hub-avatar-label \{.*?\})|(/\* Top Section: Editorial / Hero List \*/.*?\.hub-editorial-list li a:hover \.arrow \{.*?\})|(\.hub-editorial-hero \{.*?(?=\.hub-footer \{))'

text = re.sub(css_to_remove, "", text, flags=re.DOTALL)

new_css = """
      /* Top Section: Full-Bleed Quarters */
      .hub-quad-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr;
        gap: 6px;
        aspect-ratio: 1 / 1;
        margin-bottom: 1.25rem;
        flex-grow: 1;
        border-radius: 8px;
        overflow: hidden;
      }
      .hub-quad-item {
        position: relative;
        background-color: #f4f4f4;
        text-decoration: none;
        overflow: hidden;
      }
      .hub-quad-placeholder {
        width: 100%;
        height: 100%;
        background-color: #eee;
        transition: transform 0.4s ease;
      }
      .hub-quad-item:hover .hub-quad-placeholder {
        transform: scale(1.1);
      }
      .hub-quad-label {
        position: absolute;
        bottom: 8px;
        left: 8px;
        font-size: 0.7rem;
        font-weight: 700;
        color: #fff;
        background-color: rgba(0,0,0,0.6);
        padding: 4px 8px;
        border-radius: 4px;
        z-index: 2;
        max-width: 85%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      
"""
# inject new CSS right before .hub-footer
text = text.replace('.hub-footer {', new_css + '\n      .hub-footer {')


featured_html = """
    <section class="featured-hubs-section section-reset">
      <div class="container">
        <div class="featured-hubs-grid">
          
          <div class="hub-card">
            <h3 class="hub-title">Top Computing & Tech</h3>
            <div class="hub-quad-grid">
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #e2e8f0;"></div>
                <span class="hub-quad-label">Laptops</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #cbd5e1;"></div>
                <span class="hub-quad-label">Consoles</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #94a3b8;"></div>
                <span class="hub-quad-label">Starlink</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #64748b;"></div>
                <span class="hub-quad-label">Printers</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Shop Tech Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Bestselling Smartphones</h3>
            <div class="hub-quad-grid">
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #f1f5f9;"></div>
                <span class="hub-quad-label">Samsung</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #e2e8f0;"></div>
                <span class="hub-quad-label">iPhones</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #cbd5e1;"></div>
                <span class="hub-quad-label">Xiaomi</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #94a3b8;"></div>
                <span class="hub-quad-label">Tecno</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Upgrade Now</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Home & Power</h3>
            <div class="hub-quad-grid">
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #f8fafc;"></div>
                <span class="hub-quad-label">Generators</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #f1f5f9;"></div>
                <span class="hub-quad-label">Fridges</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #e2e8f0;"></div>
                <span class="hub-quad-label">Washers</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #cbd5e1;"></div>
                <span class="hub-quad-label">ACs</span>
              </a>
            </div>
            <div class="hub-footer">
              <a href="#">Shop Home Deals</a>
            </div>
          </div>

          <div class="hub-card">
            <h3 class="hub-title">Health & Beauty</h3>
            <div class="hub-quad-grid">
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #f1f5f9;"></div>
                <span class="hub-quad-label">Oral Care</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #e2e8f0;"></div>
                <span class="hub-quad-label">Vitamins</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #cbd5e1;"></div>
                <span class="hub-quad-label">Fragrances</span>
              </a>
              <a href="#" class="hub-quad-item">
                <div class="hub-quad-placeholder" style="background-color: #94a3b8;"></div>
                <span class="hub-quad-label">Makeup</span>
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

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

