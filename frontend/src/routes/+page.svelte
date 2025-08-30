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

<main class="p-4 max-w-xl mx-auto space-y-6">
  <h1 class="text-2xl font-bold mb-4">WFRP 1st Edition Helper Tool</h1>

  <section class="space-y-2">
    <button on:click={generateCharacter}>Generate Character</button>
    {#if character}
      <div class="border p-2 mt-2">
        <strong>{character.name}</strong> ({character.race})<br>
        Profession: {character.profession}<br>
        <div>
          <strong>Stats:</strong>
          <ul>
            {#each Object.entries(character.stats) as [key, value]}
              <li>{key}: {value}</li>
            {/each}
          </ul>
        </div>
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <button on:click={generateMonster}>Generate Monster</button>
    {#if monster}
      <div class="border p-2 mt-2">
        <strong>{monster.name}</strong><br>
        <div>
          <strong>Stats:</strong>
          <ul>
            {#each Object.entries(monster.stats) as [key, value]}
              <li>{key}: {value}</li>
            {/each}
          </ul>
        </div>
        <div>
          <strong>Abilities:</strong> {monster.abilities.join(', ')}
        </div>
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <button on:click={generateQuest}>Generate Quest</button>
    {#if quest}
      <div class="border p-2 mt-2">
        <strong>Quest:</strong> {quest.quest}<br>
        <strong>Complication:</strong> {quest.complication}
      </div>
    {/if}
  </section>

  <section class="space-y-2">
    <div>
      <input type="number" bind:value={diceSides} min="2" max="100" style="width:4em;" /> sides
      <input type="number" bind:value={diceCount} min="1" max="10" style="width:3em;" /> dice
      <button on:click={roll}>Roll Dice</button>
    </div>
    {#if diceResult}
      <div class="border p-2 mt-2">
        <strong>Result:</strong> {diceResult.result.join(', ')}
      </div>
    {/if}
  </section>
</main>

<style>
button {
  background: #333;
  color: #fff;
  border: none;
  padding: 0.5em 1em;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background: #555;
}
input {
  margin-right: 0.5em;
}
</style>
