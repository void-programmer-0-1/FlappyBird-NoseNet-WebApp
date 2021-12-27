


function Bird(){

    this.x = 65;
    this.y = height / 2;

    this.width = 30;
    this.height = 35;

    this.gravity = 0.6; 
    this.velocity = 0;
    this.lift = -15;
    
    this.flappy_bird = loadImage(FLAPPY_BIRD);
    
    this.show = function(){
        image(this.flappy_bird, this.x, this.y , this.width, this.height);
    }

    this.update = function(){
        this.velocity += this.gravity;
        this.velocity *= 0.9;
        this.y += this.velocity;

        if(this.y > height){
            this.y = height;
            this.velocity = 0;
        }

        if(this.y < 0){
            this.y = 0;
            this.velocity = 0;
        }
    }

    this.up = function(){
        this.velocity += this.lift;
    }

}
