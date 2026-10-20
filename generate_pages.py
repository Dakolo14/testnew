import json
import os

with open('category_data.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# Base template for subpages
def generate_html(key, cat):
    products_html = ""
    for p in cat['products']:
        products_html += f"""
          <div class=\"shop-all-product-card\">
            <div class=\"shop-all-card-top-badges\">
              <span class=\"shop-all-discount-pill\">{p['discount']}</span>
            </div>
            <div class=\"shop-all-img-wrap\">
              <img src=\"{p['img']}\" alt=\"{p['name']}\" loading=\"lazy\">
            </div>
            <div class=\"shop-all-info-wrap\">
              <p class=\"shop-all-card-title\" title=\"{p['name']}\">{p['name']}</p>
              <div class=\"shop-all-pricing-row\">
                <div class=\"shop-all-cur-price\">{p['price']}</div>
                <div class=\"shop-all-old-price\">{p['old_price']}</div>
              </div>
              <button class=\"shop-all-cart-btn\" data-test-id=\"product-card-add-to-cart\">Add to Cart</button>
            </div>
          </div>"""

    return f"""<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
    <link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Poppins:wght@400;600;700&display=swap\" rel=\"stylesheet\" />
    <title>{cat['title']}</title>
    <meta name=\"description\" content=\"{cat['desc']}\" />
    <link rel=\"stylesheet\" href=\"category-common.css\" />
    <style>
      /* Category Page Specific Enhancements */
      body {{
        background-color: #0b0b0f;
        color: #ffffff;
      }}
      .cat-page-hero {{
        width: 100%;
        max-width: 1400px;
        margin: 1.5rem auto 2rem auto;
        padding: 0 1rem;
      }}
      .cat-hero-banner {{
        background: {cat['hero_gradient']};
        border-radius: 16px;
        padding: 3rem 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.08);
      }}
      .cat-hero-banner::after {{
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(237, 1, 127, 0.25) 0%, transparent 70%);
        pointer-events: none;
      }}
      .cat-breadcrumb {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        color: rgba(255,255,255,0.7);
        margin-bottom: 1rem;
      }}
      .cat-breadcrumb a {{
        color: #ffffff;
        text-decoration: none;
        transition: color 0.2s;
      }}
      .cat-breadcrumb a:hover {{
        color: #ed017f;
      }}
      .cat-badge {{
        display: inline-block;
        background-color: #ed017f;
        color: #ffffff;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 4px 10px;
        border-radius: 9999px;
        margin-bottom: 0.75rem;
      }}
      .cat-hero-title {{
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
        line-height: 1.2;
      }}
      .cat-hero-desc {{
        font-size: 15px;
        color: rgba(255,255,255,0.85);
        max-width: 720px;
        line-height: 1.6;
      }}
      .cat-filter-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255,255,255,0.12);
        flex-wrap: wrap;
        gap: 1rem;
      }}
      .cat-count-badge {{
        font-size: 14px;
        color: rgba(255,255,255,0.9);
        font-weight: 500;
      }}
      .cat-sort-btn {{
        background: rgba(255,255,255,0.12);
        color: #fff;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }}
      .cat-back-home {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.15);
        color: #fff;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 600;
        margin-top: 1rem;
        transition: background 0.2s;
      }}
      .cat-back-home:hover {{
        background: #ed017f;
      }}
      @media (max-width: 768px) {{
        .cat-hero-banner {{
          padding: 2rem 1.25rem;
        }}
        .cat-hero-title {{
          font-size: 24px;
        }}
        .cat-hero-desc {{
          font-size: 13px;
        }}
      }}
    </style>
  </head>
  <body>
    <!-- Main Top Navigation -->
    <header class=\"navbar\">
      <nav class=\"navbar-container\">
        <div class=\"navbar-logo\">
          <a href=\"index.html\">
            <img src=\"https://www-konga-com-res.cloudinary.com/image/upload/v1789420343/landingPages/2026%20Marketing/Yakata11/logo.png\" alt=\"Konga Logo\" />
          </a>
        </div>
        <div class=\"nav-wrapper\">
          <ul class=\"nav-items\">
            <li><a href=\"index.html\">Home</a></li>
            <li><a href=\"samsung-phones.html\">Phones</a></li>
            <li><a href=\"laptops.html\">Computers</a></li>
            <li><a href=\"consoles.html\">Gaming</a></li>
            <li><a href=\"acs.html\">Appliances</a></li>
            <li><a href=\"wigs.html\">Beauty</a></li>
          </ul>
        </div>
      </nav>
    </header>

    <!-- Category Header Hero -->
    <section class=\"cat-page-hero\">
      <div class=\"cat-hero-banner\">
        <div class=\"cat-breadcrumb\">
          <a href=\"index.html\">Home</a>
          <span>&rsaquo;</span>
          <a href=\"index.html#featured-categories\">Featured Categories</a>
          <span>&rsaquo;</span>
          <span>{cat['heading']}</span>
        </div>
        
        <span class=\"cat-badge\">{cat['badge']}</span>
        <h1 class=\"cat-hero-title\">{cat['heading']}</h1>
        <p class=\"cat-hero-desc\">{cat['desc']}</p>

        <div class=\"cat-filter-bar\">
          <div class=\"cat-count-badge\">Showing {len(cat['products'])} Featured Yakata Deals</div>
          <div>
            <a href=\"index.html\" class=\"cat-back-home\">&larr; Back to Main Yakata Page</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Product Grid Section -->
    <section class=\"shop-all-section section-reset\" style=\"margin-top: 1rem !important;\">
      <div class=\"shop-by-category-header\" style=\"background-color: #ed017f; border-radius: 12px 12px 0 0;\">
        <div style=\"display: flex; justify-content: space-between; width: 100%; align-items: center;\">
          <span>{cat['heading']} Deals</span>
          <a href=\"https://www.konga.com/search?search={key.replace('-', '+')}\" target=\"_blank\" class=\"flash-more\" style=\"color: #ffffff; font-size: 14px; text-decoration: none; display: flex; align-items: center; gap: 8px;\">
            View All On Konga
            <span class=\"icon-circle\" style=\"background-color: #ffffff; border-radius: 50%; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center;\">
              <svg width=\"12\" height=\"12\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">
                <path d=\"M9 18L15 12L9 6\" stroke=\"#ed017f\" stroke-width=\"4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>
              </svg>
            </span>
          </a>
        </div>
      </div>
      <div class=\"shop-all-container\">
        <div class=\"shop-all-grid\">{products_html}
        </div>
      </div>
    </section>

    <!-- Written SEO Footer Section -->
    <section class=\"written-seo\" style=\"margin-top: 3rem !important;\">
      <h2>Shop Genuine {cat['heading']} During Konga Yakata 2026</h2>
      <p>{cat['desc']}</p>
      <p>Enjoy guaranteed 100% authentic products sourced directly from manufacturers, flexible payment options with KongaPay, secure nationwide logistics, and 7-day hassle-free returns.</p>
    </section>

  </body>
</html>
"""

for key, cat in categories.items():
    filename = f"{key}.html"
    content = generate_html(key, cat)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {filename}")

print("All 12 category pages generated successfully!")
