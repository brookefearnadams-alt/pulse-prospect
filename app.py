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

# Top Header Layout (Stacked for better screen space)
st.markdown("<p class='main-title'>📡 OMNIPULSE AI</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>The Official Media Sales Intelligence Platform — Powered by Enterprise Data & Elvex Flows</p>", unsafe_allow_html=True)

# Sidebar System Navigation
st.sidebar.markdown("### 🖥️ Platform Controls")
st.sidebar.success("● Core Engine: Connected")
st.sidebar.success("● Knowledge Base: Active")
st.sidebar.info("● Database Year: 2026")
st.sidebar.markdown("---")
st.sidebar.markdown("**Demo Input Mapping:**")
st.sidebar.write("- Type **'ecorest'** for the premium bedding analysis.")
st.sidebar.write("- Type **'cityfurniture'** or any other URL for the retail scenario.")

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

# Database Configuration
mock_database = {
    "ecorest": {
        "prospect_name": "EcoRest Bedding",
        "vertical": "DTC Home Goods / Premium Mattress",
        "estimated_digital_monthly": "\$45,000 - \$60,000",
        "meta_ad_count": "34 Active Creative Variations",
        "google_ad_types": "Performance Max (Heavy Search & Shopping focus)",
        "pixel_detections": "Meta Pixel (Custom Conversions), Google Tag Manager, TikTok Pixel",
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
    },
    "default": {
        "prospect_name": "City Furniture",
        "vertical": "Home Furnishings / Regional Retailer",
        "estimated_digital_monthly": "\$85,000 - \$120,000",
        "meta_ad_count": "52 Active Ad Variations",
        "google_ad_types": "Local Inventory Ads, Performance Max, Youtube Pre-Roll",
        "pixel_detections": "Meta Pixel, Google Floodlight, Pinterest Tag, Criteo Retargeting",
        "creative_gap": "Heavy dependence on promotional sales banners and price-cut imagery. Significant lack of upper-funnel storytelling that emphasizes design consulting or financing ease.",
        "competitive_threat": "National chains (Rooms To Go, Ashley Furniture) are saturating regional zip codes with automated programmatic bids, forcing local direct players into high-cost bidding environments.",
        "vulnerability": "Current digital tactics are trapped in an aggressive programmatic retargeting loop. This causes audience fatigue and drops online return-on-ad-spend (ROAS) during non-holiday periods.",
        "vbr_statement": "Localized market data indicates that backing regional retail digital campaigns with consistent Early Fringe and Access Linear TV blocks increases direct digital conversions by 21% while bypassing localized digital auction bidding peaks.",
        "recommended_mix": "50% Early Fringe & Access Linear | 30% Connected TV Geotargets | 20% Premium Desktop Sponsorships",
        "email_subject": "Bypassing local digital ad inflation for City Furniture",
        "email_body": "Hi Team City Furniture,\n\nI’ve been studying your regional digital ad footprints. Your current mix of Local Inventory Ads and active Meta sets effectively targets immediate shoppers, but it exposes your budget to heavy holiday auction inflation from national furniture conglomerates.\n\nOur cross-platform performance tracking reveals that integrating Early Fringe and Access linear windows builds an immediate market baseline that improves digital conversion efficiency by 21%.\n\nThis multi-platform layer offsets audience fatigue and locks in market share before competitors can outbid you online.\n\nI have a 3-slide strategic blueprint ready for City Furniture outlining this lift. Do you have 10 minutes for a brief call this week?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": ["Auction Pressures: Facing continuous digital auction bidding inflation driven by national franchise spend.", "Audience Fatigue: High ad frequency with static promotional banners reduces overall click-through rates.", "Placement Crutch: Retargeting bottom-funnel shoppers while losing mid-funnel consideration."],
        "slide_2_bullets": ["The Reach Engine: Early Fringe and Access linear captures the localized household decision-makers.", "Conversion Lift: Proven 21% increase in web direct conversions when broadcast pairs with digital campaigns.", "Auction Protection: Broad market authority lowers reliance on expensive competitive search bidding terms."],
        "slide_3_bullets": ["The Blueprint: A balanced mix of 50% high-index local linear combined with precision CTV geotargets.", "Attribution Tracking: Deploying immediate post-air lift models to measure real-time website traffic spikes.", "Action Item: 10-minute multi-screen alignment strategy brief."]
    }
}

# Output Logic Block
if submit_button:
    with st.spinner("Processing digital footprint..."):
        time.sleep(1.0)
        
    clean_url = prospect_url.lower()
    if "ecorest" in clean_url or "bedding" in clean_url:
        data = mock_database["ecorest"]
    else:
        data = mock_database["default"]
        
    st.markdown("---")
    st.success(f"⚡ STRATEGIC PROFILE COMPILED FOR: {data['prospect_name'].upper()}")
    
    # Text Meta Block
    st.write(f"**Target Client:** {data['prospect_name']}  |  **Industry Vertical:** {data['vertical']}  |  **Data Grounding:** 98% Confidence")
    
    # 1. Scraped Signals Block (Full Width Panel)
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🕵️‍♂️ Scraped Digital Signals & Competitive Intelligence")
    # 1. Scraped Signals Block (Full Width Panel)
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🕵️‍♂️ Scraped Digital Signals & Competitive Intelligence")
    st.write(f"• **Est. Monthly Digital Spend:** {data['estimated_digital_monthly']}")
    st.write(f"• **Active Ad Footprint:** {data['meta_ad_count']}")
    st.write(f"• **Google Channels:** {data['google_ad_types']}")
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
    
    # 4. Presentation Slides Content (Stacked Vertically for Perfect Scannability)
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
