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