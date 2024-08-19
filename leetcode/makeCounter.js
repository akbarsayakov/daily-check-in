function makeCounter(initalValue = 0) {
  let count = initalValue

  return function incrementCount() {
    const currentValue = count
    count++
    return currentValue
  }
}

const counter1 = makeCounter()
console.log(counter1())
console.log(counter1())
console.log(counter1())
console.log(counter1())

const counter2 = makeCounter(5)
console.log('1', counter2())
console.log('2', counter2())
console.log('3', counter2())
console.log('4', counter2())
console.log('5', counter2())
