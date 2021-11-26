<template>
  <div className='container'>
    <form @submit.prevent='addTask'>
      <h1>Todo List</h1>
      <input placeholder='Add new task' className='taskInput' v-model="newTask" maxlength='35'>
      <button className='addButton'><p>+</p></button>
    </form>
  </div>
  <div className='container'>
    <ul role='list' className='taskList'>
      <li v-for="task in tasks" :key='task.id'> 
        <input type='checkbox' @click='updateStatus(task)' v-model="task.isComplete"> 
        <div className='taskLabels'>
        <label for='checkbox' :class="{isComplete: task.isComplete}"> {{ task.title }}  </label>
        <label className='dateLabel'>{{task.created}}</label>
        </div>
        <button v-on:click='removeTask(task)' className='removeButton'>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="rgb(201, 75, 52)">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </li>
    </ul>
  </div>
</template>


<script>
import { getAPI } from '../api.js'
export default {
  data() {
    return {
      newTask: '',
      tasks: [],
    }
  },
  mounted() {
    this.getTasks();
    // if (localStorage.getItem('tasks')) {
    //   try {
    //     this.tasks = JSON.parse(localStorage.getItem('tasks'));
    //   } catch(e) {
    //     localStorage.removeItem('tasks');
    //   }
    // }
  },
  methods: {
    addTask() {
      this.newTask = this.newTask.trim()
      if (this.newTask != '') {
        // this.tasks.push({title: this.newTask, isComplete: false})
        // this.saveTasksLocally();
        getAPI.post('tasks/create/', {
        title: this.newTask
      })
      .then(response => {
        console.log(response.data);
        this.getTasks();
      })
      .catch(error => {
        console.log(error);
      });
        this.newTask = '';
      }
    },
    getTasks(){
      getAPI.get('tasks/').then(response => {
      if (this.tasks != response.data) {
          this.tasks = response.data;
      }
      }).catch(error => {
        console.log('Error fetching tasks.', error);
      })
    },
    removeTask(task) {
      var idx = this.tasks.indexOf(task);
      getAPI.delete('/task/delete/' + task.id).then(response => {
          console.log(response);
        })
      this.tasks.splice(idx, 1);
      //this.saveTasksLocally();
    }, 
    updateStatus(task) {
      task.isComplete = !task.isComplete;
      getAPI.put('task/' + task.id, {
        title: task.title,
        isComplete: task.isComplete
      })
      .then(response => {
        console.log(response);
        
      })
      .catch(error => {
        console.log(error);
      });
    }
      //this.saveTasksLocally();
    },
    // saveTasksLocally() {
    //   const parsedObject = JSON.stringify(this.tasks);
    //   localStorage.setItem('tasks', parsedObject);
    // },
}
</script>
