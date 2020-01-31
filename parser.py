import slate3k as slate
import csv

FILE_NAME = 'open liens'

def isEmpty(str):
    str = str.replace(" ", "")
    str = str.replace(chr(12), "")
    if len(str) == 0:
        return False
    else:
        return True

with open(FILE_NAME + '.pdf','rb') as f:
    extracted_text = slate.PDF(f)

merged_lines = []
page_num = 1
for page_txt in extracted_text:
    # page_txt : each page content
    if page_num != 1 and "Payments" in page_txt:
        break
    page_lines = page_txt.split('\n')
    page_lines = list(filter(isEmpty, page_lines))
    line_num = len(page_lines)
    if page_num == 1:
        line_index = 20
    else:
        line_index = 7
    while line_index < line_num:
        line_words = list(filter(isEmpty, page_lines[line_index].split(' ')))
        if "Continued" in page_lines[line_index] or line_words[0] == "Tax" or line_words[0] == "Sewer" or line_words[0] == "Misc":
            line_index = line_index + 1
            continue
        merged_lines.append(page_lines[line_index])
        line_index = line_index + 1
    page_num = page_num + 1
line_index = 0
merged_line_num = len(merged_lines)

with open(FILE_NAME + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Block", "Lot", "Qual", "Tax Year", "Cert Num", "Property Location", "Total in Sale", "Begin in Sale"])

    while line_index < merged_line_num:
        # start parsing block
        # block variable
        block = merged_lines[line_index][:15].strip()
        line_index = line_index + 1
        lot = merged_lines[line_index][:15].strip()
        line_index = line_index + 1
        qual = merged_lines[line_index][:15].strip()
        taxyear = merged_lines[line_index][65:95].strip()
        line_index = line_index + 1
        certnum = merged_lines[line_index][:15].strip()
        prop_location = merged_lines[line_index][15:75].strip()
        line_index = line_index + 1
        if not "Total In Sale:" in merged_lines[line_index]:
            line_index = line_index + 1
        if not "Total In Sale:" in merged_lines[line_index]:
            line_index = line_index + 1
        total_sale = merged_lines[line_index][90:].strip()
        line_index = line_index + 1
        begin_sale = merged_lines[line_index][90:].strip()
        line_index = line_index + 1
        writer.writerow([block, lot, qual, taxyear, certnum, prop_location, total_sale, begin_sale])
print("Finished parsing!")