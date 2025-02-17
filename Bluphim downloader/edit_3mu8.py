with open ("test.txt", "r") as f:
    datas = f.read()
    datas = datas.split("\n")

# Nếu Gặp dấu "#" thì xóa nó đi
for data in datas:
    if data.startswith("#"):
        datas.remove(data)
    else:
        pass

with open ("test.txt", "w") as f:
    f.write("\n".join(datas))
