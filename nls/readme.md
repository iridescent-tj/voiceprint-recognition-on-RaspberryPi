1. ### 安装依赖。

   在该目录使用如下命令安装依赖：

   ```python
   python -m pip install -r requirements.txt
   ```

2. ### 安装SDK。

   依赖安装完成后使用如下命令安装SDK：

   ```python
   python -m pip install .
   ```

3. ### 运行。

   ```python
   python run.py
   ```



默认使用 tests/tts_test.pcm，可相应修改run.py中multiruntest函数来改变测试音频

`def multiruntest(num=1):`

  `for i in range(0, num):`

​    `name = "thread" + str(i)`

​    `t = TestSr(name, "tests/tts_test.pcm")`

​    `t.start()`
