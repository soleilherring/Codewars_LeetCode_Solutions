/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
//   PREP
//     Parameters - accounts (list)
//     Return - largest sum
//     Example - Input: accounts = [[1,2,3],[3,2,1]]
//     Output: 6
//     Pseuodocode:
//     1. use map function to loop through each list
//          2.  do sum for each list (item)
//     3. Will have an array of total of each list(item); use max function 
//     4. return max number
    
    return Math.max(...accounts.map(x => x.reduce((acc, curr) => acc + curr, 0)))
};