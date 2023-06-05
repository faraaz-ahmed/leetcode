"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ComputeService_1 = require("./ComputeService");
const FileParser_1 = require("./FileParser");
class SyncService {
    constructor() {
        this.getCommitIndex = (commitSHA, limit = 10) => {
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
    }
    executeGitCommand(command) {
        return require('child_process').execSync(command).toString().trim();
    }
    getLatestCommit() {
        return this.executeGitCommand('git rev-parse HEAD');
    }
    getCommitByIndex(index) {
        return this.executeGitCommand(`git rev-parse HEAD~${index}`);
    }
    getFileDiffByCommitIndex(commitIndex1, commitIndex2) {
        return this.executeGitCommand(`git diff --name-only HEAD~${commitIndex1} HEAD~${commitIndex2}`);
    }
    getFileDiff(commitSHA1, commitSHA2) {
        return this.executeGitCommand(`git diff --name-only ${commitSHA1} ${commitSHA2}`).split('\n');
    }
    async getLastProcessedCommit() {
        /**
         * gets the last processed commit from ComputeService.
         */
        const computeService = new ComputeService_1.ComputeService();
        const timestamp = await computeService.getTimestamp();
        if (typeof timestamp === 'string') {
            return timestamp;
        }
        return timestamp.timestampContent;
    }
    updateLastProcessedCommit() {
        /**
         * updates the last processed commit from ComputeService.
         */
        // return '';
    }
    getFolderNames(filePath) {
        return filePath.split('/')[0];
    }
    async saveProblemsFromLastProcessedCommit() {
        const lastProcessedCommit = await this.getLastProcessedCommit();
        const latestCommit = this.getLatestCommit();
        const fileParser = new FileParser_1.FileParser();
        if (lastProcessedCommit === 'Timestamp Name does not exist.') {
            // process all files and update last processed commit.
            fileParser.saveProblemAndUpdateTimestamp(latestCommit);
        }
        else {
            // process only the diff and update the last processed commit.
            const folderNames = [
                ...new Set(this.getFileDiff(lastProcessedCommit, latestCommit).map((path) => this.getFolderNames(path)))
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
//# sourceMappingURL=index.js.map