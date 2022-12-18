print("hello, flag system!")

flag = "ChristmasCTF{flag_system_command_flag_system_command}"
key = "h!st0ry"
enc = ""

for i in range(len(flag)):
        enc += chr(ord(flag[i]) ^ ord(key[i % len(key)]))

print(enc)
