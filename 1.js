//! find the minimum value from the array;

const findNumber = (array) => {
    if (!array.length) {
        throw new Error('Array should not be empty');
    } else if (array.length === 1) {
        return array[0];
    } else {
        let currentMinElement = array[0];
        for (let i = 0; i < array.length; i++) {
            if (array[i] < currentMinElement) {
                currentMinElement = array[i];
            }
        }
        return currentMinElement;
    }
}

const result = findNumber([4, 2, 5, 7]);
console.log(result);