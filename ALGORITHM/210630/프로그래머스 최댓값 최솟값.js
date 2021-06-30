function solution(s) {
    var answer = '';

    var s = s.split(' ')
    var minum = 123123813287129
    var maxnum= -12312312312312312
    for (var i = 0; i < s.length; i ++) {
        if(Number(s[i]) < minum) {
            minum = Number(s[i])
        }
        if(Number(s[i]) > maxnum) {
            maxnum = Number(s[i])
        }
    }
    answer = minum + " " + maxnum
    return answer;
}