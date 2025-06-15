def mmxm_stage_analysis(candles):
    stages = []
    for i in range(3, len(candles)):
        # مثال مبسط لمراحل MMXM
        if candles[i]['close'] > candles[i-1]['high']:
            stages.append({'index': i, 'stage': 'Stage 1'})
        elif candles[i]['close'] < candles[i-1]['low']:
            stages.append({'index': i, 'stage': 'Stage 2'})
        else:
            stages.append({'index': i, 'stage': 'Consolidation'})
    return stages
