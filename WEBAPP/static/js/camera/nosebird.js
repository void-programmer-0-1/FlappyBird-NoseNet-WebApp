


function Bird(){

    this.x = 65;
    this.y = height / 2;

    this.width = 30;
    this.height = 35;
    
    this.flappy_bird = loadImage("static/images/flappy-bird.png");
    
    this.show = function(){
        image(this.flappy_bird, this.x, this.y , this.width, this.height);
    }

    this.update = function(){
        return null;   
    }

}
