const now = new Date();
const year = now.getFullYear().toString().slice(-2);
const month = (now.getMonth() + 1).toString().padStart(2, "0");
const day = now.getDate().toString().padStart(2, "0");
const formattedDate = ` ${year}년  ${month}월  ${day}일 의회 회의` ;
document.getElementById("time").textContent = formattedDate;

// Get all the checkboxes
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Loop through each checkbox
// checkboxes.forEach(function (checkbox) {
//   // Add a click event listener to the checkbox
//   checkbox.addEventListener("click", function () {
//     // Get the parent row of the checkbox
//     const row = this.parentNode.parentNode;
//     // If the checkbox is checked, hide the row
//     if (this.checked) {
//       row.style.display = "none";
//     } else {
//       // If the checkbox is unchecked, show the row
//       row.style.display = "";
//     }
//   });
// });

// checkbox의 상태를 모니터링하는 함수
function checkAttendance() {
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var allChecked = true;
  checkboxes.forEach(function (checkbox) {
    if (!checkbox.checked) {
      allChecked = false;
    }
  });
  // 모든 checkbox가 체크되면 '전원 출석이 완료되었습니다!' 메시지 보이기
  if (allChecked) {
    var message = document.createElement("p");
    message.textContent = "전원 출석이 완료되었습니다!";
    document.body.appendChild(message);
  }
}

// checkbox 상태가 변할 때마다 checkAttendance 함수 실행
var checkboxes2 = document.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach(function (checkbox) {
  checkbox.addEventListener("change", checkAttendance);
});

