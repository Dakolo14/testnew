import json
import os

with open('category_data.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# Subcategories configuration with circular images matching Konga subcategory layout
PAGE_CONFIG = {
    "samsung-phones": {
        "title": "Samsung Phones",
        "subcategories": [
            {"name": "Galaxy S24 Ultra", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+s24+ultra"},
            {"name": "Galaxy S24 Series", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+s24"},
            {"name": "Galaxy Z Fold & Flip", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+z+fold"},
            {"name": "Galaxy A55 & A35", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+a55"},
            {"name": "Galaxy A15 & A05s", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+a15"},
            {"name": "Galaxy Watches", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+watch"},
            {"name": "Galaxy Buds", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+galaxy+buds"},
            {"name": "Fast Chargers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/B/M/186576_1785291116.jpg", "query": "samsung+45w+charger"}
        ]
    },
    "iphones": {
        "title": "iPhones & Apple",
        "subcategories": [
            {"name": "iPhone 16 Pro Max", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "iphone+16+pro+max"},
            {"name": "iPhone 16 & 16 Pro", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "iphone+16"},
            {"name": "iPhone 15 Series", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "iphone+15"},
            {"name": "iPhone 14 Series", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "iphone+14"},
            {"name": "iPhone 13", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "iphone+13"},
            {"name": "Apple Watch Ultra", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "apple+watch"},
            {"name": "AirPods & Max", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "airpods+pro"},
            {"name": "MagSafe & Adapters", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/T/T/161515_1790884755.jpg", "query": "apple+20w+charger"}
        ]
    },
    "xiaomi-phones": {
        "title": "Xiaomi Phones",
        "subcategories": [
            {"name": "Redmi Note 13 Pro+", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "redmi+note+13+pro"},
            {"name": "Redmi Note 13", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "redmi+note+13"},
            {"name": "POCO X6 Pro", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/D/Y/118566_1768920113.jpg", "query": "poco+x6+pro"},
            {"name": "Redmi 13C", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "redmi+13c"},
            {"name": "Redmi 14C", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "redmi+14c"},
            {"name": "Redmi A3", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "redmi+a3"},
            {"name": "Xiaomi Powerbanks", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "xiaomi+power+bank"},
            {"name": "Fast Chargers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/M/118566_1784697360.jpg", "query": "xiaomi+charger"}
        ]
    },
    "other-phones": {
        "title": "Other Phones",
        "subcategories": [
            {"name": "Tecno Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "tecno+phones"},
            {"name": "itel Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "itel+phones"},
            {"name": "Google Pixel", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "google+pixel"},
            {"name": "Vivo Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "vivo+phones"},
            {"name": "Oppo Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "oppo+phones"},
            {"name": "Realme Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "realme+phones"},
            {"name": "Nokia Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "nokia+phones"},
            {"name": "Feature Phones", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/A/118566_1789549980.jpg", "query": "button+phones"}
        ]
    },
    "laptops": {
        "title": "Laptops & Computing",
        "subcategories": [
            {"name": "HP Laptops", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/H/_1784902533.png", "query": "hp+laptop"},
            {"name": "ASUS Laptops", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/Y/56319_1786712399.jpg", "query": "asus+laptop"},
            {"name": "Apple MacBooks", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/H/163129_1770105285.jpg", "query": "macbook"},
            {"name": "Lenovo Laptops", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/H/_1784902533.png", "query": "lenovo+laptop"},
            {"name": "Dell Inspiron", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/F/Z/149469_1782466044.jpg", "query": "dell+laptop"},
            {"name": "Gaming Laptops", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/H/Y/56319_1786712399.jpg", "query": "gaming+laptop"},
            {"name": "Zinox Laptops", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/H/_1784902533.png", "query": "zinox+laptop"},
            {"name": "Laptop Bags & Stands", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/H/_1784902533.png", "query": "laptop+bag"}
        ]
    },
    "consoles": {
        "title": "Consoles & Gaming",
        "subcategories": [
            {"name": "PlayStation 5 Slim", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Z/W/240947_1783276152.jpg", "query": "ps5+slim"},
            {"name": "PS5 Digital", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Z/W/240947_1783276152.jpg", "query": "ps5+digital"},
            {"name": "Xbox Series X", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg", "query": "xbox+series+x"},
            {"name": "Xbox Series S", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg", "query": "xbox+series+s"},
            {"name": "Nintendo Switch OLED", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg", "query": "nintendo+switch"},
            {"name": "DualSense Controllers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg", "query": "dualsense+controller"},
            {"name": "EA Sports FC 25", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Y/B/63606_1770638150.jpg", "query": "ea+fc+25"},
            {"name": "Pulse 3D Headsets", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/M/R/122138_1725373498.jpg", "query": "ps5+headset"}
        ]
    },
    "washers": {
        "title": "Washers & Dryers",
        "subcategories": [
            {"name": "Front Load Washers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "front+load+washing+machine"},
            {"name": "Top Load Washers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "top+load+washing+machine"},
            {"name": "Twin Tub Washers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/I/140630_1725641773.jpg", "query": "twin+tub+washing+machine"},
            {"name": "Washer & Dryer Combo", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "washer+dryer"},
            {"name": "LG AI DD", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "lg+ai+dd"},
            {"name": "Samsung EcoBubble", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "samsung+ecobubble"},
            {"name": "Haier Thermocool", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/R/I/140630_1725641773.jpg", "query": "haier+thermocool+washer"},
            {"name": "Protective Covers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/A/O/231472_1777545584.jpg", "query": "washing+machine+cover"}
        ]
    },
    "acs": {
        "title": "Air Conditioners",
        "subcategories": [
            {"name": "1.0 HP Split ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "1hp+split+ac"},
            {"name": "1.5 HP Split ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "1.5hp+split+ac"},
            {"name": "2.0 HP Split ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/P/W/118566_1788273396.jpg", "query": "2hp+split+ac"},
            {"name": "Inverter ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "inverter+split+ac"},
            {"name": "Floor Standing ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "floor+standing+ac"},
            {"name": "LG Dual Inverter", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "lg+dual+inverter+ac"},
            {"name": "Hisense Copper ACs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/P/W/118566_1788273396.jpg", "query": "hisense+ac"},
            {"name": "AC Pipe & Kits", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/Q/B/229301_1743619260.jpg", "query": "ac+installation+kit"}
        ]
    },
    "fridges": {
        "title": "Fridges & Freezers",
        "subcategories": [
            {"name": "Double Door Fridges", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/G/229301_1750257650.jpg", "query": "double+door+refrigerator"},
            {"name": "Deep Chest Freezers", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/X/W/118566_1544086101.jpg", "query": "chest+freezer"},
            {"name": "French Door & Multi", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/K/H/118566_1747148808.png", "query": "french+door+refrigerator"},
            {"name": "Single Door & Bedside", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/G/229301_1750257650.jpg", "query": "single+door+refrigerator"},
            {"name": "Bottom Freezer Units", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/G/229301_1750257650.jpg", "query": "bottom+freezer+refrigerator"},
            {"name": "Samsung Fridges", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/K/H/118566_1747148808.png", "query": "samsung+refrigerator"},
            {"name": "Haier Thermocool", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/X/W/118566_1544086101.jpg", "query": "haier+thermocool+freezer"},
            {"name": "Surge Protectors", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/G/229301_1750257650.jpg", "query": "fridge+surge+guard"}
        ]
    },
    "sexual-wellness": {
        "title": "Sexual Wellness",
        "subcategories": [
            {"name": "Durex Condoms", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "durex+condoms"},
            {"name": "Pleasure Lubricants", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "lubricant+gel"},
            {"name": "Massage & 2-in-1 Gels", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "massage+gel"},
            {"name": "Fiesta Condoms", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "fiesta+condoms"},
            {"name": "Gold Circle Value", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "gold+circle+condoms"},
            {"name": "KY Jelly", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "ky+jelly"},
            {"name": "Endurance & Delay", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "mutual+climax+condoms"},
            {"name": "Multipack Bundles", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_240,c_limit/media/customcmsmenu/item/2ndcatsexualawareness.png", "query": "condom+multipack"}
        ]
    },
    "wigs": {
        "title": "Wigs & Human Hair",
        "subcategories": [
            {"name": "Bone Straight Wigs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "bone+straight+wig"},
            {"name": "Deep Wave & Curls", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "deep+wave+wig"},
            {"name": "Glueless Bob Wigs", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "glueless+bob+wig"},
            {"name": "HD Lace Frontals", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "hd+lace+frontal"},
            {"name": "Human Hair Bundles", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "human+hair+bundles"},
            {"name": "Piano & Highlight", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "highlight+wig"},
            {"name": "Lace Glue & Tint", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "lace+tint+glue"},
            {"name": "Hot Combs & Wax", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/V/N/240104_1742889486.jpg", "query": "hot+comb+hair"}
        ]
    },
    "makeup": {
        "title": "Makeup & Cosmetics",
        "subcategories": [
            {"name": "Matte Foundations", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "matte+foundation"},
            {"name": "Fit Me by Maybelline", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "maybelline+fit+me"},
            {"name": "Setting Powders", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "setting+powder"},
            {"name": "Setting Sprays", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "setting+spray"},
            {"name": "Eyeshadow Palettes", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "eyeshadow+palette"},
            {"name": "Lipsticks & Glosses", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "lipstick+gloss"},
            {"name": "18pc Makeup Brushes", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "makeup+brush+set"},
            {"name": "Fenty Beauty", "img": "https://www-konga-com-res.cloudinary.com/image/upload/f_auto,q_auto,w_400,c_limit/media/catalog/product/G/Z/98247_1546250142.jpg", "query": "fenty+beauty"}
        ]
    }
}

def generate_subcat_circles_html(subcats):
    items_html = ""
    for s in subcats:
        items_html += f"""
          <a href="https://www.konga.com/search?search={s['query']}" target="_blank" class="subcat-circle-item">
            <div class="subcat-circle-img-wrap">
              <img src="{s['img']}" alt="{s['name']}" loading="lazy">
            </div>
            <span class="subcat-circle-label">{s['name']}</span>
          </a>"""
    return items_html

def generate_html(key, cat):
    cfg = PAGE_CONFIG.get(key, {
        "title": cat['heading'],
        "subcategories": []
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

    subcat_circles_html = generate_subcat_circles_html(cfg['subcategories'])

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
      /* Clean Dark Subpage Styling (No large hero banner) */
      body {{
        background-color: #0b0b0f;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
      }}

      /* Navbar Logo Sizing - matching exact Konga Yakata proportions */
      .navbar-logo {{
        height: 38px !important;
        display: flex;
        align-items: center;
      }}
      .navbar-logo a {{
        display: inline-flex;
        align-items: center;
        height: 100%;
      }}
      .navbar-logo img {{
        height: 38px !important;
        max-height: 38px !important;
        width: auto !important;
        object-fit: contain !important;
        display: block;
      }}

      /* Clean Header & Breadcrumbs (Like Konga Subcategory Page) */
      .cat-simple-header {{
        width: 100%;
        max-width: 1400px;
        margin: 1.25rem auto 0.75rem auto;
        padding: 0 1rem;
      }}
      .cat-simple-breadcrumb {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        font-weight: 300;
        color: #9ca3af;
        margin-bottom: 0.5rem;
      }}
      .cat-simple-breadcrumb a {{
        color: #d1d5db;
        text-decoration: none;
        font-weight: 300;
        transition: color 0.2s;
      }}
      .cat-simple-breadcrumb a:hover {{
        color: #ed017f;
      }}
      .cat-simple-breadcrumb .crumb-active {{
        color: #ed017f;
        font-weight: 400;
      }}
      .cat-simple-title {{
        font-family: 'Poppins', sans-serif;
        font-size: 26px;
        font-weight: 500;
        color: #ffffff;
        margin: 0;
        line-height: 1.25;
      }}

      /* Subcategory Circle Grid Section (Dark Version of Konga Circular Layout) */
      .subcat-circles-section {{
        width: 100%;
        max-width: 1400px;
        margin: 1rem auto 2.5rem auto;
        padding: 0 1rem;
      }}
      .subcat-circles-container {{
        background: #14141a;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.75rem 1.25rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      }}
      .subcat-circles-grid {{
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        gap: 16px;
      }}
      .subcat-circle-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
        color: #ffffff;
        transition: transform 0.25s ease;
      }}
      .subcat-circle-item:hover {{
        transform: translateY(-5px);
      }}
      .subcat-circle-img-wrap {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 4px 14px rgba(0,0,0,0.4);
        padding: 14px;
        box-sizing: border-box;
        transition: border-color 0.25s ease, box-shadow 0.25s ease;
      }}
      .subcat-circle-item:hover .subcat-circle-img-wrap {{
        border-color: #ed017f;
        box-shadow: 0 6px 20px rgba(237, 1, 127, 0.35);
      }}
      .subcat-circle-img-wrap img {{
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
        filter: blur(8px);
        opacity: 0.65;
        transform: scale(1.15);
        transition: filter 0.3s ease, opacity 0.3s ease, transform 0.3s ease;
      }}
      .subcat-circle-item:hover .subcat-circle-img-wrap img {{
        filter: blur(4px);
        opacity: 0.85;
        transform: scale(1.2);
      }}
      .subcat-circle-label {{
        margin-top: 10px;
        font-size: 12px;
        font-weight: 300;
        text-align: center;
        color: #d1d5db;
        line-height: 1.3;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        min-height: 32px;
        transition: color 0.2s ease;
      }}
      .subcat-circle-item:hover .subcat-circle-label {{
        color: #ed017f;
      }}

      /* Responsive rules for circle subcategories */
      @media (max-width: 1200px) {{
        .subcat-circles-grid {{
          grid-template-columns: repeat(4, 1fr);
          gap: 16px 12px;
        }}
        .subcat-circle-img-wrap {{
          width: 95px;
          height: 95px;
        }}
      }}
      @media (max-width: 640px) {{
        .subcat-circles-grid {{
          grid-template-columns: repeat(4, 1fr);
          gap: 12px 8px;
        }}
        .subcat-circles-container {{
          padding: 1.25rem 0.75rem;
        }}
        .subcat-circle-img-wrap {{
          width: 72px;
          height: 72px;
          padding: 8px;
        }}
        .subcat-circle-label {{
          font-size: 11px;
          margin-top: 6px;
        }}
        .cat-simple-title {{
          font-size: 20px;
        }}
      }}
    </style>
  </head>
  <body>
    <!-- Main Top Navigation (Identical layout to index.html with fixed logo size) -->
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

    <!-- Clean Header & Breadcrumbs (No banner) -->
    <div class="cat-simple-header">
      <div class="cat-simple-breadcrumb">
        <a href="index.html">Home</a>
        <span>&rsaquo;</span>
        <span class="crumb-active">{cat['heading']}</span>
      </div>
      <h1 class="cat-simple-title">{cat['heading']}</h1>
    </div>

    <!-- Circular Subcategories Section (Dark version of Konga subcategory pills) -->
    <section class="subcat-circles-section section-reset">
      <div class="subcat-circles-container">
        <div class="subcat-circles-grid">
          {subcat_circles_html}
        </div>
      </div>
    </section>

    <!-- Product Grid Section (Trending in Category) -->
    <section class="shop-all-section section-reset" style="margin-top: 1rem !important;">
      <div class="shop-by-category-header" style="background-color: #ed017f; border-radius: 12px 12px 0 0; padding: 0.85rem 1.25rem;">
        <span style="font-weight: 400; font-size: 0.95rem; letter-spacing: 0.5px;">Trending in {cat['heading']}</span>
      </div>
      <div class="shop-all-container">
        <div class="shop-all-grid">{products_html}
        </div>
      </div>
    </section>

    <!-- Written SEO Footer Section -->
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
