

function Pipe() {

  this.top = random(70,(height/2));
  this.bottom = random(70,(height/2));

  this.x = width;
  this.w = 50;
  
  this.pipe_image_down = loadImage(PIPE_DOWN);
  this.pipe_image_up = loadImage(PIPE_UP);
  
  this.speed = 2;

  this.show = function(){           
    console.log(Math.abs(this.top - (height - this.bottom)));

    if(((height - this.bottom) - this.top) <= 90){
      this.bottom -= 45;
      this.top -= 45;
    }
   
    image(this.pipe_image_up, this.x,0,this.w,this.top);
    image(this.pipe_image_down, this.x,height-this.bottom,this.w,this.bottom);
  }

  this.update = function() {
    this.x -= this.speed;
  }

  this.offscreen = function() {
    if (this.x < -this.w) {
      return true;
    }
    else {
      return false;
    }
  }

  this.hits = function(bird) {
    if(bird.y < this.top || bird.y > height - this.bottom){
      if(bird.x > this.x && bird.x < this.x + this.w){
        return true;
      }
    }
    return false;
  }

}