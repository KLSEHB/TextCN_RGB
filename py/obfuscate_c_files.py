import os
import re
import random
import shutil

C_KEYWORDS = {
    "auto","break","case","char","const","continue","default","do","double",
    "else","enum","extern","float","for","goto","if","inline","int","long",
    "register","restrict","return","short","signed","sizeof","static","struct",
    "switch","typedef","union","unsigned","void","volatile","while","_Bool",
    "_Complex","_Imaginary"
}

def random_identifier(length=6):

    letters = "abcdefghijklmnopqrstuvwxyz"
    return "var_" + "".join(random.choice(letters) for _ in range(length))

def rename_variables(code):

    identifiers = set(re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", code))
    identifiers = [idf for idf in identifiers if idf not in C_KEYWORDS]

    mapping = {}
    for var in identifiers:
        if random.random() < 0.4:
            mapping[var] = random_identifier()

    # 替换变量名
    for old, new in mapping.items():
        code = re.sub(rf"\b{old}\b", new, code)

    return code

def insert_dummy_code(code):

    dummy_templates = [
        "int {name} = 0; {name} += 1;",
        "int {name} = 123; {name} -= 5;",
        "{name} = 0;",
        ";"
    ]

    # 找出所有函数体的大括号范围
    pattern = re.compile(r"\{([^{}]*)\}", re.DOTALL)
    matches = list(pattern.finditer(code))

    new_code = code
    offset = 0

    for match in matches:
        if random.random() < 0.5:
            insert_pos = match.start(1) + offset
            dummy = random.choice(dummy_templates).format(name=random_identifier())
            insert_code = "    " + dummy + "\n"
            new_code = new_code[:insert_pos] + insert_code + new_code[insert_pos:]
            offset += len(insert_code)

    return new_code

def process_file(src_path, dst_path):
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    code = rename_variables(code)
    code = insert_dummy_code(code)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(code)

def process_directories(src_dir, dst_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".c"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_dir)
                dst_path = os.path.join(dst_dir, rel_path)
                process_file(src_path, dst_path)
                print(f"Processed: {src_path} -> {dst_path}")

if __name__ == "__main__":

    SRC_DIR1 = "path/to/input_dir1"
    DST_DIR1 = "path/to/output_dir1"
    SRC_DIR2 = "path/to/input_dir2"
    DST_DIR2 = "path/to/output_dir2"

    process_directories(SRC_DIR1, DST_DIR1)
    process_directories(SRC_DIR2, DST_DIR2)
