import streamlit as st
import difflib
from pathlib import Path
from docx import Document
import pdfplumber
import html

def extract_text(file):
    """提取文件内容并保留原始格式"""
    file_type = Path(file.name).suffix.lower()
    
    try:
        if file_type == '.pdf':
            text = []
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text.append(page.extract_text(x_tolerance=1, y_tolerance=1))
            return '\n'.join(text)
        
        elif file_type == '.docx':
            doc = Document(file)
            return '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        
        else:  # txt/md等文本文件
            return file.read().decode("utf-8")
    
    except Exception as e:
        st.error(f"文件解析失败: {str(e)}")
        return ""

def highlight_changes(old_text, new_text):
    """生成词语级差异标记"""
    seq_matcher = difflib.SequenceMatcher(None, old_text, new_text)
    
    # 旧文本处理
    old_html = []
    # 新文本处理
    new_html = []
    
    # 特殊字符转义
    old_text = html.escape(old_text)
    new_text = html.escape(new_text)

    # 旧文本标记（红色）
    for tag, i1, i2, j1, j2 in seq_matcher.get_opcodes():
        if tag == 'equal':
            old_html.append(old_text[i1:i2])
        elif tag == 'delete':
            old_html.append(f'<span style="background-color:#ffcccc">{old_text[i1:i2]}</span>')
        elif tag == 'replace':
            old_html.append(f'<span style="background-color:#ffcccc">{old_text[i1:i2]}</span>')
        elif tag == 'insert':
            pass

    # 新文本标记（绿色）
    for tag, i1, i2, j1, j2 in seq_matcher.get_opcodes():
        if tag == 'equal':
            new_html.append(new_text[j1:j2])
        elif tag == 'insert':
            new_html.append(f'<span style="background-color:#ccffcc">{new_text[j1:j2]}</span>')
        elif tag == 'replace':
            new_html.append(f'<span style="background-color:#ccffcc">{new_text[j1:j2]}</span>')
        elif tag == 'delete':
            pass

    # 保留原始换行格式
    return (
        f'<div style="font-family:SimSun; white-space:pre-wrap;">{"".join(old_html)}</div>',
        f'<div style="font-family:SimSun; white-space:pre-wrap;">{"".join(new_html)}</div>'
    )

def main():
    st.set_page_config(
        page_title="文档差异对比器",
        layout="wide",
        page_icon="📊"
    )
    
    st.title("📊 文档差异对比工具")
    
    # 文件上传区
    col1, col2 = st.columns(2)
    with col1:
        old_file = st.file_uploader("上传旧版本", type=['pdf', 'docx', 'txt', 'md'])
    with col2:
        new_file = st.file_uploader("上传新版本", type=['pdf', 'docx', 'txt', 'md'])
    
    if old_file and new_file:
        # 解析文本内容
        with st.spinner("正在解析文档..."):
            old_text = extract_text(old_file)
            new_text = extract_text(new_file)
        
        # 生成对比结果
        old_html, new_html = highlight_changes(old_text, new_text)
        
        # 双栏显示布局
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"旧版本 · {old_file.name}")
            st.markdown(old_html, unsafe_allow_html=True)
        
        with col2:
            st.subheader(f"新版本 · {new_file.name}")
            st.markdown(new_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()