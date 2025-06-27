let walker;
let total = 20;
let randomCounts = Array.from({ length: total }, (v, i) => 0);

function setup() {
  createCanvas(420, 690);
  background('#2d549c');
  walker = new Walker(); // Create a new Walker object

  bookComments();
}

function draw() {
  // Call the step method on the walker object
  walker.step();
  walker.show(); // Call the show method to display the walker
  drawBars();
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
    // console.debug(`Walker is at (${this.x}, ${this.y})`);
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


    // {!1} 0, 1, 2, or 3. The random choice determines the step.
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

  stepWithTendendcyTowardsBottomRight() {
    let xstep = random(-2.75, 3);
    let ystep = random(-2.75, 3);
    this.x += xstep;
    this.y += ystep;
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

function bookComments() {
  const drawAceProbability = 4 / 52;
  console.log(`Probability of drawing an ace: ${drawAceProbability}`);
  const drawAceThrice = drawAceProbability * drawAceProbability * drawAceProbability;
  console.log(`\t 3 times in a row: ${drawAceThrice}`);
  console.log(`\t 3 times in a row[using Math.pow(*, )]: ${Math.pow(drawAceProbability, 3)}`);

  const drawAceFourTimes = drawAceProbability ** 4;
  console.log(`\t 4 times in a row: ${drawAceFourTimes}`);

  const cards = Array.from({ length: 52 }, (_, i) => {
    const suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades'][Math.floor(i / 13)];
    const rank = (i % 13) + 1;
    // named ranks: 1 = Ace, 11 = Jack, 12 = Queen, 13 = King 
    const name = rank === 1 ? 'Ace' :
      rank === 11 ? 'Jack' :
        rank === 12 ? 'Queen' :
          rank === 13 ? 'King' : rank;

    return {
      index: i,
      suit,
      rank,
      name,
      key: `${rank}_${suit}`,
    };
  });

  const randomCard = random(cards);
  print(`Random card drawn:`, randomCard);


  const coinTossProbability = 1 / 2;
  console.log(`Probability of tossing a coin and getting heads: ${coinTossProbability}`);
  const coinTossProbabilityThrice = coinTossProbability ** 3;
  console.log(`\t 3 times in a row: ${coinTossProbabilityThrice}`);

  const probability = 0.1; // 10% chance of success
  const r = random(1); // Generate a random number between 0 and 1

  if (r < probability) {
    console.log(`SING! Random number ${r} is less than ${probability}`);
  } else if (r < 0.7) {
    console.log(`SHOUT! Random number ${r} is between ${probability} and 0.7`);
  } else {
    console.log(`DANCE! Random number ${r} is greater than or equal to 0.7`);
  }
}