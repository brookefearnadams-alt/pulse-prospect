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
st.sidebar.write("• Type **'cityfurniture'** for regional furniture retail metrics.")
st.sidebar.write("• Type **'ecorest'** for the premium bedding analysis.")

# Session State Initialization for Form Reset Button
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Performance Tickers
t1, t2, t3, t4 = st.columns(4)
t1.metric(label="Average CPA Efficiency Lift", value="-24%")
t2.metric(label="Direct Revenue Capture", value="+31%")
t3.metric(label="Agency RFPs Bypassed", value="142")
t4.metric(label="Briefing Build Time", value="12 Sec")

st.markdown("###")

# User Input Panel
st.markdown("### 🔍 Enterprise Cost-Center & Margin Diagnostic")

# Dynamic value tracking for reset functionality
if "url_input" not in st.session_state:
    st.session_state.url_input = "https://www.cityfurniture.com/"

prospect_url = st.text_input(
    "Input Target Prospect Website URL:", 
    value=st.session_state.url_input,
    key="url_box"
)

# Button Layout alignment
btn_col1, btn_col2, _ = st.columns([2, 1, 5])
with btn_col1:
    if st.button("Generate Strategic Financial Briefing", type="primary"):
        st.session_state.submitted = True
with btn_col2:
    if st.button("Reset Form"):
        st.session_state.submitted = False
        st.session_state.url_input = ""
        st.rerun()

