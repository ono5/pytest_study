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

## --skip --skipif

テストをスキップできる。


```bash
$ pytest -v XXXX

# スキップした理由を知りたい場合
$ pytest -rs XXXX
```

## -r

指定されたテストの要約情報を pytest の出力に追加する。

```bash
  -r chars              show extra test summary info as specified by chars
                        (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
                        (p)passed, (P)passed with output, (a)all except pP.
                        Warnings are displayed at all times except when
                        --disable-warnings is set
```

# テスト分類

* ユニットテスト
  - 関数やクラスなど、コードのごく一部をチェックするテスト。単体テストとも呼ばれる。

* 結合テスト
  - 複数のクラスやサブシステムなど、ひと回り大きなコードをチェックするテスト。
    ユニットテストより大きく、システムテストより小さい。

* システムテスト
  - テストしているシステム全体をチェックするテスト。エンドツーエンドテストとも呼ばれる。
    システムテストは、可能な限り、エンドユーザー環境に近い環境で行われる。
    
* 機能テスト
  - システムのただ一つの機能をチェックするテスト
 
* 皮下テスト
  - 最終的なエンドユーザーインターフェースに対して実行されるのではなく、表面のすぐ下にある
    インターフェイスに対して実行されるテスト。

# pytest ファイル

* pytest.ini
  - プロジェクト全体の構成情報。プロジェクトに最大一つ用意する(必須ではない)。

* conftest.py
  - pytest によって、ローカルプラグインであると見なされるファイルで、フック関数やフィクスチャを含んでいる場合もある。
  * フック関数
    - pytest の実行プロセスの一部にコードを挿入することで、pytest の動作方法を変更する手段。
  * フィクスチャ
    - テスト関数の前後に実行されるセットアップ関数とティアダウン関数であり、テストに使用されるリソースやデータを表すために使用できる。
    
# pytest assert

[Demo of Python failure reports with pytest](https://docs.pytest.org/en/latest/example/reportingdemo.html)

# テスト関数にマークをつける

テスト関数に @pytest.mark.XXXX のデコレータを付与する。

# テストをパラメーター化する

## デコレータ

@pytest.mark.parametrize('<引数>', <引数値>)

```bash
@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                          Task('wake', 'brian'),
                          Task('breathe', 'BRIAN', True),
                          Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id

```

## テストID

pytest が文字列に変換しやすい型を使用すると、テストIDとしてパラメータの値が使用されるため、
出力が読みやすくなる。

```bash
(env) $ pytest -v test_add_variety.py::test_add_3
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 4 items                                                                                                                                                                                                                      

test_add_variety.py::test_add_3[sleep-None-False] PASSED                                                                                                                                                                         [ 25%]
test_add_variety.py::test_add_3[wake-brian-False] PASSED                                                                                                                                                                         [ 50%]
test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED                                                                                                                                                                       [ 75%]
test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED

# テストID sleep-None-False
$ pytest -v test_add_variety.py::test_add_3[sleep-None-False]
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_3[sleep-None-False] PASSED

# テストID にスペースが含まれている場合は、必ず引用符("")で囲んでください。
$ pytest -v "test_add_variety.py::test_add_3[eat sleep-None-False]"
```

## ids パラメータ
parametrize オプションの ids を使って、テストのデータセットをそれぞれのIDといsて使用する。

```bash
# 引用符がいる
$ pytest -v "test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)]"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_5[Task(exercise,BrIaN,False)] PASSED                                                                                                                                                               [100%]
```

# パラメータのID化
パラメータを id パラメータに渡すとパラメータを識別できる。

```bash
@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    
 $ pytest -v test_add_variety.py::test_add_6
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 3 items                                                                                                                                                                                                                      

test_add_variety.py::test_add_6[just summary] PASSED                                                                                                                                                                             [ 33%]
test_add_variety.py::test_add_6[summary/owner] PASSED                                                                                                                                                                            [ 66%]
test_add_variety.py::test_add_6[summary/owner/done] PASSED                                                                                                                                                                       [100%]

$ pytest -v "test_add_variety.py::test_add_6[just summary]"
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/hono/Desktop/user_auth_with_django/env/bin/python
cachedir: .pytest_cache
rootdir: /Users/hono/Desktop/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 1 item                                                                                                                                                                                                                       

test_add_variety.py::test_add_6[just summary] PASSED  
```
