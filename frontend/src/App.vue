<script setup>
import { ref } from 'vue';
import axios from 'axios';
import HeaderComponent from './components/HeaderComponent.vue';

const phrase = ref('');
const translatedPhrase = ref('');

const submitPhrase = async () => {
  try {
    const response = await axios.post('http://localhost:8000/translate', { sentence: phrase.value });
    translatedPhrase.value = response.data.output;
  } catch (error) {
    alert('Error translating phrase:', error);
    translatedPhrase.value = 'Error translating phrase';
  }
};
</script>

<template>
  <div id="app" class="dark-theme">
    <HeaderComponent/>

    <main class="main-content">
      <div class="input-container">
        <div class="input-group">
          <label for="input-phrase" class="label">Write a sentence in English</label>
          <textarea id="input-phrase" v-model="phrase" class="textarea" placeholder="Type your phrase here..."></textarea>
        </div>
        <div class="input-group">
          <label for="translated-phrase" class="label">Phrase translated into Portuguese</label>
          <textarea id="translated-phrase" v-model="translatedPhrase" class="textarea" readonly placeholder="Your translation will be shown here..."></textarea>
        </div>
      </div>
      <button @click="submitPhrase" class="submit-button green">Send</button>
    </main>
  </div>
</template>