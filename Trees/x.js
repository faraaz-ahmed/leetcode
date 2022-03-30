const shorten = (str) => {
  prev = str[0];
  current = str[1];
  while (i < str.length - 1) {
    current = str[i]
    if (prev === current) {
      str.pop(i);
    } else {
      i++;
    }
    prev = current;
  }
  return str;
}

const reduce = (str) => {
  length = shorten(str).length
  if (length == shorten(shorten(str)) {
    return shorten(str)
  } else {
    return reduce(shorten(str))
  }
}

const reverse = (sentence) => {
  sentenceArray = sentence.split('.')
  sentenceArray.map(x => {
    x = x.reverse();
  })
  reverseSentence = '';
  for(let i = 0; i < sentenceArray.length; i++) {
    reverseSentence += sentenceArray[i] + '.';
  }
  return reverseSentence;
}