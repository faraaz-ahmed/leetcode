/*
tsc index.ts
node index.js
*/

const executeGitCommand: any = (command: string): string =>
	require('child_process')
		.execSync(command)
		.toString()
		.trim();

const getLatestCommit = (): string => executeGitCommand('git rev-parse HEAD');

const getCommitByIndex = (index: number): string => executeGitCommand(`git rev-parse HEAD~${index}`);

const getFileDiff = (sha1: number, sha2: number): string => executeGitCommand(`git diff --name-only HEAD~${sha1} HEAD~${sha2}`);

const getLastProcessedCommit = (): string => {
	/**
	 * gets the last processed commit from ComputeService.
	 */
	return '';
};

const updateLastProcessedCommit = (): string => {
	/**
	 * updates the last processed commit from ComputeService.
	 */

	return '';
};

const getCommitIndex = (commitSHA: string, limit: number = 10): number => {
	let index = 0;
	while(limit) {
		if (getCommitByIndex(index) == commitSHA) {
			return index;
		}
		limit -= 1;
		index += 1;
	}
	return 0;
};

const getFilesFromLastProcessedCommit = (): string => {
	return getFileDiff(0, getCommitIndex(getLastProcessedCommit()));
};
