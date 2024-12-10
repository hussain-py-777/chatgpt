from playwright.sync_api import sync_playwright

def Artificial_intelligence_chat_Q2(text, page, num):
    text_ = text.replace('\n', ' ').strip()
    page.keyboard.type(text_)
    page.keyboard.press('Enter')
    page.wait_for_selector(f'div.markdownContainer >> nth={num}', timeout=30000)
    response_element = page.query_selector(f'div.markdownContainer >> nth={num}')
    num += 2
    previous_text = ""

    while True:
        if response_element:
            current_text = response_element.text_content().strip()
        else:
            current_text = ""

        if current_text != previous_text and current_text != "":
            previous_text = current_text
        elif current_text == previous_text and current_text != "":
            return current_text, num

with sync_playwright() as playwright:
    num = 0
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://deepai.org/')
    
    while True:
        user_input = input('chatgpt > ')
        response, num = Artificial_intelligence_chat_Q2(user_input, page, num)
        print(response)
