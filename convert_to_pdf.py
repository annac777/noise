import os
import sys
from playwright.sync_api import sync_playwright

def convert_html_to_pdf(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    print(f"Converting {input_file} to {output_file}...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Construct absolute file path
        file_path = os.path.abspath(input_file)
        page.goto(f'file://{file_path}')
        
        # Wait for content to load
        page.wait_for_load_state('networkidle')
        
        # Generate PDF
        # format='A4' or width/height can be specified. 
        # print_background=True ensures colors/images are printed.
        page.pdf(
            path=output_path, 
            format='A4', 
            print_background=True, 
            margin={'top': '1cm', 'bottom': '1cm', 'left': '1cm', 'right': '1cm'}
        )
        
        browser.close()
        
    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    convert_html_to_pdf('testing.html', 'testing.pdf')
