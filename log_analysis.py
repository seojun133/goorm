def load_logs(filename: str) -> list:
    """주어진 log.txt 파일을 읽고, 각 줄을 리스트에 저장하여 반환."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: 파일 '{filename}'을 찾을 수 없습니다.")
        return []

def parse_logs(log_lines: list) -> dict:
    """로그 리스트를 받아 날짜별 사용자 활동을 딕셔너리로 변환."""
    log_data = {}
    for line in log_lines:
        parts = line.split()
        if len(parts) < 3:
            continue  # 잘못된 형식 무시
        date, user_id, activity = parts[0], parts[1], parts[2]
        log_data.setdefault(date, {}).setdefault(user_id, []).append(activity)
    return log_data

def get_user_activity(log_data: dict, user_id: str) -> dict:
    """특정 사용자의 활동 내역을 날짜별로 반환."""
    user_activity = {}
    for date, users in log_data.items():
        if user_id in users:
            user_activity[date] = users[user_id]
    return user_activity

def save_summary(log_data: dict, filename: str) -> None:
    """날짜별 사용자 활동 내역을 파일로 저장."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for date, users in sorted(log_data.items()):
                file.write(f"{date}\n")
                for user, activities in users.items():
                    file.write(f"- {user}: {', '.join(activities)}\n")
                file.write("\n")
    except IOError as e:
        print(f"파일 저장 중 오류 발생: {e}")