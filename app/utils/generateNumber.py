
def Generate62(phone: str) -> str:
    if phone[0] == "0":
        phone = "62" + phone[1:]
        
    return phone