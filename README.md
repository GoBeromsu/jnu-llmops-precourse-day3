# Day 3·4 카페 실습 — Colab에서 실행합니다

지난 시간 질문을 먼저 정리하고, 1교시 실습 안내에서 Colab을 열어요. GitHub에는 원본이 있고, 코드는 Colab에서 실행해요. 첫 코드 칸이 필요한 파일을 받아 와요. AI API 키나 믹서는 필요하지 않아요.

| 순서 | 노트북 | 하는 일 | 기대 결과 |
| --- | --- | --- | --- |
| Day 3 · 1교시 | [day3_structures.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day3_structures.ipynb) | 네 겹 · 두 겹 · 한 덩어리, 세 구조로 같은 주문을 계산합니다 | 세 버전 모두 7200원 |
| Day 3 · 2교시 MCP | [day3_mcp.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day3_mcp.ipynb) | 실제 MCP 서버에서 도구 목록을 받고 채널 40의 거부 이유를 확인해요 | 도구 24개 · 입력 오류 -32602 |
| Day 3 · 2·3교시 주문 | [day3_gatekeeper.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day3_gatekeeper.ipynb) | 2교시에 기록을 읽고, 3교시에 검사 조건 두 곳을 채워요 | 통과 10 · 거부 2 · 놓침 0 · 수량 검사 2건 거부 |
| Day 4 | [day4_mock.ipynb](https://colab.research.google.com/github/GoBeromsu/jnu-llmops-precourse-day3/blob/main/notebooks/day4_mock.ipynb) | 대역 `suggest_order`의 제안 5건을 같은 문지기와 기대표로 검사합니다 | 통과 3 · 거부 2 |

## 여는 법

1. 위 링크를 누르면 Colab이 열려요. Google 계정으로 로그인하세요.
2. `파일 → Drive에 사본 저장`을 눌러 내 답을 남길 사본을 만들어요. 사본은 내 Drive에 남고, 앞으로 고친 내용도 사본에 저장돼요.
3. 코드 칸 왼쪽의 ▶를 눌러요. 수업 중에는 안내한 칸부터 순서대로 실행해요.
4. 설치한 프로그램과 변수는 잠시 자리를 비우면 사라져요. 사본의 코드와 글은 그대로 남아 있으니 첫 칸부터 다시 실행하면 돼요. 다 작성한 뒤에는 `런타임 → 모두 실행`으로 다시 확인할 수 있어요.
5. 수정한 노트북은 `파일 → 다운로드 → .ipynb`로 내려받을 수 있어요.

실행 1과 실행 2는 `day3_structures` 하나에서 이어져요. MCP를 확인할 때는 `day3_mcp`, 주문 기록을 읽을 때는 `day3_gatekeeper`를 열어요.

## MCP 실습에서 확인할 것

- 서버는 `x-m32-mcp-server@3.3.0`, Python 클라이언트는 `mcp==1.26.0`, Node.js 실행 환경은 `nodejs-wheel==22.14.0`을 사용해요.
- 첫 코드 칸은 위 버전의 패키지를 Colab에 설치해요. nodejs-wheel은 Node.js를 Python 패키지로 배포하는 외부 프로젝트예요. 인터넷이 필요해요.
- 두 번째 코드 칸은 서버 프로그램을 인터넷에서 내려받아 실행해요. 처음에는 시간이 걸릴 수 있어요. ▶ 자리에 표시가 돌고 있으면 기다려요.
- `tools/list`로 도구 24개를 받고 `channel_set_volume`의 입력 규격을 읽어요.
- 채널 `40`을 보내면 허용 범위 1~32를 벗어나 거부돼요. **채널 번호는 바꾸지 않아요.**
- `connection_connect`나 정상 볼륨 변경은 호출하지 않아요. 실제 장비와 AI 모델을 사용하지 않아요.
- 설치가 실패하면 오류 메시지를 강사에게 보여 주세요. 출력이 없는데 성공한 것으로 적지 않아요.

## 폴더

- `notebooks/` — 학생용 노트북. `day3_gatekeeper.ipynb`의 문지기는 2·3번 조건이 비어 있습니다.
- `data/orders.json` — 교육용 합성 주문 기록 12건 (실제 매장 기록이 아닙니다). 정상 10건, 깨진 2건.
- `data/expected_day3.json`, `data/expected_day4.json` — 기대표.
- `solutions/` — 강사용 완성본. 막힌 곳을 비교할 때 참고할 수 있어요.

## 실제 실행 결과 (강사, 2026-09-09)

- `day3_structures`: 7200 · 7200 · 7200
- `day3_gatekeeper` 완성본: 통과 10건 · 거부 2건(A07 없는 메뉴: 녹차라떼, A11 필수 Key 없음: is_student) · 합계 112,250원. 문지기를 채우기 전(배포본)은 통과 10 · 거부 1 · 놓침 1(A07이 문지기를 지나 KeyError로 드러남).
- `day4_mock`: 통과 3 · 거부 2 · 기대표 검사 통과
- `day3_mcp`: 실제 서버에서 도구 24개 조회, 채널 40에 `-32602` 입력 거부 확인.

위 결과는 로컬 Python 3.11과 nbclient로 확인했어요. 실제 Colab 브라우저에서의 실행은 별도 확인이 필요해요. 주문 검사 함수는 오늘 데이터에 필요한 검사만 하며 모든 형태의 주문을 검사하지는 않아요. `orders_result.json`에는 놓침 목록이 저장되지 않으므로 놓침이 남은 파일을 완성 결과로 제출하지 않아요.

## 안내문 작성 기준

[토스의 8가지 라이팅 원칙들](https://toss.tech/article/8-writing-principles-of-toss)을 참고했어요. 다음에 할 일과 보일 결과를 먼저 적고, 중복 설명과 어려운 표현을 줄였어요. 오류의 의미와 다시 시작할 방법을 함께 안내해요.
