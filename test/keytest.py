import pyotp

# 生成秘钥
def generate_secret_key():
    return pyotp.random_base32()

# 生成OTP
def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

# 验证OTP
def verify_otp(secret_key, otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp)

# 示例
if __name__ == '__main__':
    # 生成秘钥
    secret_key = generate_secret_key()
    secret_key = 'BOHVMYUESMLL7WR5T7DZJNNLBK4CLGYC'
    print('秘钥:', secret_key)

    # 生成OTP
    otp = generate_otp(secret_key)
    print('OTP:', otp)

    # 模拟用户输入的OTP
    user_input = input('请输入OTP进行验证: ')

    # 验证OTP
    if verify_otp(secret_key, user_input):
        print('验证成功')
    else:
        print('验证失败')