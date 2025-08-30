// API helper functions for WFRP backend
const BASE_URL = 'http://localhost:5000/api';

export async function getCharacter() {
  const res = await fetch(`${BASE_URL}/character`);
  return await res.json();
}

export async function getMonster() {
  const res = await fetch(`${BASE_URL}/monster`);
  return await res.json();
}

export async function getQuest() {
  const res = await fetch(`${BASE_URL}/quest`);
  return await res.json();
}

export async function rollDice(sides = 6, count = 1) {
  const res = await fetch(`${BASE_URL}/dice?sides=${sides}&count=${count}`);
  return await res.json();
}
