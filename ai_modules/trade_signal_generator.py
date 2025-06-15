def generate_trade_signals(bias, ict_signals, fvg_zones, breaker_blocks, price_actions):
    signals = []
    if bias == "صعودي":
        for fvg in fvg_zones:
            if fvg['type'] == 'bullish':
                signals.append({'type': 'buy', 'reason': 'FVG صاعد مع تحيز صاعد'})
    elif bias == "هبوطي":
        for fvg in fvg_zones:
            if fvg['type'] == 'bearish':
                signals.append({'type': 'sell', 'reason': 'FVG هابط مع تحيز هابط'})
    # إضافة تحقق من breaker blocks وict_signals وprice_actions
    # لتصفية وإعطاء ثقة أعلى
    return signals
