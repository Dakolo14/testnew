import json
import os

with open('category_data.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# Subcategories configuration for each page with curated promo buckets
PAGE_CONFIG = {
    "samsung-phones": {
        "badge": "Samsung Galaxy Store",
        "subcategories": [
            {"name": "Galaxy S Series", "tag": "Flagships", "icon": "👑"},
            {"name": "Galaxy Z Fold & Flip", "tag": "Foldables", "icon": "📱"},
            {"name": "Galaxy A Series", "tag": "Best Sellers", "icon": "🔥"},
            {"name": "Galaxy Watches & Buds", "tag": "Accessories", "icon": "🎧"},
            {"name": "Tablets & Tab S", "tag": "Productivity", "icon": "💻"},
            {"name": "Official Chargers", "tag": "Original 25W/45W", "icon": "⚡"}
        ],
        "promo_buckets": [
            {
                "title": "Galaxy AI Experience Drop",
                "tag": "Next-Gen Mobile",
                "desc": "Trade up to Galaxy S24 Ultra & S24+. Enjoy live translation, Circle to Search, and pro-visual engine cameras at unprecedented Yakata markdown prices.",
                "features": ["Free Official 45W Fast Charger on selected models", "Up to 24 Months Official Samsung Care+ Warranty", "Next-day delivery available across major cities"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/B/M/186576_1785291116.jpg",
                "cta_text": "Shop Galaxy AI",
                "cta_link": "https://www.konga.com/search?search=samsung+galaxy+s24"
            },
            {
                "title": "Galaxy A-Series Value Blast",
                "tag": "Everyday Champions",
                "desc": "Long-lasting 5000mAh batteries, Super AMOLED 120Hz displays, and multi-lens cameras starting from under ₦150,000.",
                "features": ["Super AMOLED 120Hz smooth scrolling", "50MP OIS Nightography camera system", "KongaPay Instant 10% Extra Savings applied"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/M/X/118566_1774944999.jpg",
                "cta_text": "Explore A-Series",
                "cta_link": "https://www.konga.com/search?search=samsung+galaxy+a"
            }
        ]
    },
    "iphones": {
        "badge": "Apple Certified Store",
        "subcategories": [
            {"name": "iPhone 16 Series", "tag": "Latest Drop", "icon": "🔥"},
            {"name": "iPhone 15 Series", "tag": "Pro Grade", "icon": "⚡"},
            {"name": "iPhone 14 & 13", "tag": "Value Deals", "icon": "💎"},
            {"name": "Apple Watches", "tag": "Ultra & Series 10", "icon": "⌚"},
            {"name": "AirPods & Max", "tag": "Spatial Audio", "icon": "🎧"},
            {"name": "Original MagSafe & Power", "tag": "20W / 30W", "icon": "🔌"}
        ],
        "promo_buckets": [
            {
                "title": "iPhone 16 Pro Max Flash Drop",
                "tag": "Desert Titanium A18 Pro",
                "desc": "Experience Camera Control, 4K 120 fps Dolby Vision, and groundbreaking battery life on factory-unlocked iPhone 16 series.",
                "features": ["100% Factory Unlocked (Nano SIM + eSIM)", "1-Year Official Apple Warranty", "Discreet, fully insured premium courier transit"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/T/T/161515_1790884755.jpg",
                "cta_text": "Shop iPhone 16",
                "cta_link": "https://www.konga.com/search?search=iphone+16"
            },
            {
                "title": "Pre-Owned & Open-Box Apple Deals",
                "tag": "Grade A+ Inspected",
                "desc": "Get iPhone 13, 14, and 15 flagships in pristine condition with 100% battery health check and 30-day warranty starting under ₦800k.",
                "features": ["100% Tested 45-point hardware inspection", "Factory original displays and camera sensors", "Complimentary 20W USB-C fast charging kit"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/Z/X/250053_1786663170.jpg",
                "cta_text": "Explore Certified iPhones",
                "cta_link": "https://www.konga.com/search?search=apple+iphone"
            }
        ]
    },
    "xiaomi-phones": {
        "badge": "Xiaomi Official Deals",
        "subcategories": [
            {"name": "Redmi Note 13 Series", "tag": "200MP OIS", "icon": "📸"},
            {"name": "POCO Series", "tag": "Gaming Beasts", "icon": "⚡"},
            {"name": "Redmi Number Series", "tag": "13C / 14C", "icon": "🔋"},
            {"name": "Xiaomi Smart Bands", "tag": "Fitness", "icon": "🏃"},
            {"name": "Fast Power Banks", "tag": "20000mAh", "icon": "🔋"},
            {"name": "Smart Home & Audio", "tag": "Ecosystem", "icon": "🏠"}
        ],
        "promo_buckets": [
            {
                "title": "Redmi Note 13 Pro+ 5G Mega Cut",
                "tag": "120W HyperCharge",
                "desc": "Curved AMOLED 1.5K screen, 200MP flagship OIS camera, and zero to 100% charge in just 19 minutes with Xiaomi HyperOS.",
                "features": ["IP68 Water & Dust Resistance rating", "120W In-box Gallium Nitride Charger included", "Huge ₦155,000 instant Yakata discount"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg",
                "cta_text": "Grab Note 13 Pro+",
                "cta_link": "https://www.konga.com/search?search=redmi+note+13"
            },
            {
                "title": "POCO Performance Beast Zone",
                "tag": "Snapdragon 8s Gen 3",
                "desc": "Built for competitive mobile gamers with LiquidCool 4.0 vapor chambers and WildBoost optimization at mid-range prices.",
                "features": ["120Hz Flow AMOLED crystal clear visuals", "Ultra-stable frame rates on PUBG & COD Mobile", "Free gamer earbuds on select orders"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/D/Y/118566_1768920113.jpg",
                "cta_text": "Shop POCO Beasts",
                "cta_link": "https://www.konga.com/search?search=poco+x6"
            }
        ]
    },
    "infinix-phones": {
        "badge": "Infinix Mobile Store",
        "subcategories": [
            {"name": "Infinix Note 40 Series", "tag": "Wireless All-Round", "icon": "⚡"},
            {"name": "Infinix Hot 50 Series", "tag": "Smooth 120Hz", "icon": "🔥"},
            {"name": "Infinix Smart 8 Series", "tag": "Under ₦120k", "icon": "💰"},
            {"name": "Infinix GT 20 Pro", "tag": "Gaming Flagship", "icon": "🎮"},
            {"name": "Zero Series Flagships", "tag": "4K 60fps Vlogging", "icon": "🎬"},
            {"name": "MagCharge & Power", "tag": "Originals", "icon": "🔌"}
        ],
        "promo_buckets": [
            {
                "title": "Infinix Note 40 Pro 5G Wireless Kit",
                "tag": "All-Round FastCharge 2.0",
                "desc": "70W Multi-Speed FastCharge + 20W Wireless MagCharge. Includes 3D-Curved 120Hz AMOLED display and Halo Active Lighting.",
                "features": ["Free MagCase & MagCharge Wireless Pad in the box", "Cheetah X1 Dedicated Charging Chipset", "2-Year VIP warranty and screen protection"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/H/A/118566_1789549980.jpg",
                "cta_text": "Shop Note 40 Pro",
                "cta_link": "https://www.konga.com/search?search=infinix+note+40"
            },
            {
                "title": "Campus & Pocket Super Savers",
                "tag": "Hot 50 & Smart 8",
                "desc": "Ultra-slim body, Dynamic Bar notifications, and 5000mAh battery that keeps going all weekend without recharge anxiety.",
                "features": ["Up to 8GB Extended RAM for smooth multitasking", "Side-mounted biometric fingerprint security", "Prices starting from ₦108,000 only"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/H/A/118566_1789549980.jpg",
                "cta_text": "Shop Hot Series",
                "cta_link": "https://www.konga.com/search?search=infinix+hot"
            }
        ]
    },
    "laptops": {
        "badge": "Top Computing & Laptops",
        "subcategories": [
            {"name": "HP Business & Pavilion", "tag": "Core i5 / i7", "icon": "💼"},
            {"name": "ASUS Zenbook & TUF", "tag": "OLED & Gaming", "icon": "💻"},
            {"name": "Apple MacBooks", "tag": "M2 / M3 / M5", "icon": "🍏"},
            {"name": "Lenovo IdeaPad & ThinkPad", "tag": "Durability", "icon": "⚙️"},
            {"name": "Dell Inspiron & Latitude", "tag": "Workhorses", "icon": "🏢"},
            {"name": "Laptop Bags & Docks", "tag": "Accessories", "icon": "🎒"}
        ],
        "promo_buckets": [
            {
                "title": "HP 240R G10 Commercial Workhorse",
                "tag": "Intel Core 7-150U Power",
                "desc": "Built for modern hybrid professionals with 16GB high-speed memory, 512GB NVMe SSD, and Windows 11 Pro preloaded.",
                "features": ["14\" Anti-Glare FHD narrow-border display", "Long-lasting HP Fast Charge 3-cell 41Wh battery", "Save over ₦160,000 on official HP stock"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/R/H/_1784902533.png",
                "cta_text": "Shop HP Notebooks",
                "cta_link": "https://www.konga.com/search?search=hp+laptop"
            },
            {
                "title": "High-Performance Gaming & Creators",
                "tag": "RTX 4060 / 4070 Ready",
                "desc": "High refresh rate ASUS TUF and Zenbook OLED laptops built for 3D rendering, video editing, and AAA esports dominance.",
                "features": ["144Hz - 240Hz esports display options", "Advanced dual-fan self-cleaning thermal cooling", "Free gaming bag on orders above ₦1.5m"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/H/Y/56319_1786712399.jpg",
                "cta_text": "Explore Gaming Laptops",
                "cta_link": "https://www.konga.com/search?search=asus+gaming+laptop"
            }
        ]
    },
    "consoles": {
        "badge": "Console Gaming Hub",
        "subcategories": [
            {"name": "PlayStation 5 Slim", "tag": "Disc & Digital", "icon": "🎮"},
            {"name": "Xbox Series X / S", "tag": "Game Pass Hub", "icon": "🟢"},
            {"name": "Nintendo Switch OLED", "tag": "Portable Fun", "icon": "🕹️"},
            {"name": "DualSense Controllers", "tag": "Haptic Feedback", "icon": "🎯"},
            {"name": "EA FC 25 & Hit Games", "tag": "Top Titles", "icon": "⚽"},
            {"name": "Gaming Headsets & Gear", "tag": "Pulse 3D", "icon": "🎧"}
        ],
        "promo_buckets": [
            {
                "title": "PS5 Slim Disc + FC 25 Mega Bundle",
                "tag": "Ultimate Match Day",
                "desc": "Ultra-fast 1TB NVMe SSD, Ray Tracing, 4K 120Hz HDR output, bundled with two DualSense controllers and EA FC 25 disc.",
                "features": ["Official Sony Interactive Entertainment warranty", "Includes extra DualSense controller for co-op games", "Save ₦185,000 with Yakata bundle pricing"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/Z/W/240947_1783276152.jpg",
                "cta_text": "Claim PS5 Bundle",
                "cta_link": "https://www.konga.com/search?search=playstation+5"
            },
            {
                "title": "Xbox Series X | S Game Pass Vault",
                "tag": "120 FPS Quick Resume",
                "desc": "The most powerful console hardware ever engineered. Play hundreds of games on day one with 3-month Game Pass Ultimate included.",
                "features": ["12 Teraflops GPU processing muscle", "Instant Quick Resume across up to 5 games simultaneously", "Whisper-quiet architecture vapor chamber design"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg",
                "cta_text": "Explore Xbox Consoles",
                "cta_link": "https://www.konga.com/search?search=xbox+series"
            }
        ]
    },
    "washers": {
        "badge": "Laundry Appliances",
        "subcategories": [
            {"name": "Front Load Washers", "tag": "AI DD Inverters", "icon": "🔄"},
            {"name": "Top Load Washers", "tag": "Smart Inverters", "icon": "🧺"},
            {"name": "Twin Tub Washers", "tag": "Gen Compatible", "icon": "⚡"},
            {"name": "Washer-Dryer Combos", "tag": "All-in-One", "icon": "💨"},
            {"name": "Commercial Washers", "tag": "Heavy Duty 15kg+", "icon": "🏢"},
            {"name": "Covers & Detergents", "tag": "Care Kits", "icon": "🧴"}
        ],
        "promo_buckets": [
            {
                "title": "LG AI DD Intelligent Front Loaders",
                "tag": "18% More Fabric Care",
                "desc": "AI Direct Drive detects fabric weight and softness to choose optimal wash motions automatically. Built-in Steam eliminates 99.9% allergens.",
                "features": ["TurboWash 360 completes clean cycle in 39 mins", "10-Year Inverter Direct Drive motor warranty", "SmartThinQ WiFi remote control from your phone"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/A/O/231472_1777545584.jpg",
                "cta_text": "Shop LG Washers",
                "cta_link": "https://www.konga.com/search?search=lg+washing+machine"
            },
            {
                "title": "Low Voltage & Gen-Friendly Twin Tubs",
                "tag": "Haier Thermocool & Scanfrost",
                "desc": "Wash full family laundry loads using your small generator. Double tub design allows washing and spinning at the same time.",
                "features": ["Runs comfortably on 1.5kVA generators", "Rust-free plastic body prevents bathroom corrosion", "Special soak cycle for stubborn collar stains"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/R/I/140630_1725641773.jpg",
                "cta_text": "Shop Twin Tubs",
                "cta_link": "https://www.konga.com/search?search=twin+tub+washing+machine"
            }
        ]
    },
    "acs": {
        "badge": "Cool Zone & Climate",
        "subcategories": [
            {"name": "Inverter Split ACs", "tag": "Up to 70% Energy Save", "icon": "❄️"},
            {"name": "Gen-Cool Compatible", "tag": "Low Voltage", "icon": "⚡"},
            {"name": "Floor Standing Tower", "tag": "2.0HP - 5.0HP", "icon": "🏢"},
            {"name": "1.0HP & 1.5HP ACs", "tag": "Bedroom Comfort", "icon": "🛏️"},
            {"name": "Copper Condenser Units", "tag": "Anti-Rust", "icon": "🛡️"},
            {"name": "AC Installation Kits", "tag": "Pipes & Brackets", "icon": "🔧"}
        ],
        "promo_buckets": [
            {
                "title": "LG Dual Inverter Gen-Cool ACs",
                "tag": "Runs on Small Generators",
                "desc": "Dual Inverter compressor saves up to 70% electricity and cools 40% faster. Gen-Mode allows the AC to run on your generator without tripping.",
                "features": ["10-Year compressor manufacturer warranty", "Gold Fin anti-corrosion coating for coastal humidity", "Ultra-quiet operation at just 19 decibels"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg",
                "cta_text": "Shop Dual Inverter ACs",
                "cta_link": "https://www.konga.com/search?search=lg+inverter+ac"
            },
            {
                "title": "Carrier & Hisense Fast-Cool Specials",
                "tag": "100% Pure Copper Pipes",
                "desc": "Heavy-duty outdoor condensers engineered for Nigerian power fluctuations and tropical heat waves. Immediate freezing cold air in minutes.",
                "features": ["R410A Eco-friendly zero ozone depletion gas", "High-density multi-stage air purification filter", "Free installation pipe and bracket kit included"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/M/X/104208_1630012306.jpg",
                "cta_text": "Explore Split ACs",
                "cta_link": "https://www.konga.com/search?search=split+air+conditioner"
            }
        ]
    },
    "fridges": {
        "badge": "Cool Zone Refrigeration",
        "subcategories": [
            {"name": "Double Door Fridges", "tag": "No Frost Inverter", "icon": "🧊"},
            {"name": "Chest Freezers", "tag": "100-Hour Frost", "icon": "❄️"},
            {"name": "French Door & Side-by-Side", "tag": "Luxury 450L+", "icon": "💎"},
            {"name": "Single Door & Bedside", "tag": "Compact 90L-150L", "icon": "🚪"},
            {"name": "Bottom Freezer Units", "tag": "Easy Access", "icon": "🍓"},
            {"name": "Surge Guards & Voltage", "tag": "Compressor Safety", "icon": "⚡"}
        ],
        "promo_buckets": [
            {
                "title": "Haier Thermocool 100-Hour Frost Retention",
                "tag": "Beat Blackouts",
                "desc": "Deep chest freezers engineered with extra thick foaming to keep meats, soups, and drinks frozen for over 4 days after power outage.",
                "features": ["Low voltage operation down to 160V", "Anti-rust zinc galvanized cabinet body", "Super freezing function with LED cabinet lighting"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/X/W/118566_1544086101.jpg",
                "cta_text": "Shop Chest Freezers",
                "cta_link": "https://www.konga.com/search?search=chest+freezer"
            },
            {
                "title": "Samsung Twin Cooling Plus Multi-Door",
                "tag": "Keeps Food Fresh 2X Longer",
                "desc": "Separate cooling evaporators for fridge and freezer compartments eliminate odor mixing and preserve 70% natural food humidity.",
                "features": ["Convertible 5-in-1 smart cooling modes", "Digital Inverter Compressor with 20-Year warranty", "Fingerprint-resistant premium matte silver finish"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/K/H/118566_1747148808.png",
                "cta_text": "Shop Multi-Door Fridges",
                "cta_link": "https://www.konga.com/search?search=samsung+refrigerator"
            }
        ]
    },
    "sexual-wellness": {
        "badge": "Discrete Care & Wellness",
        "subcategories": [
            {"name": "Premium Condoms", "tag": "Durex & Fiesta", "icon": "🛡️"},
            {"name": "Pleasure Lubricants", "tag": "Water & Silicone", "icon": "💧"},
            {"name": "Massage & Warming Gels", "tag": "2-in-1 Sensual", "icon": "✨"},
            {"name": "Performance Aids", "tag": "Endurance & Delay", "icon": "⏱️"},
            {"name": "Intimate Hygiene", "tag": "pH Balanced", "icon": "🌸"},
            {"name": "Multipack Value Bundles", "tag": "Save up to 40%", "icon": "📦"}
        ],
        "promo_buckets": [
            {
                "title": "100% Discrete Packaging Guarantee",
                "tag": "Total Privacy",
                "desc": "Your privacy is paramount. Every order is packed in plain, unbranded opaque boxes with zero indication of contents or category on the label.",
                "features": ["No product names visible on exterior packaging", "Confidential delivery straight to your doorstep or Konga pickup store", "Secure online payment with KongaPay for zero card trace"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png",
                "cta_text": "Explore Wellness Hub",
                "cta_link": "https://www.konga.com/search?search=sexual+wellness"
            },
            {
                "title": "Durex Sensation & Pleasure Bundles",
                "tag": "Fetherlite & Extra Safe",
                "desc": "World's #1 condom brand with dermatologically tested natural rubber latex and sensual water-based lubricants for silky smooth comfort.",
                "features": ["Electronically tested 5 times for safety and strength", "Mutual Climax ribbing & delay benzocaine technology", "Bulk multi-pack discounts with up to 35% Yakata savings"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png",
                "cta_text": "Shop Durex Packs",
                "cta_link": "https://www.konga.com/search?search=durex"
            }
        ]
    },
    "wigs": {
        "badge": "Beauty & Hair Lounge",
        "subcategories": [
            {"name": "Bone Straight Wigs", "tag": "Double Drawn", "icon": "✨"},
            {"name": "Deep Wave & Curly", "tag": "Bouncy Curls", "icon": "🌊"},
            {"name": "Glueless Bob Wigs", "tag": "Wear & Go", "icon": "💇‍♀️"},
            {"name": "HD Lace Frontals", "tag": "13x4 / 13x6 Invisible", "icon": "🎀"},
            {"name": "Human Hair Bundles", "tag": "Virgin Grade 12A", "icon": "👑"},
            {"name": "Lace Glues & Tools", "tag": "Hot Combs & Wax", "icon": "💄"}
        ],
        "promo_buckets": [
            {
                "title": "Virgin Human Hair Bone Straight Vault",
                "tag": "Zero Tangle & Shed-Free",
                "desc": "100% unprocessed human hair from single donors. Silky bone straight texture that stays sleek even in tropical humidity, ready to bleach and dye.",
                "features": ["Pre-plucked natural hairline with baby hairs", "Available from 16-inch to 32-inch lengths", "Free satin bonnet & edge brush with every wig"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/V/N/240104_1742889486.jpg",
                "cta_text": "Shop Bone Straight",
                "cta_link": "https://www.konga.com/search?search=bone+straight+wig"
            },
            {
                "title": "5-Minute Wear & Go Glueless Bobs",
                "tag": "Beginner Friendly",
                "desc": "No glue, no spray, no headache. Elastic band install gives an undetectable scalp melt in under 3 minutes for office and weekend glam.",
                "features": ["Pre-cut transparent HD lace for instant fit", "180% full natural density volume", "Yakata price drop starting from under ₦50,000"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/V/N/240104_1742889486.jpg",
                "cta_text": "Explore Glueless Bobs",
                "cta_link": "https://www.konga.com/search?search=glueless+bob+wig"
            }
        ]
    },
    "makeup": {
        "badge": "Cosmetics & Glam Store",
        "subcategories": [
            {"name": "Foundations & Primers", "tag": "Matte Poreless", "icon": "✨"},
            {"name": "Setting Powders & Sprays", "tag": "All-Day Lock", "icon": "💨"},
            {"name": "Eyeshadows & Liners", "tag": "High Pigment", "icon": "👁️"},
            {"name": "Lip Glosses & Mattes", "tag": "Long Lasting", "icon": "💋"},
            {"name": "18pc Makeup Brush Sets", "tag": "Pro Grade", "icon": "🖌️"},
            {"name": "Skincare Prep & Remover", "tag": "Gentle Cleansing", "icon": "🧴"}
        ],
        "promo_buckets": [
            {
                "title": "Pro Longwear Matte Foundations",
                "tag": "Shades for Every Melanin Tone",
                "desc": "Oil-free, shine-control formulas from Fenty Beauty, Maybelline Fit Me, and Mary Kay that resist transfer in heat and humidity.",
                "features": ["24-Hour humidity-proof and sweat-resistant wear", "Pore-blurring micro-powder technology", "Guaranteed 100% original manufacturer stock"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg",
                "cta_text": "Shop Foundations",
                "cta_link": "https://www.konga.com/search?search=matte+foundation"
            },
            {
                "title": "Beauty Bag Must-Haves Under ₦20,000",
                "tag": "Budget Glam Steals",
                "desc": "Stock up on Milani setting sprays, classic liquid lipsticks, sponge blenders, and 18-piece soft synthetic brush sets at massive discounts.",
                "features": ["Complete makeup toolkit essentials in one order", "Cruelty-free dermatologically approved cosmetics", "Discounts up to 40% throughout Yakata season"],
                "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_800,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg",
                "cta_text": "Shop Budget Glam",
                "cta_link": "https://www.konga.com/search?search=makeup"
            }
        ]
    }
}

def generate_subcategories_html(subcats, page_key):
    chips_html = ""
    for s in subcats:
        chips_html += f"""
          <a href="https://www.konga.com/search?search={s['name'].replace(' ', '+').replace('&', '%26')}" target="_blank" class="subcat-chip-card">
            <div class="subcat-chip-icon">{s['icon']}</div>
            <div class="subcat-chip-info">
              <span class="subcat-chip-name">{s['name']}</span>
              <span class="subcat-chip-tag">{s['tag']}</span>
            </div>
          </a>"""
    return chips_html

def generate_promo_buckets_html(buckets):
    cards_html = ""
    for b in buckets:
        features_html = "".join([f"<li>{feat}</li>" for feat in b['features']])
        cards_html += f"""
        <div class="promo-card">
          <span class="promo-tag">{b['tag']}</span>
          <h3 class="promo-title">{b['title']}</h3>
          <p class="promo-desc">{b['desc']}</p>
          <ul class="promo-features">
            {features_html}
          </ul>
          <div class="promo-image-placeholder">
            <img src="{b['img']}" alt="{b['title']}" loading="lazy">
          </div>
          <a href="{b['cta_link']}" target="_blank" class="promo-action">{b['cta_text']}</a>
        </div>"""
    return cards_html

def generate_html(key, cat):
    cfg = PAGE_CONFIG.get(key, {
        "badge": cat.get('badge', 'Yakata Deals'),
        "subcategories": [],
        "promo_buckets": []
    })

    products_html = ""
    for p in cat['products']:
        products_html += f"""
          <div class="shop-all-product-card">
            <div class="shop-all-card-top-badges">
              <span class="shop-all-discount-pill">{p['discount']}</span>
            </div>
            <div class="shop-all-img-wrap">
              <img src="{p['img']}" alt="{p['name']}" loading="lazy">
            </div>
            <div class="shop-all-info-wrap">
              <p class="shop-all-card-title" title="{p['name']}">{p['name']}</p>
              <div class="shop-all-pricing-row">
                <div class="shop-all-cur-price">{p['price']}</div>
                <div class="shop-all-old-price">{p['old_price']}</div>
              </div>
              <button class="shop-all-cart-btn" data-test-id="product-card-add-to-cart">Add to Cart</button>
            </div>
          </div>"""

    subcats_html = generate_subcategories_html(cfg['subcategories'], key)
    promo_buckets_html = generate_promo_buckets_html(cfg['promo_buckets'])

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
    <title>{cat['title']}</title>
    <meta name="description" content="{cat['desc']}" />
    <link rel="stylesheet" href="category-common.css" />
    <style>
      /* Category Page Specific Enhancements */
      body {{
        background-color: #000000;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
      }}
      .cat-page-hero {{
        width: 100%;
        max-width: 1400px;
        margin: 1.5rem auto 1rem auto;
        padding: 0 1rem;
      }}
      .cat-hero-banner {{
        background: {cat['hero_gradient']};
        border-radius: 16px;
        padding: 2.5rem 2.25rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255,255,255,0.1);
      }}
      .cat-hero-banner::after {{
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 380px;
        height: 380px;
        background: radial-gradient(circle, rgba(237, 1, 127, 0.3) 0%, transparent 70%);
        pointer-events: none;
      }}
      .cat-breadcrumb {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        color: rgba(255,255,255,0.7);
        margin-bottom: 0.85rem;
        flex-wrap: wrap;
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
        padding: 4px 12px;
        border-radius: 9999px;
        margin-bottom: 0.75rem;
      }}
      .cat-hero-title {{
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.65rem;
        line-height: 1.2;
        font-family: 'Poppins', sans-serif;
      }}
      .cat-hero-desc {{
        font-size: 15px;
        color: rgba(255,255,255,0.9);
        max-width: 760px;
        line-height: 1.6;
        font-weight: 300;
      }}
      .cat-filter-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.25rem;
        padding-top: 1.25rem;
        border-top: 1px solid rgba(255,255,255,0.15);
        flex-wrap: wrap;
        gap: 1rem;
      }}
      .cat-count-badge {{
        font-size: 14px;
        color: rgba(255,255,255,0.95);
        font-weight: 500;
      }}
      .cat-back-home {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.15);
        color: #fff;
        text-decoration: none;
        padding: 8px 18px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 600;
        transition: background 0.2s;
      }}
      .cat-back-home:hover {{
        background: #ed017f;
      }}

      /* --- Subcategories Grid Section --- */
      .subcategories-section {{
        width: 100%;
        max-width: 1400px;
        margin: 1.5rem auto 2.5rem auto;
        padding: 0 1rem;
      }}
      .subcategories-container {{
        background: #111116;
        border: 1px solid rgba(255,255,255,0.08);
        border-top: none;
        border-radius: 0 0 12px 12px;
        padding: 1.25rem 1rem;
      }}
      .subcategories-grid {{
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 12px;
      }}
      .subcat-chip-card {{
        background: #18181f;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 12px 10px;
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        color: #fff;
        transition: transform 0.25s ease, border-color 0.25s ease, background 0.25s ease;
      }}
      .subcat-chip-card:hover {{
        transform: translateY(-3px);
        border-color: #ed017f;
        background: #20202a;
      }}
      .subcat-chip-icon {{
        font-size: 22px;
        line-height: 1;
        flex-shrink: 0;
      }}
      .subcat-chip-info {{
        display: flex;
        flex-direction: column;
        overflow: hidden;
      }}
      .subcat-chip-name {{
        font-size: 13px;
        font-weight: 600;
        color: #ffffff;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .subcat-chip-tag {{
        font-size: 11px;
        color: #ed017f;
        font-weight: 500;
        margin-top: 2px;
      }}

      /* Promo Banners Section Overrides for Subpages */
      .subpage-promo-section {{
        width: 100%;
        max-width: 1400px;
        margin: 3rem auto 2rem auto;
        padding: 0 1rem;
      }}
      .subpage-promo-section .promo-banners-grid {{
        max-width: 100%;
      }}
      .subpage-promo-section .promo-image-placeholder {{
        height: 220px;
        background: #1a1a24;
      }}
      .subpage-promo-section .promo-image-placeholder img {{
        height: 100%;
        width: 100%;
        object-fit: contain;
        padding: 12px;
        background: #ffffff;
      }}

      @media (max-width: 1024px) {{
        .subcategories-grid {{
          grid-template-columns: repeat(3, 1fr);
        }}
      }}
      @media (max-width: 640px) {{
        .subcategories-grid {{
          grid-template-columns: repeat(2, 1fr);
          gap: 8px;
        }}
        .cat-hero-banner {{
          padding: 1.75rem 1.25rem;
        }}
        .cat-hero-title {{
          font-size: 24px;
        }}
        .cat-hero-desc {{
          font-size: 13px;
        }}
        .subcat-chip-card {{
          padding: 10px 8px;
        }}
        .subcat-chip-name {{
          font-size: 12px;
        }}
      }}
    </style>
  </head>
  <body>
    <!-- Main Top Navigation (Identical to Yakata Main Landing Page) -->
    <header class="navbar">
      <nav class="navbar-container">
        <div class="navbar-logo">
          <a href="index.html">
            <img src="https://www-konga-com-res.cloudinary.com/image/upload/v1789420343/landingPages/2026%20Marketing/Yakata11/logo.png" alt="Konga Logo" />
          </a>
        </div>
        <div class="nav-wrapper">
          <ul class="nav-items">
            <li><a href="index.html">Home</a></li>
            <li><a href="samsung-phones.html">Phones & Tablets</a></li>
            <li><a href="laptops.html">Computers</a></li>
            <li><a href="consoles.html">Electronics</a></li>
            <li><a href="acs.html">Home & Kitchen</a></li>
            <li><a href="makeup.html">Beauty</a></li>
          </ul>
        </div>
      </nav>
    </header>

    <!-- Category Header Hero -->
    <section class="cat-page-hero">
      <div class="cat-hero-banner">
        <div class="cat-breadcrumb">
          <a href="index.html">Home</a>
          <span>&rsaquo;</span>
          <a href="index.html#featured-categories">Categories</a>
          <span>&rsaquo;</span>
          <span>{cat['heading']}</span>
        </div>
        
        <span class="cat-badge">{cfg['badge']}</span>
        <h1 class="cat-hero-title">{cat['heading']}</h1>
        <p class="cat-hero-desc">{cat['desc']}</p>

        <div class="cat-filter-bar">
          <div class="cat-count-badge">Showing {len(cat['products'])} Verified Yakata Deals</div>
          <div>
            <a href="index.html" class="cat-back-home">&larr; Back to Main Yakata Page</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 1. Sub Categories Section -->
    <section class="subcategories-section section-reset">
      <div class="shop-by-category-header" style="background-color: #ed017f; border-radius: 12px 12px 0 0;">
        <span>Shop Sub-Categories</span>
        <span class="yakata-badge">Explore All</span>
      </div>
      <div class="subcategories-container">
        <div class="subcategories-grid">
          {subcats_html}
        </div>
      </div>
    </section>

    <!-- 2. Promo Buckets Section -->
    <section class="subpage-promo-section section-reset">
      <div class="centered-red-header" style="margin-bottom: 1.5rem; text-align: left; padding: 0.75rem 1.25rem;">
        <span>Special Promo Buckets & Exclusive Deals</span>
      </div>
      <div class="promo-banners-grid">
        {promo_buckets_html}
      </div>
    </section>

    <!-- 3. Featured Products Grid Section -->
    <section class="shop-all-section section-reset" style="margin-top: 2rem !important;">
      <div class="shop-by-category-header" style="background-color: #ed017f; border-radius: 12px 12px 0 0;">
        <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
          <span>{cat['heading']} Deals</span>
          <a href="https://www.konga.com/search?search={key.replace('-', '+')}" target="_blank" class="flash-more" style="color: #ffffff; font-size: 14px; text-decoration: none; display: flex; align-items: center; gap: 8px;">
            View All On Konga
            <span class="icon-circle" style="background-color: #ffffff; border-radius: 50%; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center;">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 18L15 12L9 6" stroke="#ed017f" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </a>
        </div>
      </div>
      <div class="shop-all-container">
        <div class="shop-all-grid">{products_html}
        </div>
      </div>
    </section>

    <!-- 4. Written SEO Footer Section -->
    <section class="written-seo" style="margin-top: 3.5rem !important;">
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
