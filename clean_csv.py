import pandas as pd

# ── 1. CSV 파일 읽기 ─────────────────────────────────────
# na_values="\\N" → CSV 안의 \N을 자동으로 빈칸(NaN)으로 변환해요
df = pd.read_csv("races.csv", na_values="\\N")

print(f"✅ 파일 읽기 완료! 총 {len(df)}개 행")
print(f"📋 컬럼 목록: {list(df.columns)}")

# ── 2. 빈칸을 빈 문자열로 바꾸기 ────────────────────────
# MySQL Import Wizard는 빈 문자열("")을 NULL로 자동 처리해요
df = df.where(pd.notnull(df), "")

print("✅ \\N 값 → 빈칸 변환 완료!")

# ── 3. 깨끗해진 CSV로 저장 ───────────────────────────────
df.to_csv("races_clean.csv", index=False)

print("✅ races_clean.csv 저장 완료!")
print("👉 이제 races_clean.csv 파일로 MySQL Import 하세요!")
