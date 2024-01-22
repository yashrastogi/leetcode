class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = chars[0]
        count = 1
        writer_ptr = 0
        for i in range(1, len(chars)):
            char = chars[i]
            if curr_char != char:
                chars[writer_ptr] = curr_char
                writer_ptr += 1
                if count > 9:
                    str_count = str(count)
                    for c in str_count:
                        chars[writer_ptr] = c
                        writer_ptr += 1
                elif count > 1:
                    chars[writer_ptr] = str(count)
                    writer_ptr += 1
                curr_char = char
                count = 0
            count += 1
        chars[writer_ptr] = curr_char
        writer_ptr += 1
        if count > 9:
            str_count = str(count)
            for c in str_count:
                chars[writer_ptr] = c
                writer_ptr += 1
        elif count > 1:
            chars[writer_ptr] = str(count)
            writer_ptr += 1
        return writer_ptr
