let walker;

function setup() {
  createCanvas(400, 400);
  background(220);
  walker = new Walker(); // Create a new Walker object
}

function draw() {
   // Call the step method on the walker object
  walker.step(walker.stepRealNumbers.bind(walker));
  walker.show(); // Call the show method to display the walker
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
    stroke(0);
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

    //{!1} 0, 1, 2, or 3. The random choice determines the step.
    let choice = floor(random(4));
    if (choice === 0) {
      this.x++;
    } else if (choice === 1) {
      this.x--;
    } else if (choice === 2) {
      this.y++;
    } else {
      this.y--;
    }
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