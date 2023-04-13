function toggleBtn1() {
    // 토글 할 버튼 선택 (btn1)
    const btn1 = document.getElementById('btn1');
    // btn1 숨기기 (display: none)
    if (btn1.style.display !== 'none') {
        btn1.style.display = 'none';
    }
    // btn` 보이기 (display: block)

    else {
        btn1.style.display = 'block';
    }
}

function sendRequest(tweet_id, event) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState == XMLHttpRequest.DONE && httpRequest.status == 200) {

            var json_data = JSON.parse(httpRequest.responseText)
            if (json_data['message'] == 'added') {
                event.innerText = "♥ " + json_data['like_cnt'];
            } else {
                event.innerText = "♡ " + json_data['like_cnt'];
            }
        }
    };
    // GET 방식으로 요청을 보내면서 데이터를 동시에 전달함.
    httpRequest.open("GET", "/tweet/likes/" + tweet_id, true);
    httpRequest.send();
}
