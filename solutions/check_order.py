from catalog import MENU

REQUIRED_KEYS = ("order_id", "items", "is_student")

def check_order(record):
    for key in REQUIRED_KEYS:                       # 1. 필수 Key
        if key not in record:
            return False, f"필수 Key 없음: {key}"
    for item in record["items"]:
        if item["menu_name"] not in MENU:           # 2. 허용 메뉴
            return False, f"없는 메뉴: {item['menu_name']}"
        quantity = item["quantity"]
        if type(quantity) is not int or not 1 <= quantity <= 10:   # 3. 수량 범위
            return False, f"수량 범위 밖: {quantity!r}"
    return True, ""
