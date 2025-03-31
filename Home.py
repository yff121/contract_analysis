# Home.py
import streamlit as st

st.set_page_config(
    page_title="智能文档处理平台",
    layout="centered",
    page_icon="📁",
    initial_sidebar_state="auto"
)

# 安全可靠的CSS样式
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: #f8f9fa !important;
        border-right: 1px solid #e0e0e0;
    }
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #202124;
        margin-bottom: 0.5rem;
    }
    .header-subtitle {
        color: #5f6368;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# 主页内容
st.markdown('<div class="header"><div class="header-title">📁 智能文档处理平台</div><div class="header-subtitle">高效、精准、安全的文档处理解决方案</div></div>', unsafe_allow_html=True)

# 功能卡片区
st.markdown("""
<style>
    .feature-card {
        border-radius: 10px;
        padding: 25px;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .feature-desc {
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container():
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">文档对比</div>
            <div class="feature-desc">快速比较两个文档版本之间的差异，精确到词语级别，支持PDF/Word/文本文件</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("开始使用", key="doc_compare", use_container_width=True):
            st.switch_page("pages/1_📊_文档对比.py")

with col2:
    with st.container():
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📑</div>
            <div class="feature-title">合规检查</div>
            <div class="feature-desc">自动检查合同文档是否符合相关法规要求，生成详细合规性报告</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("开始使用", key="compliance_check", use_container_width=True):
            # 确保session state中有api_key字段
            if "api_key" not in st.session_state:
                st.session_state["api_key"] = ""
            st.switch_page("pages/2_📑_合规检查.py")
