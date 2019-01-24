# flake8

```
pytest test_one.py && flake8
```

# pytestの検索

test_xxxx.py xxxx_test.py のファイルを検索する。

# 命名規則

* テストファイルの名前は、test_<something>.py または、<something>_test.py という形式でなければならない
* テストメソッドやテスト関数の名前は test_<something> とう形式でなければならない
* テストクラスの名前は、Test<Something> という形式でなければならない

# テストを一つだけ実行

```bash
pytest -v tasks/test_four.py::test_asdict
```

# pytest オプション

### --help

ヘルプを表示

```bash
python --help
```

### --collect-only

指定したオプションと構成に基づいて時刻されるテストを表示する。

テスト対象一覧。

```bash
$ pytest --collect-only
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
<Module test_one.py>
  <Function test_passing>
<Module test_two.py>
  <Function test_failing>
<Module tasks/test_four.py>
  <Function test_asdict>
  <Function test_replace>
<Module tasks/test_three.py>
  <Function test_defaults>
  <Function test_member_access>
```

## -k EXPRESSION

- k オプションは、実行するテスト関数を、式を使って検索できるようにしたフィルタ。

テストに一意な名前がついている場合は、テストを個別に実行するためのショートカットとしても利用可能。

```bash
# テスト対象を確かめる
$ pytest -k "asdict or defaults" --collect-only
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       
<Module tasks/test_four.py>
  <Function test_asdict>
<Module tasks/test_three.py>
  <Function test_defaults>

# テストする
$ pytest -k "asdict or defaults"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       

tasks/test_four.py .                                                                                                                                                                                                             [ 50%]
tasks/test_three.py .  
``` 

# -m MARKERPR

マーカーは、テスト関数の一部に名前をつけ、それらの関数をまとめて実行できるようにする。

```bash
# run_these_please というマーカーを付与して、実行

 $ pytest -v -m run_these_please
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 4 deselected                                                                                                                                                                                                       

tasks/test_four.py::test_asdict PASSED                                                                                                                                                                                           [ 50%]
tasks/test_three.py::test_member_access PASSED                                                                                                                                                                                   [100%]

# その他のパターン
$ pytest -v -m mark1 and mark2
$ pytest -v -m mark1 and not mark2
$ pytest -v -m mark1 or mark2
```

## -x, --exitfirst

テスト失敗時に、後続のテストが走らないようにする。

```bash
 $ pytest -x
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError
```

## --tb=style

トレースバックのオプション。

```bash
 $ pytest --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..   


 $ pytest --tb=short
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________
test_two.py:2: in test_failing
    assert (1, 2, 3) == (3, 2, 1)
E   assert (1, 2, 3) == (3, 2, 1)
E     At index 0 diff: 1 != 3
E     Use -v to get the full diff

$ pytest --tb=line
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

=============================================================================================================== FAILURES ===============================================================================================================
/Users/hono/Desktop/pytest_code/ch1/test_two.py:2: assert (1, 2, 3) == (3, 2, 1)
```

## --maxfail=num

テストが失敗する数に上限を持たせる。

```bash
$ pytest --maxfail=2 --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..     

$ pytest --maxfail=1 --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      

test_one.py .                                                                                                                                                                                                                    [ 16%]
test_two.py F
```

## -s, --capture=method

テスト実行中に print 文の出力を標準出力に書き出すことができる。

```bash
# Start / End 
pytest -s tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collecting ... -------------Start Test-------------------
-------------End Test-------------------
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py ..


 $ pytest  tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py ..                                                                                                                                                                                                            [100%]
```

## -l, --showlocals

テストが失敗した場合に、そのテストのローカル変数を表示する。

````bash
pytest -l tasks/test_four.py 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 2 items                                                                                                                                                                                                                      

