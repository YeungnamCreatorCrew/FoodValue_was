"""지표 카드 → 한 줄 요약·칩 문구. 순수 함수. 방향(state)은 카드가 정한 값을 그대로 쓴다."""

POSITION_PHRASE = {'DOWN': '싼 편', 'UP': '비싼 편', 'NEUTRAL': '중간 수준'}
POSITION_LABEL = {'DOWN': '싼 편', 'UP': '비싼 편', 'NEUTRAL': '중간'}
SEASONAL_LABEL = {'DOWN': '싼 편', 'UP': '비싼 편', 'NEUTRAL': '평년 수준', None: '참고'}
LEAD_LABEL = {'UP': '상승 신호', 'DOWN': '하락 신호', 'NEUTRAL': '신호 없음'}
SEASONAL_PHRASE = {'DOWN': '평년보다 싼 편', 'UP': '평년보다 비싼 편', 'NEUTRAL': '평년 수준'}
LEAD_PHRASE = {'UP': '도매가가 크게 올라 앞으로 소매가도 오를 수 있는 신호가 보입니다',
               'DOWN': '도매가가 크게 내려 앞으로 소매가도 내릴 수 있는 신호가 보입니다',
               'NEUTRAL': '당장 가격을 움직일 신호는 보이지 않습니다'}


def topic(name: str) -> str:
    """이름 + 은/는. 한글이 아니면 '은(는)'."""
    last = name[-1]
    if '가' <= last <= '힣':
        return name + ('은' if (ord(last) - 0xAC00) % 28 else '는')
    return name + '은(는)'


def build(name: str, cards: list[dict]) -> dict | None:
    """cards: [{'key','state'}...]. 칩(signals)과 headline. 카드가 없으면 None."""
    by_key = {c['key']: c for c in cards}
    signals = []
    season, lead = by_key.get('SEASONAL'), by_key.get('WHOLESALE_LEAD')
    position = by_key.get('PRICE_POSITION')
    if position:
        signals.append({'key': 'PRICE_POSITION', 'label': '1년 중 위치', 'state': position['state'],
                        'stateLabel': POSITION_LABEL[position['state']]})
    if season:
        signals.append({'key': 'SEASONAL', 'label': '같은 시기 대비', 'state': season['state'],
                        'stateLabel': SEASONAL_LABEL[season['state']]})
    if lead:
        signals.append({'key': 'WHOLESALE_LEAD', 'label': '도매 흐름', 'state': lead['state'],
                        'stateLabel': LEAD_LABEL[lead['state']]})
    if not signals:
        return None
    season_phrase = SEASONAL_PHRASE.get(season['state']) if season else None
    lead_phrase = LEAD_PHRASE[lead['state']] if lead else None
    if season_phrase and lead_phrase:
        headline = f'{topic(name)} 지금 {season_phrase}이고, {lead_phrase}.'
    elif season_phrase:
        headline = f'{topic(name)} 지금 {season_phrase}입니다.'
    elif lead_phrase:
        headline = f'{name}: {lead_phrase}.'
    elif position:
        headline = f'{topic(name)} 지금 최근 1년 가격 중 {POSITION_PHRASE[position["state"]]}입니다.'
    else:
        headline = f'{name}의 같은 시기 가격을 평년과 비교한 참고 지표입니다.'
    return {'headline': headline, 'signals': signals}
