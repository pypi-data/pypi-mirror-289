#%%
from pathlib import Path
from typing import *
import json
import os
import git

class ExpLogger():
    def __init__(self, log_dir: Union[Path, str], git_repo_dir=None):
        """
        Utility to log experiments in a structured way.
        
        log_dir: Path to the directory where logs will be stored. If a relative path, it will be relative to the envvar EXPLOGGER_ROOT if defined, else relative to the CWD
        git_repo_dir: Optional path to the git repository directory. Envvar EXPLOGGER_GITDIR will override this value if defined. Only used to easily retrieve git commit of experiment
        """
        if os.path.isabs(log_dir):
            self.log_dir = Path(log_dir)
        else:
            exp_logger_root = os.environ.get("EXPLOGGER_ROOT")
            if exp_logger_root:
                # If defined, use log_dir relative to EXPLOGGER_ROOT
                self.log_dir = Path(exp_logger_root) / log_dir
            else:
                # If not defined, use log_dir relative to current working directory
                self.log_dir = Path.cwd() / log_dir

        exp_logger_gitdir = os.environ.get("EXPLOGGER_GITDIR")
        print("exp_logger_gitdir", exp_logger_gitdir)
        print("log_dir", self.log_dir)
        if exp_logger_gitdir is not None:
            git_repo_dir = Path(exp_logger_gitdir)
            self.git_repo = git.Repo(git_repo_dir, search_parent_directories=True)
        else:
            if git_repo_dir is None:
                self.git_repo = None
            else:
                self.git_repo = git.Repo(git_repo_dir, search_parent_directories=True)
            
        self.checkpoint_dir = Path(self.log_dir) / "checkpoints"
        self.checkpoint_dir.mkdir(exist_ok=True, parents=True)

        # Read log file with `df = pd.read_json(self.recordsf, lines=True)`
        self.recordsf = self.log_dir / "log.jsonl" # Store logs in json line format
        self.txtlogf = self.log_dir / "log.txt" # Store other logs in a text file
        self.metaf = self.log_dir / "meta.json" # Store a JSON object in a file. Not for serial recording

        self.stdoutf = self.log_dir / "stdout.log"
        self.stderrf = self.log_dir / "stderr.log"

        self._recordsfp = open(self.recordsf, "a+") # Open in an 'append' mode
        self._txtlogfp = open(self.txtlogf, "a+") # Open in an 'append' mode
        self._meta = dict()

    def get_commit_id(self):
        if self.git_repo is not None:
            return self.git_repo.head.commit.hexsha
        else:
            return None

    def __del__(self):
        self._recordsfp.close()
        self._txtlogfp.close()

    def add_meta(self, key, value, force=False):
        """Add a key-value pair to the meta file. Use force=True to overwrite existing keys."""
        if force or key not in self._meta:
            self._meta[key] = value
        else:
            print(f"Key `{key}` already exists in meta. Use force=True to overwrite")

        with open(self.metaf, "w") as fp:
            json.dump(self._meta, fp)

    def log_record(self, obj):
        """Append object as a JSON record at the end of recordsf"""
        json.dump(obj, self._recordsfp)
        self._recordsfp.write("\n")

    def write_file(self, fname, s, mode="a+"):
        """Write string s to file fname in the log directory"""
        with open(self.log_dir / fname, mode) as fp:
            fp.write(s)

    def log_txt(self, s):
        """Append string s a line of the text log file"""
        self._txtlogfp.write(s + "\n")

    def flush(self):
        """Flush the log file, writing all things in buffer to disk"""
        self._recordsfp.flush()
        self._txtlogfp.flush()


#%%
if __name__ == "__main__":
    logger = ExpLogger("logtest")
    code_dir = Path('.')
    logger.save_code(code_dir, exclude_files_or_dirs=["inputs", "outputs"])

    logger.log_txt("Some command")
    logger.log({"test": "this is a test"})
    logger.log({"step": 0})
    logger.log({"end": "end"})
    logger.flush()

    import pandas as pd
    df = pd.read_json(logger.recordsf, lines=True)