# Ridge v1 버전 매니페스트

기록 시각: 2026-11-11T10:21:42+09:00
- Git SHA: `9e73e593738267c3779a9199b1256f2a93d860db`. Git 작업은 읽기만 수행했으며 Ridge 소스는 미커밋 상태이므로 소스 해시를 함께 사용한다.
- 스냅샷 ID: `fv-snap-20261031-v1`; manifest SHA-256: `3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0`.
- 공식 실행 ID: `ridge-p1-20261111-07`; config ID: `bfc463b0`; phase=p1; origin_list=validation; Alpha=10.
- 원본 실행 폴더: `runs/ridge-p1-20261111-07`. 실행 시작 2026-11-11T10:21:18+09:00, 종료 2026-11-11T10:21:42+09:00.
- 실행 명령: `C:\FoodValue_was\.venv\Scripts\python.exe -B -u -m tools.run_backtest --config model_comparison/ridge/config_alpha_10.json --phase p1 --origins validation --snapshot data/snapshots/fv-snap-20261031-v1 --out runs --experiment-id ridge-p1-20261111-07 --where local --tuning-log runs/ridge-p1-tuning.csv`
- 모델 소스 SHA-256: `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f`. Trial 04 model_source.py와 일치한다.
- 원본 환경 정보 및 패키지 목록은 신규 실행 environment.txt에 있다. 6개 튜닝 행은 신규 실행 tuning_log.csv에 복사했고 기존 CSV는 변경하지 않았다.
- final_config.json은 config_alpha_10.json의 바이트 단위 사본이다. 실행 메타데이터를 포함한 config는 원본 실행 폴더의 config.json에 별도 보존한다.

| 구분 | 실행 ID | 설정 ID | Alpha | policy MAPE % | metrics SHA-256 |
|---|---|---|---:|---:|---|
| tune 01 | ridge-p1-20261111-01 | eeccea32 | 1.0 | 4.789801 | 7dde04b743dc65357b9e6346e58f8848f641057a99d6def2940abc247fdb8119 |
| tune 02 | ridge-p1-20261111-02 | 5c11ea5c | 0.1 | 4.797184 | 80f67fa4df61ad9036019075856fbd0c89b793d4431cfc9fff95b55ccf4af7ea |
| tune 03 | ridge-p1-20261111-03 | a7cb6b1b | 0.01 | 4.798315 | abcc83f0c02244ebc4992c2a13256c1df8b29d8442d0ce85e01450454f18b52c |
| tune 04 | ridge-p1-20261111-04 | bfc463b0 | 10 | 4.785119 | d0f5821d2f6d0a8d8a41d176cb1dab81c4cc1e7dcd57ba5c73a5d22d17736471 |
| tune 05 | ridge-p1-20261111-05 | 33af5014 | 100 | 5.039178 | 5ebc13b958d16a53fe5ffa0c0f94e13bdb147948b300375f5ce2d1a1a084045c |
| tune 06 | ridge-p1-20261111-06 | 9ef98252 | 1000 | 5.483619 | 681d61e28425f0da2b1d63c835503622f5e786a4584b9d865eda58105f1ee25a |
| 공식 Validation | ridge-p1-20261111-07 | bfc463b0 | 10 | 5.060471 | 9c3e399dc7dc882b1e1e051e7ddf4a608a928234de79ef1e4f1e4f4c24535902 |

## 주요 파일 SHA-256 및 원본 경로

경로는 저장소 루트 기준이다. 복사본은 해당 원본 경로와 SHA-256으로 추적한다. 원본 파일은 이동하거나 수정하지 않았다.

