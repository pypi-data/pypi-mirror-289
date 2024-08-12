from ..sms import aliyun

ali = aliyun.AliyunSms(
    app_key='LTAI4GBCfDWKReiSaDNQ3GX3',
    secret_key='sk-vfpMz5HOxZWbVOsc5c1G1YS2bhD3zA3B32EF3585811EF9A1EB61E393DC850'
)
ali.send(
    mobile='17720089779',
    config={"sign": "AI社区"},
    template_id='SMS_471245350'
)