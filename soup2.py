from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<div class="_1hl2r">
    <!-- ... (other HTML elements) ... -->
    <div class="_21Ahp">
        <span dir="ltr" aria-label="" class="_11JPr selectable-text copyable-text" data-pre-plain-text="Text 1">
            <span>quem gosta de foto é ele</span>
        </span>
    </div>
    <div class="_21Ahp">
        <span dir="ltr" aria-label="" class="_11JPr selectable-text copyable-text" data-pre-plain-text="Text 2">
            <span>quem gosta de foto é ela</span>
        </span>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

elements_with_attribute = soup.select(".copyable-text")

for element in elements_with_attribute:
    data_pre_plain_text = element['data-pre-plain-text']
    print(data_pre_plain_text)
