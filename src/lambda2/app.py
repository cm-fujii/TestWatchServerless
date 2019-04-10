def lambda_handler(event, context):
    print('lambda2')

    # 強制的にエラー発生させる
    raise NotImplementedError()
