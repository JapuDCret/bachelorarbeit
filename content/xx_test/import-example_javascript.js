function Car() {
    this.speed = 0;

    this.speedUp = function (speed) {
        this.speed = speed;
        setTimeout(
            () => console.log(this.speed),
            1000);
    };
}

let car = new Car();
car.speedUp(50); // outputs 50