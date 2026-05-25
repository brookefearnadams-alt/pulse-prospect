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

# Helper function to generate deep, multi-data PowerPoint presentation arrays
def create_pptx_deck(data, clean_url):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # ----------------------------------------------------
    # SLIDE 1: Enterprise Data Scrape & Signal Matrix
    # ----------------------------------------------------
    slide_1 = prs.slides.add_slide(blank_layout)
    
    # Header Blue Band
    rect_1 = slide_1.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
    rect_1.fill.solid()
    rect_1.fill.fore_color.rgb = RGBColor(30, 58, 138)
    rect_1.line.fill.background()
    
    txBox_1 = slide_1.shapes.add_textbox(Inches(0.5), Inches(0.15), Inches(12.333), Inches(0.8))
    p1 = txBox_1.text_frame.paragraphs[0]
    p1.text = f"{data['prospect_name']} — Enterprise Signal Scrape Matrix"
    p1.font.size = Pt(26)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    
    # Add Large Data Grid Table Shape (Rows: 7, Columns: 2)
    x, y, cx, cy = Inches(0.5), Inches(1.5), Inches(12.333), Inches(5.5)
    table_shape = slide_1.shapes.add_table(7, 2, x, y, cx, cy)
    table = table_shape.table
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(9.133)
    
    # Populate Matrix Rows
    risk_label = "HIGH VOLATILITY / STRUCTURAL COMPRESSION RISK" if "city" in clean_url or "furniture" in clean_url else "ELEVATED CONVERSION AUCTION RISK"
    sov_label = "Drop 14% YoY due to National Corporate Bidding Pods" if "city" in clean_url or "furniture" in clean_url else "Drop 22% YoY vs Aggressive Venture-Backed Scale Players"
    infra_label = "Google Floodlight Enabled Tracker | TLS 1.3 Certified Checkout" if "city" in clean_url or "furniture" in clean_url else "Klaviyo Direct Event Sync Active | TLS 1.3 Certified Flow"
    
    matrix_data = [
        ["Market Classification & Vertical", data['vertical']],
        ["Est. Monthly Digital Capital Deployment", data['estimated_digital_monthly']],
        ["Active Social/Programmatic Creative Footprint", data['meta_ad_count']],
        ["Search & Core Automation Channels", data['google_ad_types']],
        ["Verified Tracking Infrastructure Found", f"{data['pixel_detections']} | {infra_label}"],
        ["Market Share Erosion & Conquest Risks", data['competitive_threat']],
        ["Core Creative Asset Optimization Deficit", data['creative_gap']]
    ]
    
    for row_idx, row_content in enumerate(matrix_data):
        for col_idx, cell_text in enumerate(row_content):
            cell = table.cell(row_idx, col_idx)
            cell.text = cell_text
            # Formatting text size layout cleanly inside cells
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(13)
            p.font.color.rgb = RGBColor(55, 65, 81)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = RGBColor(30, 58, 138)
                
    # ----------------------------------------------------
    # SLIDE 2: Consultative Strategic Action Briefing
    # ----------------------------------------------------
    slide_2 = prs.slides.add_slide(blank_layout)
    
    # Header Blue Band
    rect_2 = slide_2.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
    rect_2.fill.solid()
    rect_2.fill.fore_color.rgb = RGBColor(30, 58, 138)
    rect_2.line.fill.background()
    
    txBox_2 = slide_2.shapes.add_textbox(Inches(0.5), Inches(0.15), Inches(12.333), Inches(0.8))
    p2 = txBox_2.text_frame.paragraphs[0]
    p2.text = f"{data['prospect_name']} — Consultative Account Strategy"
    p2.font.size = Pt(26)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)
    
    # Left Box Container - Strategy Pillars (Full Width Framework)
    leftBox = slide_2.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(6.0), Inches(5.5))
    ltf = leftBox.text_frame
    ltf.word_wrap = True
    
    lp1 = ltf.paragraphs[0]
    lp1.text = "🎯 Core Optimization Strategy"
    lp1.font.size = Pt(20)
    lp1.font.bold = True
    lp1.font.color.rgb = RGBColor(30, 58, 138)
    
    lp2 = ltf.add_paragraph()
    lp2.text = f"\n• Valid Business Reason (VBR):\n{data['vbr_statement']}"
    lp2.font.size = Pt(12)
    lp2.space_after = Pt(10)
    
    lp3 = ltf.add_paragraph()
    lp3.text = f"• Identified Operational Inefficiency:\n{data['vulnerability']}"
    lp3.font.size = Pt(12)
    lp3.space_after = Pt(10)
    
    lp4 = ltf.add_paragraph()
    lp4.text = f"• Proposed Capital Reallocation Mix:\n{data['recommended_mix']}"
    lp4.font.size = Pt(12)
    lp4.font.bold = True
    
    # Right Box Container - Actionable Email Copy Block
    rightBox = slide_2.shapes.add_textbox(Inches(6.8), Inches(1.5), Inches(6.0), Inches(5.5))
    rtf = rightBox.text_frame
    rtf.word_wrap = True
    
    rp1 = rtf.paragraphs[0]
    rp1.text = "✉️ Executive Outreach Blueprint"
    rp1.font.size = Pt(20)
    rp1.font.bold = True
    rp1.font.color.rgb = RGBColor(30, 58, 138)
    
    rp2 = rtf.add_paragraph()
    rp2.text = f"\nSubject: {data['email_subject']}\n\n{data['email_body']}"
    rp2.font.size = Pt(10)
    
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
st.sidebar.success("### 🧠 Elvex Workflow Intelligence Nodes")
st.sidebar.info("✔ Web Scraper Node [Active]")
st.sidebar.info("✔ Cross-Platform Grounding Database [Active]")
st.sidebar.info("✔ Business Rule Formulation Persona [Active]")
st.sidebar.markdown("---")
st.sidebar.markdown("**Demo Input Mapping:**")
st.sidebar.write("• Type **'cityfurniture'** for South Florida regional retail intelligence.")
st.sidebar.write("• Type **'ecorest'** for premium DTC mattress metrics.")

