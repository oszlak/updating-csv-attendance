def sep_id(chat_file):
    f = open(chat_file, encoding="utf8")
    f_lines = f.readlines()
    f.close()
    id_lst = []
    for line in f_lines:
        line_striped = line.strip().split(" ")
        for c in range(len(line_striped)):
            if line_striped[c].isdigit() and len(line_striped[c]) > 5:
                id_lst.append(line_striped[c])
    return id_lst
'''
    with open("id_file2.txt","w") as file:
        for id in id_lst:
            file.write(str(id)+"\n")
sep_id("meeting_saved_chat.txt")
'''