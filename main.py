<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>규민이의 공원 🌳</title>

<style>
body{
    margin:0;
    overflow:hidden;
    font-family:Arial, sans-serif;
}

#game{
    width:100vw;
    height:100vh;
    background:#7dd87d;
    position:relative;
}

/* 플레이어 */
#player{
    width:50px;
    height:50px;
    background:#4a6cff;
    border-radius:50%;
    position:absolute;
    left:300px;
    top:300px;
    border:4px solid white;
    box-sizing:border-box;
}

/* 눈 */
.eye{
    width:8px;
    height:8px;
    background:white;
    border-radius:50%;
    position:absolute;
    top:15px;
}

.left-eye{
    left:12px;
}

.right-eye{
    right:12px;
}

/* 말풍선 */
#bubble{
    position:absolute;
    padding:8px 12px;
    background:white;
    border-radius:15px;
    font-size:24px;
    display:none;
    pointer-events:none;
    transform:translate(-25%, -100%);
}

/* 나무 */
.tree{
    width:70px;
    height:70px;
    background:green;
    border-radius:50%;
    position:absolute;
}

.trunk{
    width:20px;
    height:30px;
    background:brown;
    position:absolute;
    left:25px;
    top:60px;
}

/* UI */
#ui{
    position:fixed;
    top:15px;
    left:15px;
    background:rgba(255,255,255,0.9);
    padding:15px;
    border-radius:12px;
}

button{
    border:none;
    padding:10px;
    margin:3px;
    font-size:20px;
    cursor:pointer;
    border-radius:10px;
}
</style>
</head>
<body>

<div id="ui">
    <h3>😀 이모지</h3>
    <button onclick="showEmoji('😀')">😀</button>
    <button onclick="showEmoji('😎')">😎</button>
    <button onclick="showEmoji('😂')">😂</button>
    <button onclick="showEmoji('❤️')">❤️</button>
</div>

<div id="game">

    <div class="tree" style="left:100px;top:100px;">
        <div class="trunk"></div>
    </div>

    <div class="tree" style="left:700px;top:150px;">
        <div class="trunk"></div>
    </div>

    <div class="tree" style="left:500px;top:500px;">
        <div class="trunk"></div>
    </div>

    <div class="tree" style="left:900px;top:300px;">
        <div class="trunk"></div>
    </div>

    <div id="player">
        <div class="eye left-eye"></div>
        <div class="eye right-eye"></div>
    </div>

    <div id="bubble"></div>

</div>

<script>
const player = document.getElementById("player");
const bubble = document.getElementById("bubble");

let x = 300;
let y = 300;
let speed = 4;

let keys = {};

document.addEventListener("keydown", e=>{
    keys[e.key.toLowerCase()] = true;
});

document.addEventListener("keyup", e=>{
    keys[e.key.toLowerCase()] = false;
});

function update(){

    if(keys["w"]) y -= speed;
    if(keys["s"]) y += speed;
    if(keys["a"]) x -= speed;
    if(keys["d"]) x += speed;

    x = Math.max(0, Math.min(window.innerWidth-50,x));
    y = Math.max(0, Math.min(window.innerHeight-50,y));

    player.style.left = x + "px";
    player.style.top = y + "px";

    bubble.style.left = (x+10) + "px";
    bubble.style.top = y + "px";

    requestAnimationFrame(update);
}

function showEmoji(emoji){

    bubble.innerHTML = emoji;
    bubble.style.display = "block";

    clearTimeout(window.emojiTimeout);

    window.emojiTimeout = setTimeout(()=>{
        bubble.style.display = "none";
    },2000);
}

update();
</script>

</body>
</html>
