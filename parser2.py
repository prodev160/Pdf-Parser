import slate3k as slate
import csv

FILE_NAME = 'Delinquent RE 2020 January PUBLIC'

def isEmpty(str):
    str = str.replace(" ", "")
    str = str.replace(chr(12), "")
    if len(str) == 0:
        return False
    else:
        return True

with open(FILE_NAME + '.pdf','rb') as f:
    extracted_text = slate.PDF(f)

with open(FILE_NAME + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Parid", "Owner Name", "Address", "Amount Each Bill", "Prior Year"])
    page_num = 0
    page_count = len(extracted_text)
    for page_txt in extracted_text:
        page_boxes = page_txt.split('\n')
        page_boxes = list(filter(isEmpty, page_boxes))
        line_index = 8
        line_num = len(page_boxes)
        line_num = line_num - 1
        if page_num == (page_count - 1):
            line_num = line_num - 1

        while line_index < line_num:
            Parid = page_boxes[line_index]
            line_index = line_index + 1
            Owner_name = page_boxes[line_index]
            line_index = line_index + 1
            Address = page_boxes[line_index]
            line_index = line_index + 1
            Amount_Each_Bill = page_boxes[line_index]
            line_index = line_index + 1
            Prior_year = page_boxes[line_index]
            line_index = line_index + 1
            writer.writerow([Parid, Owner_name, Address, Amount_Each_Bill, Prior_year])
        page_num = page_num + 1
print("Finished parsing!")