import streamlit as st
import time
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import io

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

# Helper function to generate PowerPoint presentation
def create_pptx_deck(data):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide layout node
    
    slides_config = [
        {"title": "Slide 1: Diminishing Returns in Siloed Auction Environments", "bullets": data['slide_1_bullets']},
        {"title": "Slide 2: The Portfolio Effect (Stabilizing Blended Acquisition Costs)", "bullets": data['slide_2_bullets']},
        {"title": "Slide 3: The Efficiency Blueprint (Convergent Capital Mix)", "bullets": data['slide_3_bullets']}
    ]
    
    for config in slides_config:
        slide = prs.slides.add_slide(blank_layout)
        shapes = slide.shapes
        rect = shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        rect.fill.solid()
        rect.fill.fore_color.rgb = RGBColor(30, 58, 138)
        rect.line.fill.background()
        
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.15), Inches(12), Inches(0.8))
        tf = txBox.text_frame
        p = tf.paragraphs[0]
        p.text = config["title"]
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        contentBox = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(11.833), Inches(5))
        ctf = contentBox.text_frame
        ctf.word_wrap = True
        
        for idx, bullet in enumerate(config["bullets"]):
            p_bullet = ctf.add_paragraph() if idx > 0 else ctf.paragraphs[0]
            p_bullet.text = f"• {bullet}"
            p_bullet.font.size = Pt(22)
            p_bullet.font.color.rgb = RGBColor(55, 65, 81)
            p_bullet.space_after = Pt(24)
            
    binary_output = io.BytesIO()
    prs.save(binary_output)
    binary_output.seek(0)
    return binary_output

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

# Session State Initialization
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

if "url_input" not in st.session_state:
    st.session_state.url_input = "https://cityfurniture.com"

prospect_url = st.text_input(
    "Input Target Prospect Website URL:", 
    value=st.session_state.url_input,
    key="url_box"
)

