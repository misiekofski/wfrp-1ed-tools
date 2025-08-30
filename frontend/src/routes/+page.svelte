<script>
import { getCharacter, getMonster, getQuest, rollDice } from '$lib/api.js';

let character = null;
let monster = null;
let quest = null;
let diceResult = null;
let diceSides = 6;
let diceCount = 1;

async function generateCharacter() {
  character = await getCharacter();
}
async function generateMonster() {
  monster = await getMonster();
}
async function generateQuest() {
  quest = await getQuest();
}
async function roll() {
  diceResult = await rollDice(diceSides, diceCount);
}
</script>

<main class="p-4 max-w-xl mx-auto space-y-8">
  <h1 class="text-3xl font-extrabold mb-6 text-indigo-700 text-center drop-shadow">WFRP 1st Edition Helper Tool</h1>

  <section class="space-y-2">
    <button class="btn btn-character" on:click={generateCharacter}>🎲 Generate Character</button>
    {#if character}
      <div class="card card-character mt-3">
        <h2 class="text-xl font-bold text-indigo-800 mb-1">{character.name} <span class="text-gray-600">({character.race})</span></h2>
        <div class="mb-2 text-sm text-gray-700">Profession: <span class="font-semibold text-indigo-600">{character.profession}</span></div>
        <div class="mb-2 text-sm text-gray-700">A {character.race} {character.profession} known for their skills and unique background. They are ready to face the dangers of the Old World!</div>
        <div>
          <strong class="text-indigo-700">Stats:</strong>
          <ul class="grid grid-cols-3 gap-x-4 gap-y-1 mt-1 text-sm">
            {#each Object.entries(character.stats) as [key, value]}
              <li><span class="font-bold text-indigo-800">{key}</span>: <span class="text-gray-800">{value}</span></li>
            {/each}
          </ul>
        </div>
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <button class="btn btn-monster" on:click={generateMonster}>👹 Generate Monster</button>
    {#if monster}
      <div class="card card-monster mt-3">
        <h2 class="text-lg font-bold text-red-700 mb-1">{monster.name}</h2>
        <div>
          <strong class="text-red-700">Stats:</strong>
          <ul class="grid grid-cols-3 gap-x-4 gap-y-1 mt-1 text-sm">
            {#each Object.entries(monster.stats) as [key, value]}
              <li><span class="font-bold text-red-800">{key}</span>: <span class="text-gray-800">{value}</span></li>
            {/each}
          </ul>
        </div>
        <div class="mt-1 text-sm text-gray-700">
          <strong class="text-red-700">Abilities:</strong> {monster.abilities.join(', ')}
        </div>
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <button class="btn btn-quest" on:click={generateQuest}>🗺️ Generate Quest</button>
    {#if quest}
      <div class="card card-quest mt-3">
        <div class="text-lg font-bold text-green-700 mb-1">Quest:</div>
        <div class="mb-1 text-gray-800">{quest.quest}</div>
        <div class="text-sm text-gray-700"><strong class="text-green-700">Complication:</strong> {quest.complication}</div>
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <div class="flex items-center gap-2">
      <input type="number" bind:value={diceSides} min="2" max="100" class="input-dice" /> sides
      <input type="number" bind:value={diceCount} min="1" max="10" class="input-dice" /> dice
      <button class="btn btn-dice" on:click={roll}>🎲 Roll Dice</button>
    </div>
    {#if diceResult}
      <div class="card card-dice mt-3">
        <strong class="text-blue-700">Result:</strong> <span class="text-gray-800">{diceResult.result.join(', ')}</span>
      </div>
    {/if}
  </section>
</main>

<style>
main {
  font-family: 'Segoe UI', 'Arial', sans-serif;
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
}
.btn {
  padding: 0.6em 1.2em;
  border-radius: 6px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 1px 4px #0001;
}
.btn-character {
  background: linear-gradient(90deg, #a5b4fc, #6366f1);
  color: #fff;
}
.btn-character:hover {
  background: linear-gradient(90deg, #6366f1, #a5b4fc);
}
.btn-monster {
  background: linear-gradient(90deg, #fca5a5, #ef4444);
  color: #fff;
}
.btn-monster:hover {
  background: linear-gradient(90deg, #ef4444, #fca5a5);
}
.btn-quest {
  background: linear-gradient(90deg, #6ee7b7, #22c55e);
  color: #fff;
}
.btn-quest:hover {
  background: linear-gradient(90deg, #22c55e, #6ee7b7);
}
.btn-dice {
  background: linear-gradient(90deg, #93c5fd, #2563eb);
  color: #fff;
}
.btn-dice:hover {
  background: linear-gradient(90deg, #2563eb, #93c5fd);
}
.input-dice {
  width: 4em;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  border: 1px solid #cbd5e1;
  background: #fff;
  font-size: 1em;
}
.card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 4px #0001;
  padding: 1em;
  margin-top: 0.5em;
}
.card-character {
  border-left: 6px solid #6366f1;
}
.card-monster {
  border-left: 6px solid #ef4444;
}
.card-quest {
  border-left: 6px solid #22c55e;
}
.card-dice {
  border-left: 6px solid #2563eb;
}
</style>