# Business-First Strategy Database
mock_database = {
    "cityfurniture": {
        "prospect_name": "City Furniture",
        "vertical": "Home Furnishings / Regional Retailer",
        "estimated_digital_monthly": "\$145,000 - \$180,000 (Local/Regional Capital Allocation)",
        "meta_ad_count": "84 Active Creative Variations",
        "google_ad_types": "Google Performance Max (PMax), Local Inventory Ads, YouTube Pre-Roll",
        "pixel_detections": "Meta Pixel (Advanced Conversions), Google Floodlight, Pinterest Tag, Criteo Retargeting Engine",
        "creative_gap": "92% of marketing assets are tied directly to margin-diluting discount codes and price-cut promotional inventory. Significant deficit in equity-building assets that protect long-term gross product margins.",
        "competitive_threat": "National scale conglomerates have increased regional ad auction spending by 54% this quarter, artificially driving up customer acquisition inflation and squeezing regional retail operating income.",
        "vulnerability": "Severe customer acquisition cost (CAC) inflation. Relying exclusively on immediate digital feedback loops has trapped customer acquisition within a highly competitive auction model, leading to a 41% YoY increase in conversion costs.",
        "vbr_statement": "Regional tracking confirms that mid-market operations that insulate their digital customer acquisition pipelines with a broad-market authority baseline achieve an average 21% reduction in overall digital CAC. This structural pivot stabilizes margins by reducing direct dependency on hyper-inflated, auction-based bidding platforms.",
        "recommended_mix": "50% Market Authority Baselines (Mass Media) | 30% Mid-Funnel Localized Geotargeting | 20% Premium Digital Integration",
        "email_subject": "Stabilizing City Furniture's customer acquisition costs and protecting product margins",
        "email_body": "Hi Team City Furniture,\n\nI’ve been reviewing City Furniture’s regional customer acquisition footprint. Our enterprise analytics dashboard flags that your current digital pipeline is heavily leveraged within automated ad auctions, managing roughly 84 active creative variations across standard channels.\n\nWhile this model efficiently captures low-hanging demand, it introduces a severe financial vulnerability: national competitors have increased local auction bids by 54% this quarter, driving your customer acquisition costs (CAC) up an estimated 41% YoY and putting pressure on net operating margins.\n\nOur cross-platform financial data demonstrates that regional retailers who anchor their digital acquisition engines with a broad-market authority baseline reduce overall digital CAC by 21%. This approach shifts your budget away from volatile, reactive bidding environments and locks in a predictable market share baseline.\n\nI have put together a 3-slide operational blueprint detailing how this mix adjustment will stabilize your acquisition costs this quarter. Do you have 10 minutes this Thursday at 2 PM for a brief, business-level look at the numbers?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": [
            "The Capital Inefficiency: Over-allocating budget to digital ad auctions has exposed City Furniture to a 41% YoY increase in customer acquisition costs (CAC).",
            "Auction Vulnerability: National corporate spenders have inflated regional search engine bidding costs by 54%, eating into product net margins.",
            "Margin Dilution: Heavy reliance on price-cut digital creative signals to consumers that the brand relies on continuous discounting rather than intrinsic value."
        ],
        "slide_2_bullets": [
            "The Market Shield: Re-establishing broad-market brand equity builds a proprietary consumer consideration pipeline outside of ad platforms.",
            "The Portfolio Effect: Transitioning away from pure-play digital bidding yields a proven 21% reduction in total blended acquisition costs.",
            "Showroom Asset Optimization: Broad geographic presence drives an 18% lift in showroom asset utilization and floor traffic."
        ],
        "slide_3_bullets": [
            "The Allocation Reset: Diversifying capital allocations into a structured mix of 50% broad-market authority, 30% targeted streaming, and 20% premium digital integrations.",
            "Attribution Alignment: Measuring success via enterprise web baseline traffic lifts and total blended marketing efficiency ratios (MER) rather than isolated click-through tracking.",
            "Strategic Next Step: A 10-minute executive alignment meeting to review local market cost-insulation test zones."
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
        "slide_1_bullets": [
            "Digital Inflation: EcoRest is absorbing a 38% YoY increase in Meta/Google acquisition costs.",
            "Keyword Conquesting: Competitors are outbidding EcoRest by 42% on high-intent local search phrases.",
            "Creative Bottleneck: 34 active Meta ads rely entirely on static testimonials, ignoring screen-based video storytelling."
        ],
        "slide_2_bullets": [
            "The Halo Effect: Daytime broadcast presence drives immediate mobile/desktop organic brand searches.",
            "CAC Reduction: Proven 24% decrease in digital acquisition costs by stabilizing competitive auction dependency.",
            "Audience Capture: Reaching premium 35-64 homeowners who own 80% of local premium home assets."
        ],
        "slide_3_bullets": [
            "Efficiency Mix: Deploying a 60% Daytime Linear flight paired with high-impact CTV retargeting.",
            "Pixel Sync: Utilizing existing Meta pixels to retarget consumers exposed to our local broadcast windows.",
            "Next Steps: Reviewing customized local zone maps on Thursday."
        ]
    }
}

# Smart Input Matching Logic
if st.session_state.submitted:
    with st.spinner("Processing economic and digital footprint metrics..."):
        time.sleep(1.0)
        
    clean_url = prospect_url.lower()
    
    if "city" in clean_url or "furniture" in clean_url:
        data = mock_database["cityfurniture"]
    elif "ecorest" in clean_url or "bedding" in clean_url:
        data = mock_database["ecorest"]
    else:
        data = mock_database["cityfurniture"]
        
    st.markdown("---")
    st.success(f"⚡ STRATEGIC ACCOUNT BRIEFING COMPILED FOR: {data['prospect_name'].upper()}")
    
    # Text Meta Block
    st.write(f"**Target Account:** {data['prospect_name']}  |  **Market Vertical:** {data['vertical']}  |  **Analytical Framework:** Cost-Center Optimization Index")
    
    # 1. Scraped Signals Block (Full Width Panel)
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🕵️‍♂️ Scraped Commercial Footprint & Competitive Market Signals")
    st.write(f"• **Estimated Digital Capital Deployment:** {data['estimated_digital_monthly']}")
    st.write(f"• **Active Programmatic Asset Footprint:** {data['meta_ad_count']}")
    st.write(f"• **Search & Placement Automation Channels:** {data['google_ad_types']}")
    st.write(f"• **Data Analytics Infrastructure Found:** {data['pixel_detections']}")
    st.write(f"• ⚠️ **Market Share Erosion Risk:** {data['competitive_threat']}")
    st.write(f"• 💡 **Creative Asset Gap:** {data['creative_gap']}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 2. Strategy & Pitch Text Blocks
    st.markdown("### 🎯 Consultative Account Strategy")
    st.info(f"**The Valid Business Reason (VBR):**\n\n{data['vbr_statement']}")
    st.error(f"**Identified Operational Inefficiency:**\n\n{data['vulnerability']}")
    
    # 3. Outreach Copy Block
    st.markdown("### 📨 Automated Executive Outreach Script")
    st.text_input("Recommended Subject Line:", data['email_subject'])
    st.text_area("Generated Consultative Copy (Ready to Copy/Paste):", data['email_body'], height=250)
    
    # 4. Presentation Slides Content
    st.markdown("---")
    st.markdown("### 📊 Executive Presentation Content Architecture")
    st.write(f"**Proposed Marketing Capital Reallocation Mix:** {data['recommended_mix']}")
    st.caption("Utilize these structured business cases directly inside your presentation deck to execute a direct consultative sale:")
    
    # Slide 1
    st.markdown("<div class='slide-red'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 1: The Digital Bottleneck (Diminishing Marginal Returns in Auction Environments)**")
    for bullet in data['slide_1_bullets']:
        st.markdown(f"❌ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 2
    st.markdown("<div class='slide-green'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 2: The Portfolio Effect (Stabilizing Blended Acquisition Costs via Diversified Authority)**")
    for bullet in data['slide_2_bullets']:
        st.markdown(f"📈 {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 3
    st.markdown("<div class='slide-blue'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 3: The Efficiency Blueprint (Capital Reallocation and Margin Protection)**")
    for bullet in data['slide_3_bullets']:
        st.markdown(f"🛠️ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
# Construct the download text block
download_text = f"""==================================================
EXECUTIVE PRESENTATION CONTENT ARCHITECTURE
==================================================
Target Account: {data['prospect_name']}
Proposed Capital Reallocation Mix: {data['recommended_mix']}

--------------------------------------------------
SLIDE 1: The Digital Bottleneck 
(Diminishing Marginal Returns in Auction Environments)
--------------------------------------------------
""" + "\n".join([f"❌ {b}" for b in data['slide_1_bullets']]) + f"""

--------------------------------------------------
SLIDE 2: The Portfolio Effect 
(Stabilizing Blended Acquisition Costs via Diversified Authority)
--------------------------------------------------
""" + "\n".join([f"📈 {b}" for b in data['slide_2_bullets']]) + f"""

--------------------------------------------------
SLIDE 3: The Efficiency Blueprint 
(Capital Reallocation and Margin Protection)
--------------------------------------------------
""" + "\n".join([f"🛠️ {b}" for b in data['slide_3_bullets']])

# Render the download button in Streamlit
st.download_button(
    label="💾 Download Presentation Deck Script (TXT)",
    data=download_text,
    file_name=f"{data['prospect_name'].lower().replace(' ', '_')}_presentation_deck.txt",
    mime="text/plain"
)

