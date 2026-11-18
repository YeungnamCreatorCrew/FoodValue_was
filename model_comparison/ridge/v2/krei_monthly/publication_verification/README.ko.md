# 공개 시점·버전 검증 코드

최종 보고서: [PUBLICATION_VERIFICATION_REPORT.ko.md](../PUBLICATION_VERIFICATION_REPORT.ko.md)

정식 실행: `publication_verification/runs/publication_20261117T162601173971Z`

- 최종 PDF 등급: `archive_adjudication/pdf_evidence_grades.json/csv`
- 최종 Tune 사전 진단: `diagnostics_v3/`
- 두 정책의 독립 특징 파일: `diagnostics_v3/STRICT/`, `diagnostics_v3/EXPLORATORY/`
- 무결성: `preservation_before.json`, `preservation_after.json`
- 정책/실제 행 검증: `diagnostics_v3/audit_summary.json`

`diagnostics/`와 `diagnostics_v2/`는 중간 계산이며 최종 결과가 아니다. 첫 초안은 보존 시각을 탐색 경계로 포함하고 62일 상한을 사용했다. 최종 정책은 아카이브 관측 상한과 간접 날짜 경계를 분리하고 연간 정보의 신선도를 민감도로 별도 진단한다. 코드 변경으로 과거 출력을 덮어쓰지 않았다.

`policies.py`는 기존 `asof.py`를 수정하지 않는 STRICT 어댑터와 별도 탐색 정책이다. `policy_training_eligible`은 시점별 STRICT 계약 통과 여부이고 `final_model_approved`는 별도이며 모두 false이다. 과거 전체 해시가 맞더라도 그 보존 시각 이전으로 사용을 소급하지 않는다.

재현 순서: `workspace.py start` → `evidence.py --run <new run> --phase ...` → `classify.py --run ...` → `evidence.py --phase archive-payloads` → `adjudicate_archives.py` → `diagnose.py --output-name diagnostics_v3 --grades <archive_adjudication/pdf_evidence_grades.json>` → `audit_diagnostics.py` → `workspace.py finish` → `write_report.py`. 모두 `python -B`로 실행한다. 네트워크는 별도 승인이 필요할 수 있다. 출력을 이미 존재하는 경로에 다시 쓰면 실패하도록 만들어졌다. 이전 실행을 재수행하거나 중간 결과를 정식 학습 입력으로 쓰지 않는다.

회귀 검사: `python -B -m unittest discover -s model_comparison/ridge/v2/krei_monthly/publication_verification -p test_contracts.py -v`. Ridge 학습, DB 쓰기, Git 쓰기 코드는 없다.
