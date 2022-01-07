


function Bird(){

    this.x = 65;
    this.y = height / 2;

    this.width = 30;
    this.height = 35;

    this.gravity = 0.6; 
    this.velocity = 0;
    this.lift = -15;

    this.isdead = false;
    
    this.flappy_bird = loadImage(FLAPPY_BIRD);
    
    this.show = function(){
        if(this.isdead == true){
            textSize(32);
            text('You Are Dead', width / 2 - 150, height / 2);
            fill(0, 102, 153);
        }
        else{
            image(this.flappy_bird, this.x, this.y , this.width, this.height);
        }
    }

    this.update = function(){

        if(this.isdead == true){
            this.x = width / 2;
            this.y = height / 2;

            this.velocity += this.gravity;
            this.velocity *= 0.9;
            this.y += this.velocity;

            if(this.y > height){
                this.y = height + 50;
            }
        }
        else{
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
        
    }

    this.up = function(){
        this.velocity += this.lift;
    }

}
