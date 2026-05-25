import streamlit as st
import time

# Page configuration
st.set_page_config(layout="wide", page_title="OmniPulse AI", page_icon="📡")

# Custom Styles for High Scannability
st.markdown("""
    <style>
    .main-title { font-size: 36px !important; font-weight: 800; color: #1E3A8A; margin: 0; }
    .subtitle { font-size: 15px !important; color: #4B5563; margin-bottom: 20px; font-style: italic; }
    .section-box { background-color: #F9FAFB; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 20px; }
    .slide-red { background-color: #FEE2E2; padding: 15px; border-radius: 6px; border-left: 5px solid #EF4444; margin-bottom: 15px; }
    .slide-green { background-color: #D1FAE5; padding: 15px; border-radius: 6px; border-left: 5px solid #10B981; margin-bottom: 15px; }
    .slide-blue { background-color: #DBEAFE; padding: 15px; border-radius: 6px; border-left: 5px solid #3B82F6; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Top Header Layout
st.markdown("<p class='main-title'>📡 OMNIPULSE AI</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>The Official Media Sales Intelligence Platform — Powered by Enterprise Data & Elvex Flows</p>", unsafe_allow_html=True)

# Sidebar System Navigation
st.sidebar.markdown("### 🖥️ Platform Controls")
st.sidebar.success("● Core Engine: Connected")
st.sidebar.success("● Knowledge Base: Active")
st.sidebar.info("● Database Year: 2026")
st.sidebar.markdown("---")
st.sidebar.markdown("**Demo Input Mapping:**")
st.sidebar.write("This app will automatically detect 'cityfurniture' or 'ecorest' in your URL and pull custom deep intelligence.")

# Performance Tickers
t1, t2, t3, t4 = st.columns(4)
t1.metric(label="Average CPA Lift", value="-24%")
t2.metric(label="Direct Revenue Capture", value="+31%")
t3.metric(label="Agency RFPs Bypassed", value="142")
t4.metric(label="Pitch Build Time", value="12 Sec")

st.markdown("###")

# User Input Panel
st.markdown("### 🔍 Deep Web Scrape & Local Media Diagnostic")
prospect_url = st.text_input(
    "Input Target Prospect Website URL:", 
    value="https://www.cityfurniture.com/"
)
submit_button = st.button("Generate Deep Intelligence Briefing", type="primary")

# Heavy-Hitting Media Database
mock_database = {
    "cityfurniture": {
        "prospect_name": "City Furniture",
        "vertical": "Home Furnishings / Regional Retailer",
        "estimated_digital_monthly": "\$145,000 - \$180,000 (Local/Regional Spender)",
        "meta_ad_count": "84 Active Creative Variations",
        "google_ad_types": "Google Performance Max (PMax), Local Inventory Ads, YouTube Pre-Roll",
        "pixel_detections": "Meta Pixel (Advanced Conversions), Google Floodlight, Pinterest Tag, Criteo Retargeting Engine",
        "creative_gap": "92% of active ads rely on price-cut imagery (e.g., 'Save \$500') and holiday promo banners. Severe deficit in premium lifestyle video storytelling, design consulting spotlights, and family/home emotional triggers.",
        "competitive_threat": "National giants (Rooms To Go and Ashley Furniture) have increased local programmatic search bids by 54% this quarter, deliberately outbidding City Furniture on localized long-tail search phrases like 'modern sectional near me'.",
        "vulnerability": "Extreme exposure to digital auction manipulation during peak sales windows. Digital-only retargeting is trapping them in a conversion bottleneck where their Cost Per Acquisition (CPA) is up 41% YoY, killing non-holiday margins.",
        "vbr_statement": "Secure regional campaign tracking confirms that regional furniture retailers anchoring digital spend with high-frequency Early Fringe, Access, and Early News Linear TV see an immediate 21% surge in direct web conversions and an 18% lift in showroom foot traffic, while insulating their digital budgets from national auction bidding spikes.",
        "recommended_mix": "50% High-Index Local Linear (News/Access) | 30% Connected TV (CTV) Zip-Code Targets | 20% Premium Desktop Sponsorships",
        "email_subject": "Bypassing national ad auction inflation for City Furniture",
        "email_body": "Hi Team City Furniture,\n\nI’ve been studying your regional digital ad footprints. Our intelligence engine flagged that you currently have 84 active ad variations running across Meta alongside a heavy Google PMax setup.\n\nWhile your product retargeting is highly efficient, a digital-only approach leaves you vulnerable. National conglomerates (Rooms To Go/Ashley) have flooded local zip codes with a 54% increase in programmatic bids, driving your digital customer acquisition costs up 41% YoY.\n\nOur cross-platform data shows that regional retailers anchoring their digital spend with strategic Early Fringe and Access television blocks build a local 'market shield.' This multi-screen baseline increases direct web conversions by 21% and completely bypasses expensive digital bidding wars.\n\nI’ve mapped out a 3-slide strategic blueprint showing how this unified lift will protect City Furniture’s margins this quarter. Do you have 10 minutes this Thursday at 2 PM for a brief look at the data?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": [
            "Auction Pressures: National brands have inflated local digital bidding costs by 54% this quarter.",
            "Margin Erosion: City Furniture's digital acquisition costs (CPA) have spiked 41% YoY due to ad auction wars.",
            "Creative Fatigue: Over-reliance on transactional price-cut banners ignores upper-funnel emotional storytelling."
        ],
        "slide_2_bullets": [
            "The Screen Blanket: Early Fringe, Access, and Local News lock down the local household decision-makers.",
            "The Halo Conversion: Unified cross-screen flights trigger an immediate 21% surge in high-intent organic web searches.",
            "Showroom Lift: Broadcast presence acts as an offline anchor, driving a proven 18% lift in physical store traffic."
        ],
        "slide_3_bullets": [
            "The Guardrail Mix: Transitioning to 50% premium local linear, 30% hyper-targeted CTV, and 20% digital sponsorships.",
            "Unified Tracking: Measuring success through real-time web traffic correlation during broadcast windows.",
            "Next Steps: 10-minute strategy alignment to deploy localized market test zones."
        ]
    },
    "ecorest": {
        "prospect_name": "EcoRest Bedding",
        "vertical": "DTC Home Goods / Premium Mattress",
        "estimated_digital_monthly": "\$45,000 - \$60,000",
        "meta_ad_count": "34 Active Creative Variations",
        "google_ad_types": "Performance Max (Heavy Search & Shopping focus)",
        "pixel_detections": "Meta Pixel, Google Tag Manager, TikTok Pixel, Klaviyo Tracking",
        "creative_gap": "Over-indexing on text-heavy testimonial static ads. Complete absence of high-production video storytelling or lifestyle video formats to build brand equity.",
        "competitive_threat": "Casper and Purple Mattresses are currently running localized geotargeted digital conquests in this market, outbidding EcoRest for the keyword 'organic latex mattress' by 42%.",
        "vulnerability": "Heavy reliance on Meta and Google Ads is causing a 38% YoY inflation in their Digital Customer Acquisition Costs (CAC), severely squeezing net margins on their organic latex mattress line.",
        "vbr_statement": "Internal campaign data proves that local DTC brands anchoring active digital campaigns with a high-impact Linear TV daytime flight experience an average 24% reduction in overall Digital CAC via a 15% surge in high-intent organic brand searches.",
        "recommended_mix": "60% Daytime Linear (Homeowner index) | 20% Connected TV (CTV) Retargeting | 20% Localized Digital News Takeovers",
        "email_subject": "Optimizing EcoRest's digital acquisition efficiency by 24%",
        "email_body": "Hi Team EcoRest,\n\nI’ve been tracking your impressive digital presence for your organic latex mattress line. Our intelligence engine flagged that you are currently managing 34 active creative variations on Meta, heavily leaning into Performance Max channels.\n\nWhile this captures baseline demand, running a digital-only acquisition strategy right now means you are highly exposed. Competitors like Casper are currently outbidding you by 42% locally on key search phrases, driving up your digital CAC by 38% YoY.\n\nOur cross-platform data shows that local brands pairing active digital with strategic daytime Linear TV see an average 24% drop in digital CAC. This builds a protective 'brand shield' around your search keywords.\n\nI’ve put together a 3-slide efficiency blueprint tailored to your active pixel profiles. Do you have 10 minutes this Thursday at 2 PM to review our data?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": ["Digital Inflation: EcoRest is absorbing a 38% YoY increase in Meta/Google acquisition costs.", "Keyword Conquesting: Competitors are outbidding EcoRest by 42% on high-intent local search phrases.", "Creative Bottleneck: 34 active Meta ads rely entirely on static testimonials, ignoring screen-based video storytelling."],
        "slide_2_bullets": ["The Halo Effect: Daytime broadcast presence drives immediate mobile/desktop organic brand searches.", "CAC Reduction: Proven 24% decrease in digital acquisition costs by stabilizing competitive auction dependency.", "Audience Capture: Reaching premium 35-64 homeowners who own 80% of local premium home assets."],
        "slide_3_bullets": ["Efficiency Mix: Deploying a 60% Daytime Linear flight paired with high-impact CTV retargeting.", "Pixel Sync: Utilizing existing Meta pixels to retarget consumers exposed to our local broadcast windows.", "Next Steps: Reviewing customized local zone maps on Thursday."]
    }
}

# Smart Input Matching Logic
if submit_button:
    with st.spinner("Processing digital footprint..."):
            time.sleep(1.0)
    
    # Clean up the input string to match keywords anywhere in the typed text
    clean_url = prospect_url.lower()
    
    if "city" in clean_url or "furniture" in clean_url:
        data = mock_database["cityfurniture"]
    elif "ecorest" in clean_url or "bedding" in clean_url:
        data = mock_database["ecorest"]
    else:
        # If they type something else, default to City Furniture to ensure it looks amazing for the live pitch
        data = mock_database["cityfurniture"]
        
    st.markdown("---")
    st.success(f"⚡ STRATEGIC PROFILE COMPILED FOR: {data['prospect_name'].upper()}")
    
    # Text Meta Block
    st.write(f"**Target Client:** {data['prospect_name']}  |  **Industry Vertical:** {data['vertical']}  |  **Data Grounding Source:** Elvex Media Index")
    
    # 1. Scraped Signals Block (Full Width Panel)
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🕵️‍♂️ Scraped Digital Signals & Competitive Intelligence")
    st.write(f"• **Est. Monthly Digital Spend:** {data['estimated_digital_monthly']}")
    st.write(f"• **Active Ad Footprint:** {data['meta_ad_count']}")
    st.write(f"• **Google Channels Found:** {data['google_ad_types']}")
    st.write(f"• **Active Tracking Pixels Detected:** {data['pixel_detections']}")
    st.write(f"• ⚠️ **Competitive Threat:** {data['competitive_threat']}")
    st.write(f"• 💡 **Creative Optimization Gap:** {data['creative_gap']}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 2. Strategy & Pitch Text Blocks
    st.markdown("### 🎯 Data-Backed Pitch Strategy")
    st.info(f"**The Valid Business Reason (VBR):**\n\n{data['vbr_statement']}")
    st.error(f"**Identified Digital Vulnerability:**\n\n{data['vulnerability']}")
    
    # 3. Outreach Copy Block
    st.markdown("### 📨 Automated Executive Outreach Script")
    st.text_input("Recommended Subject Line:", data['email_subject'])
    st.text_area("Generated Consultative Copy (Ready to Copy/Paste):", data['email_body'], height=250)
    
    # 4. Presentation Slides Content
    st.markdown("---")
    st.markdown("### 📊 Automated Multi-Tactical Pitch Presentation Content")
    st.write(f"**Recommended Cross-Platform Allocation:** {data['recommended_mix']}")
    st.caption("Copy these blocks directly into your PowerPoint deck to pitch a direct, non-agency account:")
    
    # Slide 1
    st.markdown("<div class='slide-red'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 1: The Digital Bottleneck (Why Only Using Digital Fails)**")
    for bullet in data['slide_1_bullets']:
        st.markdown(f"❌ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 2
    st.markdown("<div class='slide-green'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 2: The Multiplier Effect (Why Broadcast + Digital Wins)**")
    for bullet in data['slide_2_bullets']:
        st.markdown(f"📈 {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 3
    st.markdown("<div class='slide-blue'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 3: The Multi-Platform Blueprint (The Tactical Mix)**")
    for bullet in data['slide_3_bullets']:
        st.markdown(f"🛠️ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)

