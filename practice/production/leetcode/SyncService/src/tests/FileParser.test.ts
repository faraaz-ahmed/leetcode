// this.computeService.saveProblemAndUpdateTimestamp();
// new FileParser()
// 	.getFileContent('../../leetcode/strings/lc6.py')
// 	.then((x) => console.log(x));

import { FileParser } from '../FileParser';

// new FileParser().saveTopic('strings').then((response) => console.log(response));

// new FileParser()
// 	.saveProblemAndUpdateTimestamp('mock commit', ['strings'])
// 	.then((response) => console.log(response))
// 	.catch((response) => console.log('error', response));

new FileParser()
	.getDirectories('../../leetcode')
	.then((result) => console.log('Check Result = ', result));

/**
 * Steps to build:

cd SyncScript
tsc
node ./dist/tests/FileParser.test.js

 */
