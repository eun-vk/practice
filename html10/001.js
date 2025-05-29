let 참깨방 = () => {
    순쇠고기패티();
    console.log('Call 참깨빵');
}

let 순쇠고기패티 = () => {
    특별한 소스();
    console.log('Call 순쇠고기패티');
}

let 특별한 소스 = () => {
    console.log('Call 특별한소스');
}

//다음 코드를 실행하면 어떤 순서로 출력될까요?
console.log("시작");
setTimeout(() => console.log("타이머 A"), 100);
setTimeout(() => console.log("타이머 B"), 50);
console.log("중간");
setTimeout(() => console.log("타이머 C"), 0);
console.log("끝");

//문제2: 직접 구현하기,
//다음과 같은 순서로 출력되도록 코드를 완성하세요.

/*원하는 출력:
준비
시작
첫번째 작업 완료
두번째 작업 완료
모든 작업 끝*/

console.log("준비");
setTimeout(() =>{
    console.log("___");
}, ___);

console.log("___");
setTimeout(() => {
    console.log("___");
}, ___);
setTimeout(() => {
    console.log("___");
}, ___);



