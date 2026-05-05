import math

def compute_features(data, amount_mean, amount_std):

    hour = int((data.Time // 3600) % 24)
    hour_sin = math.sin(2 * math.pi * hour / 24)
    hour_cos = math.cos(2 * math.pi * hour / 24)

    amount_log = math.log1p(data.Amount)
    amount_z = (data.Amount - amount_mean) / amount_std
    small_amount = int(data.Amount < 10)

    time_diff = 0

    features = [
        data.V1, data.V2, data.V3, data.V4, data.V5, data.V6,
        data.V7, data.V8, data.V9, data.V10,
        data.V11, data.V12, data.V13, data.V14, data.V15,
        data.V16, data.V17, data.V18, data.V19, data.V20,
        data.V21, data.V22, data.V23, data.V24, data.V25,
        data.V26, data.V27, data.V28,
        data.Amount,
        hour, hour_sin, hour_cos,
        amount_log, amount_z, small_amount, time_diff
    ]

    return features