# Session State Initialization
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Performance Tickers
t1, t2, t3, t4 = st.columns(4)
t1.metric(label="Average Cross-Platform CAC Drop", value="-24%")
t2.metric(label="Multi-Screen Conversion Lift", value="3.2x")
t3.metric(label="Showroom Foot Traffic Lift", value="+22%")
t4.metric(label="Elvex Processing Time", value="1.2 Sec")

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

# Elvex-Enriched Strategy Database
mock_database = {
    "cityfurniture": {
        "prospect_name": "CITY Furniture",
        "corporate_intel": "Regional Retail Powerhouse | South Florida Footprint",
        "estimated_digital_monthly": "$150,000 - $200,000",
        "meta_ad_count": "45+ Active Creative Variations",
        "google_ad_types": "Search, PMax, Local Campaigns",
        "pixel_detections": "Meta Pixel, Google Tag Manager, Floodlight Tracker",
        "creative_gap": "Heavy reliance on programmatic display and high-turnover item promotions.",
        "competitive_threat": "National competitors like Wayfair and Ashley Furniture executing aggressive local keyword conquesting.",
        "vulnerability": "Auction competition inflating digital acquisition costs, combined with display ad dwell times dropping below 1.5 seconds.",
        "vbr_statement": "Verified cross-platform retail tracking confirms that anchoring localized digital search spend with high-frequency daytime and local news broadcast media blocks drops blended digital Customer Acquisition Cost (CAC) by 24% while driving an immediate 15% surge in high-intent organic brand searches.",
        "recommended_mix": "Convergent Mix: 50% Mass Local Linear TV Authority Layers | 30% Hyper-Targeted Connected TV | 20% Search/Social Retargeting Shield",
        "email_subject": "Optimizing CITY Furniture's customer acquisition costs and showroom foot traffic by 22%",
        "email_body": "Hi Team CITY Furniture,\n\nI’ve been tracking your market footprint across South Florida. Our enterprise intelligence analytics engine flags that your digital acquisition layer is heavily leveraged within automated ad auctions, facing intense local keyword conquesting from national scale competitors like Wayfair and Ashley.\n\nWhile your e-commerce retargeting captures immediate intent, a digital-only approach leaves you vulnerable: auction competition is inflating your acquisition costs, and average display ad dwell time has dropped below 1.5 seconds.\n\nOur cross-platform data reveals that regional retailers who anchor their search and social engines with structured daytime and local news media blocks create an insulation layer that reduces digital CAC by 24%, while triggering a 22% increase in verified showroom foot traffic.\n\nI’ve mapped out a 3-slide efficiency blueprint showing how a convergent media allocation will protect CITY Furniture's product margins this quarter. Do you have 10 minutes this Thursday at 2 PM to look over the metrics?\n\nBest,\n[Account Executive Name]",
        "slide_1_bullets": [
            "The Auction Trap: Bidding directly against multi-billion dollar national conglomerates on hyper-crowded search keywords.",
            "Margin Pressure: Digital acquisition costs (CAC) are rising as local programmatic auction bids inflate across Florida markets.",
            "The Attention Gap: Dwell time on transactional digital banner inventory sits under 1.5 seconds, failing to capture lasting household consideration."
        ],
        "slide_2_bullets": [
            "The Portfolio Multiplier: Moving away from siloed digital tactics and adding an offline mass authority layer triggers a 3.2x multi-screen conversion rate lift.",
            "The Cost Shield: Anchoring digital search and social spending with daytime and early news broadcast flights drops digital CAC by 24%.",
            "Showroom Asset Lift: Media convergence builds market-wide brand equity, yielding a proven 22% increase in verified in-store foot traffic."
        ],
        "slide_3_bullets": [
            "Convergent Reallocation: Moving budget into a resilient allocation of 50% broad-market authority blocks, 30% zip-code targeted CTV, and 20% digital retargeting capture.",
            "Advanced Attribution: Measuring campaign success through blended Marketing Efficiency Ratios (MER) and post-air organic spikes, bypassing broken click tracking pixels.",
            "Strategic Execution: Coordinating localized media test windows across high-propensity South Florida homeowner demographics next month."
        ]
    },
    "ecorest": {
        "prospect_name": "EcoRest Bedding",
        "vertical": "DTC Home Goods / Premium Mattress",
        "corporate_intel": "DTC E-Commerce Scale Player | Focus: Premium Organic Latex Lines",
        "estimated_digital_monthly": "$45,000 - $60,000",
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
