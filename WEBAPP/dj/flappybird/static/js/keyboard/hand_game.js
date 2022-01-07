
let capture;
let Canvas;
let bird;
let start_game = 0;
let pipes = [];
let background;
let score = 0;

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



document.getElementById("start-btn").addEventListener("click",() => {
  start_game = 1;
});

document.getElementById("stop-btn").addEventListener("click",() => {
  start_game = 0;
});

document.getElementById("restart-btn").addEventListener("click",() => {
  location.reload();
});

function setup() {

  Canvas = createCanvas(600, 400);
  Canvas.parent("column");


  bird = new Bird();
  pipes.push(new Pipe());

  background = loadImage(BACKGROUND);

}

function draw() {
  
  image(background, 0, 0, 600, 400);

  if(start_game == 1){

    bird.update();
    bird.show();
    
    if(frameCount % 100 == 0){
      pipes.push(new Pipe());
    }

    for(let i=pipes.length-1;i >= 0;i--){

      pipes[i].show();
      pipes[i].update();
      
      if(pipes[i].hits(bird)){
        bird.isdead = true;
        const csrftoken = getCookie('csrftoken');
        $.ajax({
          type: "POST",
          url : "/game/hand-game/",
          data : {
              score: score,
              csrfmiddlewaretoken:csrftoken
          }
      }).done((res) => {
        console.log(res);  
      })
      }
      
      if(pipes[i].offscreen()){
        if(bird.isdead != true){
          score += 1;
        }
        pipes.splice(i,1);
      }

    }
    textSize(32);
    text(`SCORE : ${score}`,400,50);
    fill(0, 102, 153);
  }
}

function keyPressed(){
    if(key == " "){
        bird.up();
    }
}