| 경로 | SHA-256 |
|---|---|
| `data/snapshots/fv-snap-20261031-v1/calendar_day.csv` | `7813e3adf688beebd6dd8913fdbadc8c1e6ccf5ef93f07f01e43047cfb6e2b14` |
| `data/snapshots/fv-snap-20261031-v1/calendar_event.csv` | `b8f83919ca5bd30f47c59eb7eba99df07835e6649dd299920dd75d3baccf748d` |
| `data/snapshots/fv-snap-20261031-v1/exchange_rate_daily.csv` | `bea5c29537651da76e9b5dfc2edb7373358ba5e642ac86545193e67b326964bd` |
| `data/snapshots/fv-snap-20261031-v1/item_production.csv` | `2075f6417801d6f020e55e40dcf255ea5d3234765d2adebd9041e9e2def26c43` |
| `data/snapshots/fv-snap-20261031-v1/manifest.json` | `3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0` |
| `data/snapshots/fv-snap-20261031-v1/origins_test.csv` | `47672445e79987ed6c83411386dbf531c18641ff7c4bd68d7424b88f60b91c7f` |
| `data/snapshots/fv-snap-20261031-v1/origins_tune.csv` | `fc5c91d5303dc1d162e09978495e11a7c16413f652faee1412d91f6a4a4eea5e` |
| `data/snapshots/fv-snap-20261031-v1/origins_validation.csv` | `a52f4ed460c60781b37659f3c049d1af17cb985f0eb4e0fbe9d891c37709c549` |
| `data/snapshots/fv-snap-20261031-v1/price_daily.csv` | `eecf9cc6546cf7aad06d820cca890af62b8570461e1bd10117d9a255f640dc4f` |
| `data/snapshots/fv-snap-20261031-v1/price_daily_kind.csv` | `6e75f649b2f4de89d880c5dbdd74c953dd568bab16c203d27cebac330b9203ea` |
| `data/snapshots/fv-snap-20261031-v1/price_daily_merged.csv` | `3d06c0bd68dca35df92e964be89fb612bf54edc4b1cae99b4b57dd0806f64b92` |
| `data/snapshots/fv-snap-20261031-v1/price_series.csv` | `676c84c8a2a6c5f590e1f3327011b5338d7b50ef52e75c3a7506202edb6498a1` |
| `data/snapshots/fv-snap-20261031-v1/weather_daily.csv` | `d902550775e2e3a9cb60a05c14563c8b0f980734fe72a72197d5e436d871d0f8` |
| `model_comparison/MODEL_TRAINING_STANDARD.md` | `6c7a7b0b6417ed59b8aa0be0edaebe91f51f6ae477dbc217d65d8c1a79771aec` |
| `model_comparison/MODEL_TRAINING_TEAM_CONVENTIONS.md` | `4b71d309b2d2f77a58c6d7e13550b0b362ce4ba0654e264f66865b1c160c6cd8` |
| `model_comparison/ridge/config_alpha_10.json` | `f28af6b4af86183524a638bde1d2d9734ca70d8bf74392fa4dd4ca61511bc1cd` |
| `model_comparison/ridge/experiments/experiment_summary.md` | `5632b0dc670a9bb29ac96158cbb6b12a20f95903ce5f564a30ea18dbb84f78a1` |
| `model_comparison/ridge/experiments/ridge_v1.md` | `7969fbe7f9f6c9c798f4c4465ef0f39af4b606846a3fd70527c7d98f46ad44e2` |
| `model_comparison/ridge/experiments/v1/audit/archive_script.py` | `594efe02e89cd11299573db4c43cae5b046182fd498288cf157db858238f0686` |
| `model_comparison/ridge/experiments/v1/audit/before.json` | `16af07e75b79e71a12f68ed2fc0b1f90dffd604f040fb63ea794ddb81e30d90f` |
| `model_comparison/ridge/experiments/v1/audit/console.log` | `aff34bd2c24fb1c44abc08a968faed2a727e0e826f0bd12e576ae280aa0f220f` |
| `model_comparison/ridge/experiments/v1/audit/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `model_comparison/ridge/experiments/v1/audit/snapshot_check.log` | `8bcbc12d33ca6ae81b5bb4e8a2c8cf03307be6820f10b8fa046dc37ceb911696` |
| `model_comparison/ridge/experiments/v1/audit/validation_finished.json` | `7f074419d04fab935e0d1709e22dd2eeeb5cb9a858e84d162a40de65647c1034` |
| `model_comparison/ridge/experiments/v1/audit/validation_started.json` | `d1e2eca2bec9aa346a82b2ce86c6f6ea959a8bd5a273d3cb33528d533a3ed0d7` |
| `model_comparison/ridge/experiments/v1/experiment_summary.md` | `cf3f560bf74172847fd41f010e935c5848a3e71d74e7eacc40a74b4835f4f94e` |
| `model_comparison/ridge/experiments/v1/final_config.json` | `f28af6b4af86183524a638bde1d2d9734ca70d8bf74392fa4dd4ca61511bc1cd` |
| `model_comparison/ridge/experiments/v1/ridge_v1.md` | `b6479fea6d61eecc3ecc682cd5536d057e43d4bc470f1283c6af0bde051ac180` |
| `model_comparison/ridge/model.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `model_comparison/ridge/tune_p1.py` | `fabd4dfbdf12f5050dd682c56be5faf497bb6bb82175ac4fbeb3e2bfc0da4792` |
| `model_comparison/ridge/validate_and_archive_v1.py` | `594efe02e89cd11299573db4c43cae5b046182fd498288cf157db858238f0686` |
| `model_comparison/ridge/verify_p1.py` | `eb3cd643a3e8b937599471a2cada76b649224dccab8a0aec9f4e715ee17596a4` |
| `pyproject.toml` | `33c0cea4207e0c6ad3b905aa38aaa4e64d6b8b3a0432046a150def007b3b47ab` |
| `runs/ridge-p1-20261111-01/config.json` | `b1076c88cd773c87c700e067f7b68097f46b97c0025c99ce558b8c4d85d17041` |
| `runs/ridge-p1-20261111-01/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-01/metrics.json` | `7dde04b743dc65357b9e6346e58f8848f641057a99d6def2940abc247fdb8119` |
| `runs/ridge-p1-20261111-01/predictions.csv` | `8bc7a8caa2bae710eb3c348dcfd520132eb1752a7618717d68838402b97459de` |
| `runs/ridge-p1-20261111-01/run.log` | `ec1331767e6d4fcb1cabff2d544bffc05190205190cfbd08b1b6b449f3d6fb15` |
| `runs/ridge-p1-20261111-01/tuning_log.csv` | `6bd15a2ca4e50cb4034fa5ee3111d737382b0ebf57d73929a550e6ddcd12245c` |
| `runs/ridge-p1-20261111-02/config.json` | `371cac7e08496abbd418a0d22a0e877a69c994aaa212e950c802a02e67a290a7` |
| `runs/ridge-p1-20261111-02/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-02/metrics.json` | `80f67fa4df61ad9036019075856fbd0c89b793d4431cfc9fff95b55ccf4af7ea` |
| `runs/ridge-p1-20261111-02/predictions.csv` | `aa838a145bc36a5c20c5c4ce12bcb026fb6688db7cc371e7b9ff09accc687a33` |
| `runs/ridge-p1-20261111-02/run.log` | `eed36bcf90fae998abeaff8a04d3047e52ae799e41e58995019d2090ca0fe7b0` |
| `runs/ridge-p1-20261111-02/tuning_log.csv` | `6bd15a2ca4e50cb4034fa5ee3111d737382b0ebf57d73929a550e6ddcd12245c` |
| `runs/ridge-p1-20261111-03/config.json` | `8ba9422f70bae425fc0947d2a4e7c1e0e9ec6ae95aeea9111bbfd0417c792f21` |
| `runs/ridge-p1-20261111-03/console.log` | `72a3d093b8b445ce066163da24d72e51c4631dec33c9cd011f2cb2c88921bec5` |
| `runs/ridge-p1-20261111-03/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-03/invocation.json` | `ad99fe81b7124a983deea33dad40180132b8fed1512d90c50d09d79fad30895c` |
| `runs/ridge-p1-20261111-03/metrics.json` | `abcc83f0c02244ebc4992c2a13256c1df8b29d8442d0ce85e01450454f18b52c` |
| `runs/ridge-p1-20261111-03/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `runs/ridge-p1-20261111-03/predictions.csv` | `ec2270a1c94863468f7145a1e3c83fa7123329c09fff49d1bd82184dbe32dc57` |
| `runs/ridge-p1-20261111-03/run.log` | `c3a3eb0214796f28ec0f75b34b5f19ad3899f7415336ad70f8a84c0789832bc9` |
| `runs/ridge-p1-20261111-03/tuning_log.csv` | `8fc55ba1628c693955ca78bdedb0b5b74c9fcf684bd5e9008edfb7df7649b2c9` |
| `runs/ridge-p1-20261111-04/config.json` | `14d1cd67253ac55c83f9648d06454cafa93c57d1adad3d569770339fcb0fe88e` |
| `runs/ridge-p1-20261111-04/console.log` | `0901115b613b4261340337e5bb24636c1ce45736d9d628da35039ec30fc1f0b2` |
| `runs/ridge-p1-20261111-04/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-04/invocation.json` | `674dd86a30a65cf487dc45c99c4715973de596edc488a57ac40d81cbda858299` |
| `runs/ridge-p1-20261111-04/metrics.json` | `d0f5821d2f6d0a8d8a41d176cb1dab81c4cc1e7dcd57ba5c73a5d22d17736471` |
| `runs/ridge-p1-20261111-04/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `runs/ridge-p1-20261111-04/predictions.csv` | `29158a4ea7013378ab19c92fa2bee84cbc6ceebe80e0776d5da0d7b2a6c5492f` |
| `runs/ridge-p1-20261111-04/run.log` | `6c118a91541cd2f48c5845ce81535eb765ff49de2185a6a6cbf974d05ff0503d` |
| `runs/ridge-p1-20261111-04/tuning_log.csv` | `a4e12c8c6d3173b349ca5bd5c072dcee30c471db5bf665ecbc0c7c526cd8671c` |
| `runs/ridge-p1-20261111-05/config.json` | `91c56d7c1cc253823c0d91b7b36f1e41e34f4f9273d25160dd170e0e188b8dc4` |
| `runs/ridge-p1-20261111-05/console.log` | `9ecef70bec66780ef659dba68a159f2d80ee5783457b46d6dfc84de85e1a3238` |
| `runs/ridge-p1-20261111-05/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-05/invocation.json` | `abba24068992ebe9c7447560a450feedfa10acf4a0743508a4dee4d0b78dc21a` |
| `runs/ridge-p1-20261111-05/metrics.json` | `5ebc13b958d16a53fe5ffa0c0f94e13bdb147948b300375f5ce2d1a1a084045c` |
| `runs/ridge-p1-20261111-05/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `runs/ridge-p1-20261111-05/predictions.csv` | `269db4c87cbf1a29567d1235fddab1b11ac883c97918ac0cd198797abd9ef614` |
| `runs/ridge-p1-20261111-05/run.log` | `75ac10f00b29dbb18b8fa83fa324181ad4ef1557ab7df87027f7e01f45f8281b` |
| `runs/ridge-p1-20261111-05/tuning_log.csv` | `f4954ffd27f4850b4dcdac3b9076533cdecfdaa2d8f9d115e524f8f558e4b532` |
| `runs/ridge-p1-20261111-06/config.json` | `68ccd09937e5d764d133a5a0d64fcbde2338cf3e8adebbfae96ad992daa60d32` |
| `runs/ridge-p1-20261111-06/console.log` | `f2d1a08c1b5e4c21fce6418b5f0fc963f8ae47495286b5e2e758685b3ebfa473` |
| `runs/ridge-p1-20261111-06/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-06/invocation.json` | `383b3339f832e70d44188952b3a431217c6165def1d1fb03a220c397f70bfb75` |
| `runs/ridge-p1-20261111-06/metrics.json` | `681d61e28425f0da2b1d63c835503622f5e786a4584b9d865eda58105f1ee25a` |
| `runs/ridge-p1-20261111-06/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `runs/ridge-p1-20261111-06/predictions.csv` | `9c1a16e77a72cdab3b9b75add38384a2a64c2d99cf921bc41607c4cbca33db99` |
| `runs/ridge-p1-20261111-06/run.log` | `7172911db4232a6c932f862a69162ece899ab7252328fcd879241aded277498b` |
| `runs/ridge-p1-20261111-06/tuning_log.csv` | `b2621249632fa36d62c3bbfea58d37840194f38d3997ee0bd00677e0caafb89d` |
| `runs/ridge-p1-20261111-07/config.json` | `6a9b547da766ec0750f801e3a327ec459a792b314d5b52e1465843bd4c06219e` |
| `runs/ridge-p1-20261111-07/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-p1-20261111-07/invocation.json` | `7f074419d04fab935e0d1709e22dd2eeeb5cb9a858e84d162a40de65647c1034` |
| `runs/ridge-p1-20261111-07/metrics.json` | `9c3e399dc7dc882b1e1e051e7ddf4a608a928234de79ef1e4f1e4f4c24535902` |
| `runs/ridge-p1-20261111-07/model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `runs/ridge-p1-20261111-07/predictions.csv` | `1e72a16dcea61989a376b32fb8c5d3854b9f6319f2ffe8c0c9ebdea41427199b` |
| `runs/ridge-p1-20261111-07/run.log` | `32693ae628e5af9b8c7238bf610cc025aaa1281a30882a88d0db7b09a4e423e0` |
| `runs/ridge-p1-20261111-07/tuning_log.csv` | `b7081be0704acca04d2481f589cec4738dee9e349bedc31fa9e0a714593cf5b3` |
| `runs/ridge-p1-tuning.csv` | `b7081be0704acca04d2481f589cec4738dee9e349bedc31fa9e0a714593cf5b3` |
| `runs/ridge-smoke-20261111-01/config.json` | `ce8f54d717010af4b4b6a863582a0c77fd807b3c9cb92b6334476ebe956fbc29` |
| `runs/ridge-smoke-20261111-01/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-smoke-20261111-01/metrics.json` | `9d88d589aae24b5a42f87cf0a682a2ad8a1925cdbd3b9a0a992442efac02287a` |
| `runs/ridge-smoke-20261111-01/predictions.csv` | `4d9bd6e457dad23e5755c84c9f867885d9f9424e1bf0a592d3341df551fc8f14` |
| `runs/ridge-smoke-20261111-01/run.log` | `a3b438cb4d96abc0dbaed6f7548776b769ca36e7f235b42387d47f2e9c6d92b2` |
| `runs/ridge-smoke-20261111-01/tuning_log.csv` | `6bd15a2ca4e50cb4034fa5ee3111d737382b0ebf57d73929a550e6ddcd12245c` |
| `runs/ridge-smoke-20261111-02/config.json` | `974efd0723118e204caac5373a4892f749a016ee1ef8b0f4fb16fdc0197764c1` |
| `runs/ridge-smoke-20261111-02/environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `runs/ridge-smoke-20261111-02/metrics.json` | `1c0f298a0e7d7167ba36782300a8304af83e18933dc3f272f2e6649c4bf7151e` |
| `runs/ridge-smoke-20261111-02/predictions.csv` | `a572e0d8897d5034e6edec661ca49d3dd98df8145548c211702890b000dc1212` |
| `runs/ridge-smoke-20261111-02/run.log` | `8dd434c64d4468238bc18d13631a615a87d94719974da9def5a3811352b48e24` |
| `runs/ridge-smoke-20261111-02/tuning_log.csv` | `6bd15a2ca4e50cb4034fa5ee3111d737382b0ebf57d73929a550e6ddcd12245c` |
| `tools/__init__.py` | `8f355d39ac44cdba5f159287fdfc4e20a628b76396d0af0788adec7cb4a77a39` |
| `tools/baselines.py` | `c522a33663f4a93dcffdf75c58d709f6ad6b1b37449a579b4e455470325648f8` |
| `tools/check_snapshot.py` | `5edc4d0aec3b531570b210adca10aec44a03d74ccafd4a89be55c7ef07503eb4` |
| `tools/evaluate.py` | `9434b9ef1d5313cbd1b2093ec67cf5cc635f7503a77dcd6e631e8d0af8038f63` |
| `tools/export_snapshot.py` | `e3dc3cdf82e1f8e2383eea1365d8f2764227e2dcceae6353b28e044d965d9164` |
| `tools/loader.py` | `e9eebcbec01194611638ed3f6bfb0e16382bbada6ddfef2153aa11955e97cb2a` |
| `tools/origins.py` | `23610d2a8263efb967ee804977fee9a8f0f236b0e3b2507e7e39978b95ebfc12` |
| `tools/run_backtest.py` | `893475a6847a97afe0cdc2f85a4ecaae862336976da5460559b0a32e2a67a08e` |
| `tools/runtime.py` | `682274274f0a9e92382320f351e8c560ad0bd621683f688493494718e8919273` |
| `tools/snapshot.py` | `817b63cb2c1fb8a619a8f0b5f42fcac907310d28a9fcc4ae4812b29ea38304ee` |
| `tools/standard.py` | `a773a1be40fbd6337abe3ab701174bb92b23e646b4c58020a473ac5ca1792d28` |
| `tools/validate_experiment.py` | `c2ae675e10aee932af2aba3b9195978419482ecbe818755ad032a2d31dddbe6a` |
| `uv.lock` | `577fa2be7b700995b4f3c9d368b7487cae2ed8f6e54ad1e15fa8393cfe799809` |

## 무결성 검증

audit/before.json은 작업 전 기존 파일의 해시 목록이다. audit/verification.json은 기존 원본 불변, 신규 파일 허용 경로, Validation 전체 격자, 모델·설정 동일성, 공식 관문 일치 여부와 이 매니페스트의 최종 SHA-256을 기록한다.
매니페스트 자기 자신 및 나중에 작성하는 verification.json의 해시는 위 표에서 제외하여 순환 참조를 피했다. 기존 자동화 artifact_manifest.csv는 당시 작업의 목록이며 이번 v1 추가 파일 때문에 재작성하지 않았다.
