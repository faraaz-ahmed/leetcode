import { ComputeService } from './ComputeService';
import { FileParser } from './FileParser';

export interface Timestamp {
	timestampId: number;
	timestampName: string;
	timestampContent: string;
	timestamp: string;
}

class SyncService {
	private executeGitCommand(command: string): string {
		return require('child_process').execSync(command).toString().trim();
	}

	private getLatestCommit(): string {
		return this.executeGitCommand('git rev-parse HEAD');
	}

	private getCommitByIndex(index: number): string {
		return this.executeGitCommand(`git rev-parse HEAD~${index}`);
	}

	private getFileDiffByCommitIndex(
		commitIndex1: string,
		commitIndex2: string
	): string {
		return this.executeGitCommand(
			`git diff --name-only HEAD~${commitIndex1} HEAD~${commitIndex2}`
		);
	}

	private getFileDiff(commitSHA1: string, commitSHA2: string): string[] {
		return this.executeGitCommand(
			`git diff --name-only ${commitSHA1} ${commitSHA2}`
		).split('\n');
	}

	private async getLastProcessedCommit(): Promise<string> {
		/**
		 * gets the last processed commit from ComputeService.
		 */
		const computeService = new ComputeService();
		const timestamp = await computeService.getTimestamp();
		if (typeof timestamp === 'string') {
			return timestamp;
		}
		return timestamp.timestampContent;
	}

	private updateLastProcessedCommit(): void {
		/**
		 * updates the last processed commit from ComputeService.
		 */
		// return '';
	}

	private getCommitIndex = (commitSHA: string, limit: number = 10): number => {
		let index = 0;
		while (limit) {
			if (this.getCommitByIndex(index) == commitSHA) {
				return index;
			}
			limit -= 1;
			index += 1;
		}
		return 0;
	};

	private getFolderNames(filePath: string): string {
		return filePath.split('/')[0];
	}

	public async saveProblemsFromLastProcessedCommit(): Promise<string> {
		const lastProcessedCommit = await this.getLastProcessedCommit();
		const latestCommit = this.getLatestCommit();
		const fileParser = new FileParser();
		if (lastProcessedCommit === 'Timestamp Name does not exist.') {
			// process all files and update last processed commit.
			fileParser.saveProblemAndUpdateTimestamp(latestCommit);
		} else {
			// process only the diff and update the last processed commit.
			const folderNames = [
				...new Set(
					this.getFileDiff(lastProcessedCommit, latestCommit).map(
						(path: string): string => this.getFolderNames(path)
					)
				)
			];
			fileParser.saveProblemAndUpdateTimestamp(latestCommit, folderNames);
		}
		return '';
	}
}

new SyncService().saveProblemsFromLastProcessedCommit();

/**
 * Steps to build:

cd SyncService
tsc
node ./dist/index.js

 */

/**
 * TODO:
 * data: {
      timestamp: '2023-05-29T00:21:26.455+0000',
      status: 500,
      error: 'Internal Server Error',
      message: "HV000030: No validator could be found for constraint 'javax.validation.constraints.NotBlank' validating type 'java.lang.Long'. Check configuration for 'topicId'",
      path: '/problem/save'
    }
  }
 */
