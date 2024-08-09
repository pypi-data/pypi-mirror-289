class GitLog:

    def __init__(self, raw_log: str):
        self.commits = self._split_raw_log_to_commits(raw_log)

    def _split_raw_log_to_commits(self, raw_log):
        raw_logs_in_lines = raw_log.split('\n')
        commits = []
        commit = ''
        for line in raw_logs_in_lines:
            if line.startswith('commit'):
                if commit:
                    commits.append(commit)
                    commit = ''
            commit += line + '\n'

        return commits
