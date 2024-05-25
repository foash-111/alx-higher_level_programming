0x14-javascript-web_scraping

Reading and Writing a File Synchronously
Here is a complete example that reads from one file and writes its content to another file synchronously:

const fs = require('fs');

const sourceFile = 'source.txt';
const destinationFile = 'destination.txt';

try {
  // Read the source file
  const data = fs.readFileSync(sourceFile, 'utf8');

  // Write to the destination file
  fs.writeFileSync(destinationFile, data, 'utf8');
  console.log('Content copied successfully');
} catch (err) {
  console.error('Error during file operation:', err);
}
----------------------------------
Reading and Writing a File Asynchronously
Here is a complete example that reads from one file and writes its content to another file asynchronously:

The asynchronous method fs.writeFile is used to write data to a file without blocking the execution of your program.

const fs = require('fs');

const sourceFile = 'source.txt';
const destinationFile = 'destination.txt';

// Read the source file
fs.readFile(sourceFile, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the source file:', err);
    return;
  }

  // Write to the destination file
  fs.writeFile(destinationFile, data, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to the destination file:', err);
      return;
    }
    console.log('Content copied successfully');
  });
});
----------------------------
























Note: Converting a string to a native object is called deserialization, while converting a native object to a string so it can be transmitted across the network is called serialization.

A JSON string can be stored in its own file, which is basically just a text file with an extension of .json, and a MIME type of application/json.

MIME type
A MIME type (now properly called "media type", but also sometimes "content type") is a string sent along with a file indicating the type of the file (describing the content format, for example, a sound file might be labeled audio/ogg, or an image file image/png).

It serves the same purpose as filename extensions traditionally do on Windows. The name originates from the MIME standard originally used in email.

properties.
prototypes

In JavaScript, understanding properties and prototypes is crucial for effective programming, especially when dealing with objects and inheritance. Let's explore these concepts in detail:

Properties in JavaScript
Properties are values associated with a JavaScript object. An object property can hold a value of any data type, including other objects and functions.

Example:

javascript
----------
const person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, my name is " + this.name);
  }
};

// Accessing properties
console.log(person.name); // "Alice"
console.log(person.age);  // 25

// Calling a method
person.greet(); // "Hello, my name is Alice"
---------------
Prototypes in JavaScript
JavaScript is a prototype-based language, meaning that objects can inherit properties and methods from other objects. This is done through the prototype chain.

Example:

javascript
Copy code
const animal = {
  eats: true,
  walk() {
    console.log("Animal walks");
  }
};

const rabbit = {
  jumps: true
};

// Setting animal as the prototype of rabbit
rabbit.__proto__ = animal;

console.log(rabbit.eats); // true (inherited from animal)
rabbit.walk();            // "Animal walks" (inherited from animal)
-------------------
const parent = {
  parentProperty: "I am a parent"
};

const child = Object.create(parent);

console.log(child.parentProperty); // "I am a parent"
console.log(Object.getPrototypeOf(child) === parent); // true
----------

The statements const child = Object.create(parent); and const child.__proto__ = parent; are similar in effect, but they are not exactly the same and have some important differences in how they work and how they are typically used.

Explanation of Each Statement
const child = Object.create(parent);
Creates a New Object with parent as Prototype:

This creates a new object child whose prototype is set to parent.
The new object is empty, but it inherits properties and methods from parent.
Usage:

This is the standard and recommended way to set up inheritance.
It is clear and explicit in its intention.
---------------------
const parent = {
  parentProperty: "I am a parent"
};

const child = {}; // Initially an empty object
child.__proto__ = parent;

console.log(child.parentProperty); // "I am a parent"
console.log(Object.getPrototypeOf(child) === parent); // true
---------------
const child.__proto__ = parent;
Sets the Prototype of an Existing Object:

This line directly sets the __proto__ property of an existing object child to parent.
It alters the prototype chain of child after the object has been created.
Usage:

This is less common and is generally discouraged because manipulating __proto__ directly can have performance implications and is not as clear in intention.
It is primarily used for compatibility with older code or for quick prototyping.
----------------------
// Animal constructor
function Animal(name) {
  this.name = name;
}

// Adding speak method to Animal prototype
Animal.prototype.speak = function() {
  console.log(this.name + " makes a noise.");
};

// Adding speak method directly to Animal constructor
Animal.speak = function() {
  console.log("An animal makes a noise.");
};

