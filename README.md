# Day 3·4 카페 실습 — Colab에서 실행합니다

어제 완료본(`jnu-llmops-precourse-day2/solution`)을 **밖에서 부르는** 노트북입니다. 설치 없이 Google Colab에서 엽니다. 노트북의 첫 Cell이 필요한 저장소를 받아 옵니다.

| 순서 | 노트북 | 하는 일 | 기대 결과 |
| --- | --- | --- | --- |
| Day 3 · 1교시 | [day3_structures.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day3_structures.ipynb) | 네 겹 · 두 겹 · 한 덩어리, 세 구조로 같은 주문을 계산합니다 | 세 버전 모두 7200원 |
| Day 3 · 3교시 | [day3_gatekeeper.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day3_gatekeeper.ipynb) | 주문 기록 12건을 문지기 `check_order`로 통과·거부로 나눕니다 | 통과 10 · 거부 2 · 합계 112,250원 |
| Day 4 | [day4_mock.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day4_mock.ipynb) | 대역 `suggest_order`의 제안 5건을 같은 문지기와 기대표로 검사합니다 | 통과 3 · 거부 2 |

## 여는 법

1. 위 링크를 누르면 Colab이 열립니다. Google 계정으로 로그인합니다.
2. `런타임 → 모두 실행`. 세션이 끊기면 첫 Cell부터 다시 실행합니다.
3. 수정한 노트북은 `파일 → 다운로드 → .ipynb`로 내려받아 개인 Branch에 commit합니다.

## 폴더

- `notebooks/` — 학생용 노트북. `day3_gatekeeper.ipynb`의 문지기는 2·3번 조건이 비어 있습니다.
- `data/orders.json` — 교육용 합성 주문 기록 12건 (실제 매장 기록이 아닙니다). 정상 10건, 깨진 2건.
- `data/expected_day3.json`, `data/expected_day4.json` — 기대표.
- `solutions/` — 강사용 완성본. 실습 중에는 열지 않습니다.

## 실제 실행 결과 (강사, 2026-09-09)

- `day3_structures`: 7200 · 7200 · 7200
- `day3_gatekeeper` 완성본: 통과 10건 · 거부 2건(A07 없는 메뉴: 녹차라떼, A11 필수 Key 없음: is_student) · 합계 112,250원. 문지기를 채우기 전(배포본)은 통과 10 · 거부 1 · 놓침 1(A07이 문지기를 지나 KeyError로 드러남).
- `day4_mock`: 통과 3 · 거부 2 · 기대표 검사 통과