tasks/test_four.py F.                                                                                                                                                                                                            [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_asdict ______________________________________________________________________________________________________________

    @pytest.mark.run_these_please
    def test_asdict():
        """_asdict() should return a dictionary."""
        t_task = Task('do something', 'okken', True, 21)
        t_dict = t_task._asdict()
        expected = {'summary': 'do something',
                    'owner': 'okken',
                    'done': True,
                    'id': 21}
>       assert t_dict != expected
E       AssertionError: assert OrderedDict([('summary', 'do something'), ('owner', 'okken'), ('done', True), ('id', 21)]) != {'done': True, 'id': 21, 'owner': 'okken', 'summary': 'do something'}

expected   = {'done': True, 'id': 21, 'owner': 'okken', 'summary': 'do something'}
t_dict     = OrderedDict([('summary', 'do something'), ('owner', 'okken'), ('done', True), ('id', 21)])
t_task     = Task(summary='do something', owner='okken', done=True, id=21)

tasks/test_four.py:18: AssertionError
````

## --lf, --last-failed

最後に失敗しているテストだけ実行する。

```bash
$ pytest --lf
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 5 deselected                                                                                                                                                                                                       
run-last-failure: rerun previous 1 failure

test_two.py F                                                                                                                                                                                                                    [100%]

=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get the full diff

test_two.py:2: AssertionError

$ pytest --lf --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items / 5 deselected                                                                                                                                                                                                       
run-last-failure: rerun previous 1 failure

test_two.py F   
```

## --ff, --failed-first

最後に失敗したテストを実行ご、残りの成功しているテストを実行する。

```bash
$ pytest --ff --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
run-last-failure: rerun previous 1 failure first

test_two.py F                                                                                                                                                                                                                    [ 16%]
test_one.py .                                                                                                                                                                                                                    [ 33%]
tasks/test_four.py ..                                                                                                                                                                                                            [ 66%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]
```

## -v, --verbose

詳細情報を出力する。

```bash
 $ pytest -v --ff --tb=no
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 6 items                                                                                                                                                                                                                      
run-last-failure: rerun previous 1 failure first

test_two.py::test_failing FAILED                                                                                                                                                                                                 [ 16%]
test_one.py::test_passing PASSED                                                                                                                                                                                                 [ 33%]
tasks/test_four.py::test_asdict PASSED                                                                                                                                                                                           [ 50%]
tasks/test_four.py::test_replace PASSED                                                                                                                                                                                          [ 66%]
tasks/test_three.py::test_defaults PASSED                                                                                                                                                                                        [ 83%]
tasks/test_three.py::test_member_access PASSED  
```

## -q, --quiet

出力される情報が少なくなる。

```bash
 pytest -q
.F....                                                                                                                                                                                                                           [100%]
=============================================================================================================== FAILURES ===============================================================================================================
_____________________________________________________________________________________________________________ test_failing _____________________________________________________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Full diff:
E         - (1, 2, 3)
E         ?  ^     ^
E         + (3, 2, 1)
E         ?  ^     ^

test_two.py:2: AssertionError
1 failed, 5 passed in 0.07 seconds

$ pytest -q --tb=line
.F....                                                                                                                                                                                                                           [100%]
=============================================================================================================== FAILURES ===============================================================================================================
/Users/hono/Desktop/pytest_code/ch1/test_two.py:2: assert (1, 2, 3) == (3, 2, 1)
1 failed, 5 passed in 0.06 seconds
```

## --durations=N

テストが実行された後に、もっとも時間がかかった N 個のテスト/セットアップ/ティアダウンを表示する。

```bash
$ pytest --durations=3 tasks
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/pytest_code/ch1, inifile:
collected 4 items                                                                                                                                                                                                                      

tasks/test_four.py ..                                                                                                                                                                                                            [ 50%]
tasks/test_three.py ..                                                                                                                                                                                                           [100%]

======================================================================================================= slowest 3 test durations =======================================================================================================
0.11s call     tasks/test_four.py::test_asdict

(0.00 durations hidden.  Use -vv to show these durations.)
```




