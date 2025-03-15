class UtilsService:
    def __init__(self):
        pass

    def find_line_and_column_from_index(self, text, index):
        lines = text.splitlines(keepends=True)  # Giữ ký tự xuống dòng
        char_count = 0

        for line_number, line in enumerate(lines, start=1):
            line_start_index = char_count  # Lưu vị trí bắt đầu của dòng hiện tại
            char_count += len(line)

            if char_count > index:  # Nếu index thuộc dòng này
                column_number = index - line_start_index + 1  # Cột tính từ 1
                return line_number, column_number
        
        return None, None  # Nếu index vượt quá độ dài của text