// Dog constructor
function Dog(name, breed) {
  Animal.call(this, name); // Call the parent constructor
  this.breed = breed;
}

// Proper inheritance setup
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
//Dog.prototype = Object.create(Animal.prototype);:

Sets up Dog to inherit from Animal.
Dog.prototype is a new object with Animal.prototype as its prototype.
Dog.prototype.constructor = Dog;:
Breakdown:
Dog.prototype.constructor:

constructor is a reference to the function that created the instance's prototype.
Restoring the Constructor Reference:

By default, Dog.prototype.constructor would be Animal because we set Dog.prototype to an object created from Animal.prototype.
We explicitly set Dog.prototype.constructor to Dog to correct this reference.
Without Dog.prototype.constructor = Dog;, dog.constructor would point to Animal.




// Incorrect inheritance setup
Dog = Object.create(Animal); // This is not recommended

// Create instances
const dog1 = new Dog("Rex", "Labrador");
const dog2 = new Dog("Max", "Poodle");

// Call speak method
dog1.speak(); // "Rex makes a noise."
dog2.speak(); // "Max makes a noise."

// Calling static method
Animal.speak(); // "An animal makes a noise."
-----------------------------------------------
// Parent constructor
function Animal(name) {
  this.name = name;
  this.type = "Animal";
}

// Child constructor
function Dog(name, breed) {
  // Call the parent constructor
  Animal.call(this, name);
  this.breed = breed;
}

// Instantiate a Dog
const dog = new Dog("Rex", "Labrador");

console.log(dog.name); // "Rex"
console.log(dog.type); // "Animal" (inherited from Animal constructor)
console.log(dog.breed); // "Labrador"
-------------------------------------
By calling Animal.call(this, name);, you're essentially executing the code within the Animal constructor function, but with the context (this) set to the current Dog instance.
This allows the Dog constructor to inherit properties or behaviors from the Animal constructor while also allowing the Dog constructor to perform its own initialization steps.
----------------------------------------
function Animal() {}

// Set Dog's prototype to Animal constructor itself
const Dog = Object.create(Animal);

// Create an instance of Dog
const myDog = new Dog();

// Error: Dog is not a constructor
//In this scenario, Dog is not a constructor function; it's an object with Animal as its prototype. Attempting to create an instance of Dog (myDog) results in an error because Dog is not a constructor.
--------------------------------------------------------
function Animal() {}

// Set Dog's prototype to Animal.prototype
const Dog = Object.create(Animal.prototype);

// Create an instance of Dog
const myDog = new Dog();
// Error: Dog is not a constructor
//In this scenario, Dog is not a constructor function; it's an object with Animal as its prototype. Attempting to create an instance of Dog (myDog) results in an error because Dog is not a constructor
------------------------------------------------------------------------
function Animal() {}

function Dog() {}

// Set Dog's prototype to Animal constructor itself
Dog.prototype = Object.create(Animal);

// Create an instance of Dog
const myDog = new Dog();

console.log(myDog instanceof Animal); // false
console.log(myDog instanceof Dog);    // true
//In this scenario, Dog is an object inheriting from Animal.prototype. Creating an instance of Dog (myDog) works, but myDog is considered an instance of Dog only, which might not be the intended behavior.
------------------------------------------------------------------

function Animal() {}

function Dog() {}

// Set Dog's prototype to Animal.prototype
Dog.prototype = Object.create(Animal.prototype);

// Create an instance of Dog
const myDog = new Dog();

console.log(myDog instanceof Animal); // true
console.log(myDog instanceof Dog);    // true

//In this scenario, Dog.prototype is set to a new object inheriting from Animal.prototype, establishing proper prototype-based inheritance. Creating an instance of Dog (myDog) works as expected, and myDog is considered an instance of both Animal and Dog.
--------          -------------------          ------------------------------      --------------------------
***************************************************************************************************************************************
But sometimes we aren't so lucky — sometimes we receive a raw JSON string, and we need to convert it to an object ourselves. And when we want to send a JavaScript object across the network, we need to convert it to JSON (a string) before sending it. Luckily, these two problems are so common in web development that a built-in JSON object is available in browsers, which contains the following two methods:

parse(): Accepts a JSON string as a parameter, and returns the corresponding JavaScript object.
stringify(): Accepts an object as a parameter, and returns the equivalent JSON string.

we retrieve the response as text rather than JSON, by calling the text() method of the response
we then use parse() to convert the text to a JavaScript object.