# Button Layout alignment
btn_col1, btn_col2, _ = st.columns(3)
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
        "creative_gap": "92% of marketing assets focus on low-dwell price promotional inventory. Dwell time is under 1.5 seconds. Massive deficit in broad equity storytelling or brand anchoring slots.",
        "competitive_threat": "Rooms To Go, Ashley, Wayfair, and Amazon are heavily outbidding them on bottom-of-funnel intent terms, driving up local auction CPM inflation.",
        "vulnerability": "Paying premium rates to harvest low-hanging demand that competitors can easily disrupt. They are essentially buying intent that national players control through massive ad spend budgets.",
        "vbr_statement": "Secure retail insights confirm that anchoring localized search campaigns with high-frequency daytime and early news broadcast blocks stabilizes customer acquisition cost (CAC) inflation by a proven 24%. This cross-platform mix establishes proprietary top-of-mind brand authority, cutting direct dependency on volatile ad bidding auctions.",
        "recommended_mix": "50% Local Linear TV Authority Layers | 30% Connected TV (CTV) Zip Targets | 20% Search/Social Retargeting Engine",
        "email_subject": "Bypassing national ad auction inflation for City Furniture",
        "email_body": "Hi Team City Furniture,\n\nI’ve been reviewing your regional customer acquisition footprint. Our enterprise analytics engine flagged that you are heavily leveraged within hyper-competitive automated ad auctions, balancing roughly 84 active social creative sets alongside a heavy Google PMax footprint.\n\nWhile this bottom-of-funnel approach converts active shoppers, it introduces an operational inefficiency: you are directly bidding against multi-billion dollar national players like Wayfair and Ashley, driving your digital acquisition costs up and leaving you vulnerable to margin erosion.\n\nOur vertical multi-market data shows that regional retailers who anchor their active search spend with high-frequency daytime and local news media blocks insulate their digital budgets, driving an immediate 24% drop in blended CAC and a 15% surge in direct organic web intent loops.\n\nI have structured a 3-slide strategic allocation model showing how this mix protection stabilizes your acquisition margins. Do you have 10 minutes this Thursday at 2 PM to run through the data?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": [
            "The Auction Trap: Bidding directly against multi-billion dollar national conglomerates (Wayfair, Ashley) on standard search keywords.",
            "Conversion Erosion: Over-leveraging bottom-of-funnel digital bidding drives up blended CAC as local auction prices inflate.",
            "The Attention Deficit: Dwell time on current programmatic mobile banners sits under 1.5 seconds, failing to anchor true household brand consideration."
        ],
        "slide_2_bullets": [
            "The Market Shield: Re-establishing localized broad-market equity reduces dependency on volatile platform auction bids.",
            "The Halo Effect: Anchoring search campaigns with strategic daytime and local news flights cuts digital CAC by 24%.",
            "Showroom Asset Lift: Integrating television authority loops yields a proven 22% increase in regional showroom foot traffic."
        ],
        "slide_3_bullets": [
            "Convergent Reallocation: Reallocating capital to 50% broad-market authority layers, 30% CTV targeting, and 20% optimized digital intent capture.",
            "Attribution Alignment: Measuring performance via broad marketing efficiency ratios (MER) and post-air organic spikes, bypassing siloed click tracking.",
            "Strategic Execution: Deploying low-risk test zones across high-propensity homeowner zip codes next month."
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

# --- THE DATA PROCESSING AREA (LINE-BY-LINE ALIGNED) ---
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
    
    st.write(f"**Target Account:** {data['prospect_name']}  |  **Market Vertical:** {data['vertical']}  |  **Analytical Framework:** Cost-Center Optimization Index")
    
    # 1. Upgraded Advanced Signal Scrape Matrix Panel
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown(f"### 🕵️‍♂️ Advanced Signal Scrape Matrix: {data['prospect_name'].upper()}")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("**💰 Monthly Capital Allocation**")
        st.text_area("Budget", value=data['estimated_digital_monthly'], height=68, label_visibility="collapsed", disabled=True)
    with m2:
        st.markdown("**📱 Active Social Creative Sets**")
        st.text_area("Social Footprint", value=data['meta_ad_count'], height=68, label_visibility="collapsed", disabled=True)
    with m3:
        st.markdown("**🎯 Search Automation Engine**")
        st.text_area("Google Channels", value=data['google_ad_types'], height=68, label_visibility="collapsed", disabled=True)
    with m4:
        st.markdown("**⚖️ Market Share Risk Index**")
        risk_label = "HIGH VOLATILITY" if "city" in clean_url or "furniture" in clean_url else "ELEVATED RISK"
        st.text_area("Risk Index", value=risk_label, height=68, label_visibility="collapsed", disabled=True)
        
    st.markdown("---")
    
    col_sig1, col_sig2 = st.columns(2)
    with col_sig1:
        st.markdown("#### 💻 Technical Infrastructure Diagnostics")
        st.markdown(f"• **Active Tracking Pixels Verified:** `{data['pixel_detections']}`")
        st.markdown("• **Attribution Tracking Script:** `Google Floodlight Enabled`" if "city" in clean_url or "furniture" in clean_url else "• **Attribution Tracking Script:** `Klaviyo Event Tracking Active`")
        st.markdown("• **SSL Security Framework:** `TLS 1.3 Certified (Secure Checkout Flow)`")
        st.markdown("• **Estimated Desktop Domain Authority (DA):** `64/100`" if "city" in clean_url or "furniture" in clean_url else "• **Estimated Desktop Domain Authority (DA):** `42/100`")
        
    with col_sig2:
        st.markdown("#### 📉 Strategic Gaps & Market Pressures")
        st.markdown(f"⚠️ **Market Share Erosion Threat:** {data['competitive_threat']}")
        st.markdown(f"💡 **Creative Asset Gap:** {data['creative_gap']}")
        st.markdown("• **Estimated Digital Share-of-Voice (SOV) Slip:** `Drop 14% YoY due to National Bidding Pods`" if "city" in clean_url or "furniture" in clean_url else "• **Estimated Digital Share-of-Voice (SOV) Slip:** `Drop 22% YoY vs Venture-Backed Competitors`")
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 2. Strategy & Pitch Text Blocks
    st.markdown("### 🎯 Consultative Account Strategy")
    st.info(f"**The Valid Business Reason (VBR):**\n\n{data['vbr_statement']}")
    st.error(f"**Identified Operational Inefficiency:**\n\n{data['vulnerability']}")
    
    # 3. Outreach Copy Block
    st.markdown("### 📨 Automated Executive Outreach Script")
    st.text_input("Recommended Subject Line:", data['email_subject'])
    st.text_area("Generated Consultative Copy (Ready to Copy/Paste):", data['email_body'], height=250)
    
    # 4. Presentation Slides Content Header with Real PPTX Downloader
    st.markdown("---")
    
    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        st.markdown("### 📊 Executive Presentation Content Architecture")
        st.write(f"**Proposed Marketing Capital Reallocation Mix:** {data['recommended_mix']}")
    with dl_col2:
        pptx_buffer = create_pptx_deck(data)
        st.download_button(
            label="📊 Download PowerPoint Slides (.PPTX)",
            data=pptx_buffer,
            file_name=f"{data['prospect_name'].lower().replace(' ', '_')}_executive_deck.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            type="secondary"
        )
        
    st.caption("Utilize these structured business cases directly inside your presentation deck to execute a direct consultative sale:")
    
    # Slide 1 Visual
    st.markdown("<div class='slide-red'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 1: The Digital Bottleneck (Diminishing Marginal Returns in Auction Environments)**")
    for bullet in data['slide_1_bullets']:
        st.markdown(f"❌ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 2 Visual
    st.markdown("<div class='slide-green'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 2: The Portfolio Effect (Stabilizing Blended Acquisition Costs via Diversified Authority)**")
    for bullet in data['slide_2_bullets']:
        st.markdown(f"📈 {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
        
    # Slide 3 Visual
    st.markdown("<div class='slide-blue'>", unsafe_allow_html=True)
    st.markdown("**SLIDE 3: The Efficiency Blueprint (Capital Reallocation and Margin Protection)**")
    for bullet in data['slide_3_bullets']:
        st.markdown(f"🛠️ {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)
