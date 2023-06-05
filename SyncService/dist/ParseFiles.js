"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs = require('fs');
const fs_1 = require("fs");
const _1 = require(".");
const ComputeService_1 = require("./ComputeService");
const Constants_1 = require("./Constants");
const getFileContent = (path) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        return yield fs.readFileSync(path, 'utf8');
    }
    catch (err) {
        console.error(err);
        return err;
    }
});
const getDirectories = source => (0, fs_1.readdirSync)(source, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory() && !Constants_1.IGNORE_FOLDERS.includes(dirent.name))
    .map(dirent => dirent.name);
const getFileNames = source => (0, fs_1.readdirSync)(source, { withFileTypes: true })
    .filter(dirent => !dirent.isDirectory() && dirent.name.startsWith('lc'))
    .map(dirent => dirent.name);
const getIdFromFileName = (fileName) => parseInt(fileName.replace(/[^0-9]/g, ""));
const saveProblemAndUpdateTimestamp = () => {
    getDirectories('../../leetcode').forEach(directory => {
        const directoryPath = `../../leetcode/${directory}`;
        let processingComplete = true;
        getFileNames(directoryPath).forEach((fileName) => __awaiter(void 0, void 0, void 0, function* () {
            const problem = {
                problemId: getIdFromFileName(fileName),
                problemName: fileName,
                topic: directory,
                solution: yield getFileContent(`${directoryPath}/${fileName}`),
                userId: '1'
            };
            const response = yield (0, ComputeService_1.saveProblem)(problem);
            if (response === 'error') {
                processingComplete = false;
                console.log('unable to save for problem = ', problem);
            }
        }));
        if (processingComplete) {
            (0, ComputeService_1.saveCommitTimestamp)((0, _1.getLatestCommit)());
        }
    });
};
saveProblemAndUpdateTimestamp();
//# sourceMappingURL=ParseFiles.js.map