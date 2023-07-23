"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileParser = void 0;
const fs = require('fs');
const fs_1 = require("fs");
const ComputeService_1 = require("./ComputeService");
const Constants_1 = require("./Constants");
class FileParser {
    constructor() {
        this.computeService = new ComputeService_1.ComputeService();
    }
    async getFileContent(path) {
        try {
            return await fs.readFileSync(path, 'utf8');
        }
        catch (err) {
            console.error(err);
            return err;
        }
    }
    async getDirectories(source) {
        return (0, fs_1.readdirSync)(source, { withFileTypes: true })
            .filter((dirent) => dirent.isDirectory() && !Constants_1.IGNORE_FOLDERS.includes(dirent.name))
            .map((dirent) => dirent.name);
    }
    getFileNames(source) {
        return (0, fs_1.readdirSync)(source, { withFileTypes: true })
            .filter((dirent) => !dirent.isDirectory() &&
            dirent.name.startsWith('lc') &&
            !Constants_1.IGNORE_FOLDERS.includes(dirent.name))
            .map((dirent) => dirent.name);
    }
    getIdFromFileName(fileName) {
        return parseInt(fileName.replace(/[^0-9]/g, ''));
    }
    async saveTopic(directory, retries = 2) {
        let isTopicAvailable = false;
        while (!isTopicAvailable && retries >= 0) {
            await this.computeService
                .getTopics()
                .then((topics) => {
                retries -= 1;
                isTopicAvailable =
                    Array.isArray(topics) &&
                        topics.map((topic) => topic.topicName).includes(directory);
                console.log('check??', isTopicAvailable, directory, topics.map((topic) => topic.topicName).length, topics.map((topic) => topic.topicName).includes(directory));
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
                        console.log('Successfully saved topic for ', directory, ', with response = ');
                    });
                }
            })
                .catch((error) => {
                retries -= 1;
                console.log('Error while saving topic for =', directory, 'Error =>', error);
            });
        }
        return isTopicAvailable;
    }
    async extractAndSaveProblem(directory) {
        let processingComplete = true;
        const directoryPath = `../../leetcode/${directory}`;
        this.getFileNames(directoryPath).forEach(async (fileName) => {
            if (!(await this.saveTopic(directory))) {
                processingComplete = false;
            }
            else {
                const solution = await this.getFileContent(`${directoryPath}/${fileName}`);
                const problem = {
                    problemId: this.getIdFromFileName(fileName),
                    problemName: fileName,
                    topicName: directory,
                    solution,
                    userName: 'alex'
                };
                console.log('problem ', problem);
                await this.computeService
                    .saveProblem(problem)
                    .then((response) => console.log('Successfully saved problem', response)
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
    async saveProblemAndUpdateTimestamp(latestCommit, directoryList = []) {
        (directoryList.length == 0
            ? await this.getDirectories('../../leetcode')
            : directoryList.filter((directory) => !Constants_1.IGNORE_FOLDERS.includes(directory) &&
                !Constants_1.IGNORE_FOLDERS.find((ignoredFolder) => directory.includes(ignoredFolder)) &&
                !directory.includes('.'))).forEach((directory) => {
            console.log('directory list', directory);
            try {
                this.extractAndSaveProblem(directory).then((response) => {
                    if (response) {
                        this.computeService.saveCommitTimestamp(latestCommit);
                    }
                    else {
                        // TO DO: Add rollback logic if processing is incomplete, All or none.
                    }
                });
            }
            catch (error) {
                console.log(`ERROR: ${error}`);
            }
        });
    }
}
exports.FileParser = FileParser;
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
//# sourceMappingURL=FileParser.js.map