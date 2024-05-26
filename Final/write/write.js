




document.addEventListener("DOMContentLoaded", function() {
    let coordinates;

    fetch('/static/location.json')
        .then(response => response.json())
        .then(data => {
            coordinates = data;
            document.getElementById("btn1").addEventListener("click", () => changeMap(coordinates[0].latitude, coordinates[0].longitude));
            document.getElementById("btn2").addEventListener("click", () => changeMap(coordinates[1].latitude, coordinates[1].longitude));
            document.getElementById("btn3").addEventListener("click", () => changeMap(coordinates[2].latitude, coordinates[2].longitude));
            document.getElementById("btn4").addEventListener("click", () => changeMap(coordinates[3].latitude, coordinates[3].longitude));
            document.getElementById("btn5").addEventListener("click", () => changeMap(coordinates[4].latitude, coordinates[4].longitude));
            document.getElementById("btn6").addEventListener("click", () => changeMap(coordinates[5].latitude, coordinates[5].longitude));
            document.getElementById("btn7").addEventListener("click", () => changeMap(coordinates[6].latitude, coordinates[6].longitude));
            document.getElementById("btn8").addEventListener("click", () => changeMap(coordinates[7].latitude, coordinates[7].longitude));
            document.getElementById("btn9").addEventListener("click", () => changeMap(coordinates[8].latitude, coordinates[8].longitude));
            document.getElementById("btn10").addEventListener("click", () => changeMap(coordinates[9].latitude, coordinates[9].longitude));
        })
        .catch(error => console.error('Error loading coordinates:', error));
    
    function changeMap(latitude, longitude) {
        var map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: latitude, lng: longitude },
            zoom: 15
        });

        new google.maps.Marker({
            position: { lat: latitude, lng: longitude },
            map: map
        });
    }
});


const radioContainer = document.querySelector('.radio-btn-container');
const radioButtons = radioContainer.querySelectorAll('.radio-btn-label');
radioButtons.forEach(button => {
    button.addEventListener('click', () => {
        radioButtons.forEach(btn => {
            btn.classList.remove('selected');
        });
        button.classList.add('selected');
    });
});


var selectedValue = null;
document.querySelectorAll('input[name="mapOptions"]').forEach(function(radio) {
    radio.addEventListener('click', function() {
        selectedValue = this.value;
    });
});

document.getElementById('post-form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    if (selectedValue) {
        var formData = new FormData(this);
        formData.append('mapOption', selectedValue);

        fetch('/post', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            console.log(data); 
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } 
});


