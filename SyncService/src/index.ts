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
		if (
			lastProcessedCommit === 'Timestamp Name does not exist.' ||
			!lastProcessedCommit
		) {
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

/* Problem Name is &&& Sort Segments &&& PLEASE DO NOT REMOVE THIS LINE. */

/**
 **  * Instructions to candidate.
 **  *  1) Run this code in the REPL to observe its behaviour.
 **  *  2) Consider adding some additional tests.
 **  *  3) Implement sortSegments() correctly.
 **  *  4) If time permits, try to improve your implementation.
 **
 */
// import java.util.ArrayList;
// import java.util.HashMap;
// import java.util.List;

// public class Solution {
//   record Pair(int left, int right) {}
//   /**
//    * Given a jumbled collection of segments, each of which is represented as
//    * a Pair(startPoint, endPoint), this function sorts the segments to
//    * make a continuous path.
//    *
//    * A few assumptions you can make:
//    * 1. Each particular segment goes in one direction only, i.e.: if you
//    * see (1, 2), you will not see (2, 1).
//    * 2. Each starting point only have one way to the end point, i.e.: if
//    * you see (6, 5), you will not see (6, 10), (6, 3), etc.
//    *
//    * For example, if you're passed a list containing the following int arrays:
//    *      [(4, 5), (9, 4), (5, 1), (11, 9)]
//    * Then your implementation should sort it such:
//    *      [(11, 9), (9, 4), (4, 5), (5, 1)]
//    *
//    * @param segments collection of segments, each represented by a Pair(startPoint, endPoint).
//    * @return The sorted segments such that they form a continuous path.
//    * @throws Exception if there is no way to create one continuous path from
//    *          all the segments passed into this function. Feel free to change the
//    *          Exception type as you think appropriate.
//    */
//   public static List<Pair> sortSegments(final List<Pair> segments)
//       throws Exception {
//     // Pair is a simple data structure from Commons Lang.
//     // Use getLeft() and getRight() to access the first and second value respectively.
//     List<Pair> initialPair = new ArrayList<>();
//     HashMap<Integer, Pair> map = new HashMap<>();
//     HashMap<Integer, Integer> rightValueMap = new HashMap<>();

//     for (int i = 0; i < segments.size(); i++) {
//       if (!map.containsKey(Integer.valueOf(segments.get(i).left))) {
//         map.put(Integer.valueOf(segments.get(i).left), segments.get(i));
//       } else {
//         throw new Exception();
//       }

//       if (!rightValueMap.containsKey(Integer.valueOf(segments.get(i).right))) {
//         rightValueMap.put(Integer.valueOf(segments.get(i).right), 1);
//       } else {
//         rightValueMap.put(Integer.valueOf(segments.get(i).right), rightValueMap.get(Integer.valueOf(segments.get(i).right)) + 1);
//       }
//     }

//     List<Integer> leftValueWithNoMapping = new ArrayList<>();
//     for (int i = 0; i < segments.size(); i++) {
//       if (!rightValueMap.containsKey(Integer.valueOf(segments.get(i).left))) {
//         leftValueWithNoMapping.add(Integer.valueOf(segments.get(i).left));
//       }
//     }

//     if (leftValueWithNoMapping.size() > 1) {
//       throw new Exception();
//     }
//     Integer startingLeftValue;
//     if (leftValueWithNoMapping.size() == 0) {
//       startingLeftValue = segments.get(0).left;
//     } else {
//       startingLeftValue = leftValueWithNoMapping.get(0);
//     }

//     List<Pair> result = new ArrayList<>();
//     Integer currentLeftValue = startingLeftValue;
//     Pair initialCurrentPair = map.get(currentLeftValue);
//     result.add(initialCurrentPair);
//     currentLeftValue = initialCurrentPair.right;
//     while (map.containsKey(currentLeftValue)) {
//       if (currentLeftValue == startingLeftValue) {
//         break;
//       }
//       Pair currentPair = map.get(currentLeftValue);
//       result.add(currentPair);
//       currentLeftValue = currentPair.right;
//     }
//     System.out.println(result);
//     return result;
//   }

//   public static boolean testBasicSort() throws Exception {
//     var jumbledSegments = new ArrayList<>(
//         List.of(new Pair(4, 5),
//             new Pair(9, 4),
//             new Pair(5, 1),
//             new Pair(11, 9)
//         )
//     );

//     var actualContinuousPath = sortSegments(jumbledSegments);

//     var expectedContinuousPath = new ArrayList<>(
//         List.of(new Pair(11, 9),
//             new Pair(9, 4),
//             new Pair(4, 5),
//             new Pair(5, 1) //1, 11 - cyclic 5,7
//         )
//     );

//     return expectedContinuousPath.equals(actualContinuousPath);
//   }

//   public static boolean testBasicSortCyclicCase() throws Exception {
//     var jumbledSegments = new ArrayList<>(
//         List.of(new Pair(4, 5),
//             new Pair(9, 4),
//             new Pair(5, 1),
//             new Pair(11, 9),
//             new Pair(1, 11)
//         )
//     );

//     var actualContinuousPath = sortSegments(jumbledSegments);

//     var expectedContinuousPath = new ArrayList<>(
//         List.of(new Pair(11, 9),
//             new Pair(9, 4),
//             new Pair(4, 5),
//             new Pair(5, 1),
//             new Pair(1, 11)
//         )
//     );

//     return expectedContinuousPath.equals(actualContinuousPath);
//   }

//   // public static boolean testBasicSortNonContinuous() throws Exception {
//   //   var jumbledSegments = new ArrayList<>(
//   //       List.of(new Pair(4, 5),
//   //           new Pair(9, 4),
//   //           new Pair(5, 1),
//   //           new Pair(11, 9),
//   //           new Pair(600, 9)
//   //       )
//   //   );

//   //   var actualContinuousPath = sortSegments(jumbledSegments);

//   //   var expectedContinuousPath = new ArrayList<>(
//   //       List.of(new Pair(11, 9),
//   //           new Pair(9, 4),
//   //           new Pair(4, 5),
//   //           new Pair(5, 1),
//   //           new Pair(1, 9)
//   //       )
//   //   );

//   //   return expectedContinuousPath.equals(actualContinuousPath);
//   // }

//   public static boolean doTestsPass() throws Exception {
//     boolean allPass = true;
//     allPass = allPass && testBasicSort();
//     // && testBasicSortCyclicCase();

//     return allPass;
//   }

//   public static void main(String[] args) throws Exception {
//     if (doTestsPass()) {
//       System.out.println("All tests pass");
//     } else {
//       System.out.println("Some tests fail");
//     }
//   }
// }
