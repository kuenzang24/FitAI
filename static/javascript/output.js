document.addEventListener('DOMContentLoaded', function () {
    // Sample data that would come from the backend
    const exerciseList = [
      'Group Classes Preference ',
      'Group Classes Preference ',
      'Group Classes Preference ',
      'Group Classes Preference ',
      'Group Classes Preference ',
      'Group Classes Preference '
    ];
  
    // Function to render the list items
    function renderExerciseList(items) {
      const listContainer = document.getElementById('exercise-list');
  
      // Clear any existing items
      listContainer.innerHTML = '';
  
      // Add new items
      items.forEach(item => {
        const listItem = document.createElement('div');
        listItem.className = 'list-item';
        listItem.textContent = item;
        listContainer.appendChild(listItem);
      });
    }
  
    // Render the exercise list with pre-fetched data
    renderExerciseList(exerciseList);
  });
  