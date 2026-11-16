# v2 — 모든 자료 연동 + 10계열 통합 학습

v1(4개 모델 비교, 기준서 v1)과 **별도**로 진행하는 확장 실험이다. v1 공통 도구(`tools/`)와 v1 스냅샷은 바꾸지 않고
그 위에 얹는다. 그래서 v1 결과·기준 SHA에 영향이 없다. 평가는 v1과 같은 `tools/evaluate`라 숫자를 바로 비교할 수 있다.

## 자료

v1 스냅샷(`fv-snap-20261031-v1`)은 그대로 쓰고, 옆에 추가 자료 폴더를 만든다. **팀 모두 같은 정제본을 쓴다.**

| 폴더 | 용도 | manifest SHA-256 |
| --- | --- | --- |
| `fv-v2-extra-20261031` | 원본 추출본(가락 API·ASOS 값 그대로). 정제본을 만드는 입력. PR #42 첫 결과는 이 판 | `5bc051c3…324055a` |
| `fv-v2-extra-20261031-r2` | **정제본 — 모든 v2 실험의 입력**(`run_pooled` 기본값) | `b23ca484…7b6acc` |

정제본은 원본에서 반입량 오입력 의심값의 `ton`만 빈 값으로 바꾼 것이다(그 외 파일·글자는 동일). 뺀 값은
`garak_excluded.csv`에, 규칙(직전 20개 반입일 중앙값의 8배 초과, 직전 값 10개 이상일 때만)과 원본 manifest
SHA-256은 정제본 `manifest.json`의 `cleaning`·`derived_from`에 남는다. 현재 5건: 무 2021-11-26(14,762톤),
깐마늘 2021-04-23·08-09·08-26·09-15. 2026-11-16 가락 API 재조회로 원본 값임을 확인했다(한 도매법인 값만 튐).
직접 CSV를 읽는 코드도 **빈 `ton` = 결측(NaN)**, 자료 기간 안에서 행이 없는 날(일요일 등) = 0톤으로 읽어야 같은 자료가 된다.

| 파일 | 내용 | 기간 |
| --- | --- | --- |
| `asos_station_daily.csv` | 품목 주산지 ASOS 관측소 일자료(평균·최저·최고기온, 강수, 습도, 일조) | 2016-01 ~ 2026-10-31 |
| `garak_arrivals_daily.csv` | 가락시장 경매 후 반입물량(톤), 5개 품목 | 2021-01 ~ 2026-10-31 |
| `item_station.csv` | 품목 → 주산지 관측소(`stations.py`, **팀 검토 대상**) | |
| `garak_excluded.csv` | (정제본만) 뺀 반입량: 날짜·품목·원래 톤·직전 중앙값·배수 | |

```powershell
# 스냅샷 담당(공유 DB 보유자) — v1 스냅샷이 data/snapshots/ 에 있어야 함
uv run --extra prices python -m model_comparison.v2.snapshot export --garak ..\garak_arrivals.jsonl
uv run python -m model_comparison.v2.snapshot clean          # 원본 → 정제본(-r2)
# 받는 사람: 정제본을 data/snapshots/fv-v2-extra-20261031-r2/ 에 풀고, manifest SHA-256이 위 표와 같은지 확인
uv run python -m model_comparison.v2.snapshot check
```

## 특징 (한 표본 = 계열 × 기준일 d × 시점 h)

| 묶음 | 개수 | 내용 | 이용 시점 |
| --- | --- | --- | --- |
| v1 기본 | 15 | 가격 이력·달력 | d |
| v1 §5.2 묶음 | 최대 17 | 상대 시장, 전국 기상, 명절, 환율, 생산량 | d−1 / 목표일 / 공개일 |
| `WEATHER_ANOM` | 26 | 주산지 날씨의 평년(지난 1~5년 같은 날) 대비 편차, 과거 13개 4주 블록 | d−1 |
| `ORIGIN_WEATHER` | 130 | 주산지 평균 날씨: 과거 52주 각 주의 평균기온·강수합 + 과거 13개 4주 블록의 최저·최고기온 | d−1 |
| `GARAK` | 10 | 반입량 과거 8주 각 주 합, 최근 7·28일 전년 대비 | d−1 |
| `CROSS_ITEM` | 10 | 다른 품목(같은 시장) 가격 7·28일 변화율 | d−1 |
| `SERIES_ID` | 6 | 품목 원핫 + 도매 여부 | — |

- "며칠 / 몇 주 / 몇 달 뒤 영향"을 사람이 정하지 않고, 52주 이력을 모두 주어 모델이 찾게 한다.
- 값이 없으면 NaN(반입량은 2021년 이전, 자료 기간 안의 일요일 등 경매 없는 날은 0톤).
- 정제본의 빈 반입량(오입력 의심값)은 NaN. 판정은 직전 값만 써서 시점 규칙을 지킨다.
- 시점 규칙 테스트: d일과 그 뒤 날씨·반입량을 지워도 기준일 d 특징이 같음(`tests/test_v2.py`).

## 통합 학습

`run_pooled.py`가 v1과 같은 기준일·주 1회 재학습으로, 매번 **10개 계열 표본을 한 모델이** 학습한다(표본 약 8만 개).
가격 수준이 계열마다 다르므로 대상은 변화율, 가격 수준 특징은 current 대비 비율로 바꾼다(`models.py`).

```powershell
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/all.json --origins tune
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/all.json   # 검증 전체
```

| 설정 | 내용 |
| --- | --- |
| `v1feat.json` | 통합 학습 + v1에서 효과 있던 묶음(MARKET·전국 기상·명절)만 — 통합 학습 자체의 효과 |
| `all.json` | 모든 자료 |
| `no_ow.json`, `no_garak.json`, `no_cross.json` | 모든 자료에서 하나씩 빼기 — 무엇이 기여했는지 |
| `v1feat_garak.json`, `v1feat_cross.json`, `v1feat_anom.json` | v1 효과 묶음에 하나씩 더하기 |

첫 결과는 [RESULTS.md](RESULTS.md).

결과: `experiments_v2/<설정>-<기준일 목록>-날짜-번호/` (`importance.json`에 특징 중요도). v1 CI 검사 대상이 아니다.
최종 시험 기준일은 쓰지 않는다(팀 합의 후 별도).
