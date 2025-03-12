import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 현재 파일 경로 추가
import log_analysis

# 로그 파일 로드
logs = log_analysis.load_logs("log.txt")

# 로그 데이터 파싱
log_data = log_analysis.parse_logs(logs)

# 특정 사용자 활동 출력
user_id = "user123"
print(log_analysis.get_user_activity(log_data, user_id))

# 요약 파일 저장
log_analysis.save_summary(log_data, "summary.txt")