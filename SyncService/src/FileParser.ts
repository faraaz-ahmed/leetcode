const fs = require('fs');
import { readdirSync } from 'fs';
import { Problem, ComputeService, Topic } from './ComputeService';

import { IGNORE_FOLDERS } from './Constants';

export class FileParser {
	computeService;
	constructor() {
		this.computeService = new ComputeService();
	}
	public async getFileContent(path: string): Promise<string> {
		try {
			return await fs.readFileSync(path, 'utf8');
		} catch (err) {
			console.error(err);
			return err;
		}
	}

	public async getDirectories(source) {
		return readdirSync(source, { withFileTypes: true })
			.filter(
				(dirent) =>
					dirent.isDirectory() && !IGNORE_FOLDERS.includes(dirent.name)
			)
			.map((dirent) => dirent.name);
	}

	private getFileNames(source) {
		try {
			return readdirSync(source, { withFileTypes: true })
				.filter(
					(dirent) =>
						!dirent.isDirectory() &&
						dirent.name.startsWith('lc') &&
						!IGNORE_FOLDERS.includes(dirent.name)
				)
				.map((dirent) => dirent.name);
		} catch (error) {
			console.error(error);
		}
	}

	public getIdFromFileName(fileName: string): number {
		return parseInt(fileName.replace(/[^0-9]/g, ''));
	}

	public async saveTopic(directory: string, retries = 2): Promise<boolean> {
		let isTopicAvailable = false;
		while (!isTopicAvailable && retries >= 0) {
			await this.computeService
				.getTopics()
				.then((topics: Topic[]) => {
					retries -= 1;
					isTopicAvailable =
						Array.isArray(topics) &&
						topics.map((topic) => topic.topicName).includes(directory);
					// console.log(
					// 	'check??',
					// 	isTopicAvailable,
					// 	directory,
					// 	topics.map((topic) => topic.topicName).length,
					// 	topics.map((topic) => topic.topicName).includes(directory)
					// );
					if (!isTopicAvailable) {
						this.computeService
							.saveTopics({ topics: [{ topicName: directory }] })
							.then((response) => {
								// console.log(
								// 	'Successfully saved topic for ',
								// 	directory,
								// 	', with response = ',
								// 	response
								// );
								isTopicAvailable = true;
								// console.log(
								// 	'Successfully saved topic for ',
								// 	directory,
								// 	', with response = '
								// );
							});
					}
				})
				.catch((error) => {
					retries -= 1;
					// console.log(
					// 	'Error while saving topic for =',
					// 	directory,
					// 	'Error =>',
					// 	error
					// );
				});
		}
		return isTopicAvailable;
	}

	private async extractAndSaveProblem(directory: string): Promise<boolean> {
		let processingComplete = true;
		const directoryPath = `../../leetcode/${directory}`;
		this.getFileNames(directoryPath).forEach(async (fileName) => {
			if (!(await this.saveTopic(directory))) {
				processingComplete = false;
			} else {
				const solution = await this.getFileContent(
					`${directoryPath}/${fileName}`
				);
				const problem: Problem = {
					problemId: this.getIdFromFileName(fileName),
					problemName: fileName,
					topicName: directory,
					solution,
					userName: 'alex'
				};
				// console.log('problem ', problem);
				await this.computeService
					.saveProblem(problem)
					.then(
						(response) => console.log('Successfully saved problem', response)
						// console.log('')
					)
					.catch((error) => {
						processingComplete = false;
						// console.log('unable to save for problem = ', problem, error);
					});
			}
		});
		return processingComplete;
	}

	public async saveProblemAndUpdateTimestamp(
		latestCommit: string,
		directoryList: string[] = []
	): Promise<void> {
		(directoryList.length == 0
			? await this.getDirectories('../../leetcode')
			: directoryList.filter(
					(directory) =>
						!IGNORE_FOLDERS.includes(directory) &&
						!IGNORE_FOLDERS.find((ignoredFolder) =>
							directory.includes(ignoredFolder)
						) &&
						!directory.includes('.')
			  )
		).forEach((directory) => {
			// console.log('directory list', directory);
			try {
				this.extractAndSaveProblem(directory).then((response) => {
					if (response) {
						this.computeService.saveCommitTimestamp(latestCommit);
					} else {
						// TO DO: Add rollback logic if processing is incomplete, All or none.
					}
				});
			} catch (error) {
				// console.log(`ERROR: ${error}`);
			}
		});
	}
}

/**
 * Steps to build:

cd SyncService
tsc
node ./dist/FileParser.js

 */

// Example for break in forEach
// const arr: string[] = ['bobby', 'hadz', 'com'];

// const BreakError = {};

// try {
//   arr.forEach((element) => {
//     if (element === 'hadz') {
//       throw BreakError;
//     }
//     console.log(element); // 👉️ bobby
//   });
// } catch (err) {
//   if (err !== BreakError) throw err;
// }
