
let capture;
let Canvas;
let bird;
let start_game = 0;
let pipes = [];


document.getElementById("start-btn").addEventListener("click",() => {
  start_game = 1;
});

document.getElementById("stop-btn").addEventListener("click",() => {
  start_game = 0;
});

function setup() {

  Canvas = createCanvas(600, 400);
  Canvas.parent("column");

  capture = createCapture(VIDEO);
  capture.size(600, 400);
  capture.hide();

  bird = new Bird();
  pipes.push(new Pipe());

}



function draw() {

  // this is for inverting the camera image
  push();
  translate(width,0);
  scale(-1, 1);
  image(capture, 0, 0, 600, 400);
  pop();
 
 
  if(start_game == 1){

    //bird.update();
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

