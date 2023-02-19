var getLatestCommit = function () {
    return require('child_process')
        .execSync('git rev-parse HEAD')
        .toString()
        .trim();
};
// console.log(revision);
/*
tsc index.ts
node index.js
 */
var getFileDiff = function (sha1, sha2) {
    return require('child_process')
        .execSync("git diff --name-only HEAD~".concat(sha1, " HEAD~").concat(sha2))
        .toString()
        .trim();
};
console.log(getFileDiff(10, 5), 'yo');
// latestCommit 
