let walker;
let total = 20;
let randomCounts = Array.from({ length: total }, (v, i) => 0);

function setup() {
  createCanvas(420, 690);
  background('#2d549c');
  walker = new Walker(); // Create a new Walker object
}

function draw() {
  // Call the step method on the walker object
  walker.step();
  walker.show(); // Call the show method to display the walker
  // drawBars();
}

function drawBars() {
  let index = floor(random(randomCounts.length));
  randomCounts[index]++;

  stroke(0);
  fill(175);
  let w = width / randomCounts.length;

  for (let x = 0; x < randomCounts.length; x++) {
    rect(x * w, height - randomCounts[x], w - 1, randomCounts[x]);
  }
}

class Walker {
  // Objects have a constructor where they are initialized.
  constructor() {
    // Objects have data.
    this.x = width / 2;
    this.y = height / 2;
  }

  // Objects have methods.
  show() {
    stroke(255);
    point(this.x, this.y);
    console.debug(`Walker is at (${this.x}, ${this.y})`);
  }

  /**
   * 
   * @param {Function} fn - the step function that defines how the walker moves.
   */
  step(fn) {
    if (fn) {
      console.debug("Using provided step function");
      fn();
      return;
    }
    let xstep = random(-2.75, 3);
    let ystep = random(-2.75, 3);
    this.x += xstep;
    this.y += ystep;


    //{!1} 0, 1, 2, or 3. The random choice determines the step.
    // let choice = floor(random(4));
    // if (choice === 0) {
    //   this.x++;
    // } else if (choice === 1) {
    //   this.x--;
    // } else if (choice === 2) {
    //   this.y++;
    // } else {
    //   this.y--;
    // }
  }

  stepEightWays() {
    //{!2} Yields –1, 0, or 1
    let xstep = floor(random(3)) - 1;
    let ystep = floor(random(3)) - 1;
    this.x += xstep;
    this.y += ystep;
  }

  stepRealNumbers() {
    //{!3} Yields a random number between -1 and 1
    let xstep = random(-1, 1);
    let ystep = random(-1, 1);
    this.x += xstep;
    this.y += ystep;
  }
}