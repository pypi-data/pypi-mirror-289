import pytest
import json
import pandas as pd
from simple_gpu_queue.explogger import ExpLogger
import git

@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path

@pytest.fixture
def exp_logger(temp_dir):
    return ExpLogger(temp_dir)

def test_init(temp_dir):
    logger = ExpLogger(temp_dir)
    assert logger.log_dir == temp_dir
    assert (temp_dir / "checkpoints").exists()
    assert (temp_dir / "log.jsonl").exists()
    assert (temp_dir / "log.txt").exists()
    logger.add_meta("test_key", "test_value")
    logger.flush()
    assert (temp_dir / "meta.json").exists()

def test_add_meta(exp_logger):
    exp_logger.add_meta("test_key", "test_value")
    with open(exp_logger.metaf, "r") as f:
        meta_data = json.load(f)
    assert meta_data["test_key"] == "test_value"

    # Test overwrite protection
    exp_logger.add_meta("test_key", "new_value")
    with open(exp_logger.metaf, "r") as f:
        meta_data = json.load(f)
    assert meta_data["test_key"] == "test_value"

    # Test force overwrite
    exp_logger.add_meta("test_key", "new_value", force=True)
    with open(exp_logger.metaf, "r") as f:
        meta_data = json.load(f)
    assert meta_data["test_key"] == "new_value"

def test_log_record(exp_logger):
    test_obj = {"test": "record"}
    exp_logger.log_record(test_obj)
    exp_logger.flush()

    df = pd.read_json(exp_logger.recordsf, lines=True)
    assert df.to_dict('records')[0] == test_obj

def test_write_file(exp_logger):
    test_content = "Test content"
    exp_logger.write_file("test.txt", test_content)
    
    with open(exp_logger.log_dir / "test.txt", "r") as f:
        content = f.read()
    assert content == test_content

def test_log_txt(exp_logger):
    test_log = "Test log entry"
    exp_logger.log_txt(test_log)
    exp_logger.flush()

    with open(exp_logger.txtlogf, "r") as f:
        content = f.read().strip()
    assert content == test_log

def test_get_commit_id(temp_dir, monkeypatch):
    class MockRepo:
        class MockHead:
            class MockCommit:
                hexsha = "test_commit_hash"
            commit = MockCommit()
        head = MockHead()

    class MockGit:
        @staticmethod
        def Repo(path, search_parent_directories):
            return MockRepo()

    monkeypatch.setattr("git.Repo", MockGit.Repo)
    
    logger = ExpLogger(temp_dir, git_repo_dir=temp_dir)
    assert logger.get_commit_id() == "test_commit_hash"

def test_env_vars(temp_dir, monkeypatch):
    rootdir = temp_dir / "custom_root"
    gitdir = temp_dir / "custom_git"

    rootdir.mkdir(parents=True, exist_ok=True)
    gitdir.mkdir(parents=True, exist_ok=True)
    repo = git.Repo.init(gitdir)

    monkeypatch.setenv("EXPLOGGER_ROOT", str(rootdir))
    monkeypatch.setenv("EXPLOGGER_GITDIR", str(gitdir))

    logger = ExpLogger("test_log")
    assert logger.log_dir == temp_dir / "custom_root" / "test_log"
    assert isinstance(logger.git_repo, git.Repo)