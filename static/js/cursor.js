// // static/js/cursor.js
// document.addEventListener('mousemove', (e) => {
//     const cursorTrail = document.getElementById('cursor-trail');
//     if (cursorTrail) {
//     cursorTrail.style.transform = `translate(${e.pageX}px, ${e.pageY}px)`;
//     }
// });

// 커서 트레일 요소 가져오기
const cursorTrail = document.getElementById('cursor-trail');

// 마우스 움직임 이벤트
document.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX + 20; // 마우스 X 좌표
    const mouseY = event.clientY + 20; // 마우스 Y 좌표

    // 커서 트레일 위치를 즉시 커서 위치로 업데이트
    cursorTrail.style.left = `${mouseX}px`;
    cursorTrail.style.top = `${mouseY}px`;
});