# Ridge p2 전체 Validation 실행 결과 — 2026-11-12

CONTROL, 단독 5개, 조건부 MARKET+PRODUCTION 조합을 실제로 실행했다. 전체 실행 상태는 COMPLETED다. 공식 Test와 추가 튜닝은 실행하지 않았다.

| 실험 | 실행 ID | Policy Macro MAPE (%) | p1 대비 상대 개선 (%) |
|---|---|---:|---:|
| p1 기준선 | ridge-p1-20261111-07 | 5.060471 | 0 |
| CONTROL | ridge-p2-20261112-01 | 5.060471 | 0 |
| MARKET | ridge-p2-20261112-02 | **4.940629** | **2.368199** |
| NATIONAL_WEATHER | ridge-p2-20261112-03 | 5.143822 | -1.647100 |
| EVENT | ridge-p2-20261112-04 | 5.200425 | -2.765632 |
| MACRO | ridge-p2-20261112-05 | 5.085541 | -0.495408 |
| PRODUCTION | ridge-p2-20261112-06 | 5.043419 | 0.336965 |
| MARKET+PRODUCTION | ridge-p2-20261112-07 | 4.942954 | 2.322254 |

가장 좋은 단독/전체 결과는 MARKET이다. Naive 4.912547%보다 낮아진 실험은 없다. 조합은 MARKET 단독보다 0.002325%p 나빠 생산량 단독의 개선이 조합에 추가 개선으로 이어지지 않았다. 모두 공식 채택 관문 1X·2X·3X·4O·5X이며, 로컬 메모리 계측과 Docker Test 자원 관문은 미확정이다.

CONTROL은 17,080개 예측 행의 저장 원시값(소수 6자리), 최종 가격, 상태 및 오류 코드가 p1과 완전히 동일하다. 평가 대상 11,275점과 정책 입력, 모든 실제 성능 지표도 일치한다. 의도된 실험 ID/config_id와 phase 메타데이터 차이는 명시적으로 분리했다.

- [상세 실행 보고서와 Ridge 해석](session-20261112-retry04/REPORT.md)
- [측정 결과에 근거한 해석과 유지·제외 판단](session-20261112-retry04/INTERPRETATION.md)
- [전체 분석 JSON](session-20261112-retry04/analysis.json)
- [요약 CSV](session-20261112-retry04/summary.csv)
- [10개 계열 비교 CSV](session-20261112-retry04/series-comparison.csv)
- [전체 특징 이름과 순서](session-20261112-retry04/feature-names.csv)
- [결측률·스케일·계수 안정성 CSV](session-20261112-retry04/feature-diagnostics.csv)
- [최종 주 학습 상관관계 CSV](session-20261112-retry04/latest-correlations.csv)
- [실행별 버전·설정·소스 해시 CSV](session-20261112-retry04/run-provenance.csv)
- [전체 실험 공통 평가 비교](session-20261112-retry04/all-official-comparison.json)
- [CONTROL 최종 검증](session-20261112-retry04/control-parity.json)
- [원본·UTF-8·완료 봉인 무결성 검사](session-20261112-retry04/final-integrity.json)
- [새 산출물 SHA-256 매니페스트](session-20261112-retry04/artifact-manifest.csv)
- [다음 PR 제출 파일 목록](session-20261112-retry04/PR_FILES.md)

공식 산출물은 저장소 루트의 `experiments/ridge-p2-20261112-01/`부터 `-07/`까지, FIT/PREDICT 감사·소스 복사·봉인은 `model_comparison/ridge/experiments/p2/execution/attempts/`에 있다.

실행 전 환경·감사 스크립트 문제로 중단된 4개 세션도 삭제하지 않았다. `session-20261112`, `session-20261112-retry01`, `session-20261112-retry02`, `session-20261112-retry03`의 terminal.json과 로그에서 각각의 종료 원인을 확인할 수 있다. retry03의 CONTROL 오판 기록과 retry04의 수정된 통과 기록을 모두 보존했다. 모델·공통 도구·데이터·평가 기준은 이번 작업에서 수정하지 않았다.

현재 스냅샷만 사용했다. 향후 가락시장·주산지 날씨는 새 스냅샷 ID, 공개시점·지역·품목·단위 검증과 새 CONTROL을 갖춘 별도 실험으로 비교해야 한다.
