
// const employees = [
//   {
//     employeeId: '1'
//   },
//   {
//     employeeId: '2',
//     managerId: '1'
//   },
//   {
//     employeeId: '3',
//     managerId: '1'
//   },
//   {
//     employeeId: '4',
//     managerId: '2'
//   },
//   {
//     employeeId: '5',
//     managerId: '3'
//   },
//   {
//     employeeId: '6',
//   },
//   {
//     employeeId: '7',
//     managerId: '6'
//   }
// ];

// //5, 4
// const getHierarchy = (empId, map, result) => {
//   if (!map[empId]) {
//     return result;
//   } else {
//     result.push(map[empId]);
//     // console.log('result', result)
//     return getHierarchy(map[empId], map, result);
//   }
// }

// const getCommonBoss = (empId1, empId2) => {
//   const map = {};
//   employees.forEach(x => {
//     if (!(map && map[x.employeeId])) {
//       map[x.employeeId] = x.managerId
//     }
//   });
//   hierarchy1 = getHierarchy(empId1, map, []);
//   hierarchy2 = getHierarchy(empId2, map, []);
//   // console.log('debug1', map,hierarchy1, hierarchy2);
//   answer = [];
//   for (let i = 0; i < hierarchy1.length; i++) {
//     for (let j = 0; j < hierarchy2.length; j++) {
//       if (hierarchy1[i] === hierarchy2[j]) {
//         answer.push(hierarchy1[i]);
//       }
//     }
//   }

//   console.log('answer =', answer);

// }

// getCommonBoss('4', '5');

const outerVariable = 'p'
var Person = function(pName){
  const name = pName + outerVariable;

  this.getName = function(){
    return name;
  }
}
function x() {
  console.log(outerVariable);
}
var person = new Person("sex");
console.log(person.getName());
x();