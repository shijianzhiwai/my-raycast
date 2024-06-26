#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Clipboard Replacement
# @raycast.mode silent
# @raycast.packageName Replace

import subprocess
import re
import traceback

try:
    # 获取剪切板内容
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    data = p.communicate()[0].decode().strip()

    # 替换换行符为逗号
    data = re.sub(r'\n', "','", data)

    # 在前后添加单引号
    data = "'" + data + "'"

    # 将处理后的内容写回剪切板
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data.encode())
    
except Exception as e:
    # 将捕获到的异常和堆栈信息写入文件
    with open('/Users/xuxu/Github/my-raycast/cp_error.log', 'w') as f:
        f.write('Caught exception:\n')
        f.write(str(e) + '\n')
        f.write('Traceback:\n')
        traceback.print_exc(file=f)