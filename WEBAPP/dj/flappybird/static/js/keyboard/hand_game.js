
let capture;
let Canvas;
let bird;
let start_game = 0;
let pipes = [];
let background;

document.getElementById("start-btn").addEventListener("click",() => {
  start_game = 1;
});

document.getElementById("stop-btn").addEventListener("click",() => {
  start_game = 0;
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
        console.log("DEAD");
      }
      
      if(pipes[i].offscreen()){
        pipes.splice(i,1);
      }

    }
  }
}

function keyPressed(){
    if(key == " "){
        bird.up();
    }
}
