class UtilsService:
    def __init__(self):
        pass

    def find_line_from_index(self, text, index):
        lines = text.splitlines(keepends=True)  # Giữ ký tự xuống dòng để tính toán chính xác
        char_count = 0

        for line_number, line in enumerate(lines, start=1):
            char_count += len(line)
            if char_count > index:
                return line_number
        
        return None  # Trả về None nếu index vượt quá độ dài chuỗi